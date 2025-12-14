---
title: "GCPのVMを新しいOSのVMに移行しました"
date: 2023-04-01
slug: "gcp-gce-upgrades-focal"
categories: 
  - "server"
tags: 
  - "gcp"
image: "images/gcp-gce-log-explorer.jpg"
---

これまで[Google Cloud Platform（GCP）](https://cloud.google.com/)を利用しているのですが、Googleから「あなたが[Google](https://cloud.google.com/compute?hl=ja "Google Compute Engine (GCE)") [Compute Engine (GCE)](https://cloud.google.com/compute?hl=ja "Google Compute Engine (GCE)")のVMで使っているUbuntu 18.04 LTSが2023年5月31日にEOLになるので、Ubuntu 20.04 LTSまたはUbuntu Pro 18.04 LTSに移行してください。」とリマインドがありました。もうそんな時期なのかと早めに移行を実施しました。

### 移行手順を考える

考えてみた移行手順は以下の通りです。

1. バックアップとして現在のGCEのVMインスタンスのブートディスクのスナップショットをとる。
2. 新しいVMインスタンスをUbuntu 20.04 LTSでセットアップする。
3. スナップショットから新規のディスクを作成し、新しいVMインスタンスにマウント
4. アプリケーションやデータをマウントしたディスクから移行
5. 新しいOpsエージェントに切り替えていなかったので切り替え
6. 動作確認
7. 旧VMインスタンスの削除
8. スナップショットとそれから作成したディスクはしばらく残しておいて問題なければ削除

ほぼGCPのGUIでできるのですが、初めて行なったところだけメモしておきます。

### VMに新規のディスクをマウント

スナップショットから作成した新規のディスクをVMに接続したあと、mountするためのデバイス名はどこだろうと探したところ以下のコマンドでした。

```
$ sudo lsblkNAME    MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTloop0     7:0    0  55.6M  1 loop /snap/core18/2697loop1     7:1    0  63.3M  1 loop /snap/core20/1822loop2     7:2    0 337.9M  1 loop /snap/google-cloud-cli/111loop3     7:3    0  91.9M  1 loop /snap/lxd/24061loop4     7:4    0  49.9M  1 loop /snap/snapd/18357loop5     7:5    0  49.9M  1 loop /snap/snapd/18596loop6     7:6    0  55.6M  1 loop /snap/core18/2721loop7     7:7    0  63.3M  1 loop /snap/core20/1852loop8     7:8    0 333.4M  1 loop /snap/google-cloud-cli/119sda       8:0    0    20G  0 disk ├─sda1    8:1    0  19.9G  0 part /├─sda14   8:14   0     4M  0 part └─sda15   8:15   0   106M  0 part /boot/efisdb       8:16   0    20G  0 disk ├─sdb1    8:17   0  19.9G  0 part ├─sdb14   8:30   0     4M  0 part └─sdb15   8:31   0   106M  0 part 
```

デバイス名がわかればあとはマウントするだけです。

```
$ sudo mount -o discard,defaults /dev/sdb1 /mnt/disks/old-boot$ sudo lsblkNAME    MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTloop0     7:0    0  55.6M  1 loop /snap/core18/2697loop1     7:1    0  63.3M  1 loop /snap/core20/1822loop2     7:2    0 337.9M  1 loop /snap/google-cloud-cli/111loop3     7:3    0  91.9M  1 loop /snap/lxd/24061loop4     7:4    0  49.9M  1 loop /snap/snapd/18357loop5     7:5    0  49.9M  1 loop /snap/snapd/18596loop6     7:6    0  55.6M  1 loop /snap/core18/2721loop7     7:7    0  63.3M  1 loop /snap/core20/1852loop8     7:8    0 333.4M  1 loop /snap/google-cloud-cli/119sda       8:0    0    20G  0 disk ├─sda1    8:1    0  19.9G  0 part /├─sda14   8:14   0     4M  0 part └─sda15   8:15   0   106M  0 part /boot/efisdb       8:16   0    20G  0 disk ├─sdb1    8:17   0  19.9G  0 part /mnt/disks/old-boot├─sdb14   8:30   0     4M  0 part └─sdb15   8:31   0   106M  0 part $ dfFilesystem     1K-blocks     Used Available Use% Mounted on/dev/root       20134592  3388824  16729384  17% /devtmpfs          490268        0    490268   0% /devtmpfs             494588        0    494588   0% /dev/shmtmpfs              98920     1056     97864   2% /runtmpfs               5120        0      5120   0% /run/locktmpfs             494588        0    494588   0% /sys/fs/cgroup/dev/loop0         56960    56960         0 100% /snap/core18/2697/dev/loop1         64896    64896         0 100% /snap/core20/1822/dev/loop2        345984   345984         0 100% /snap/google-cloud-cli/111/dev/loop3         94080    94080         0 100% /snap/lxd/24061/dev/loop4         51072    51072         0 100% /snap/snapd/18357/dev/sda15        106858     6161    100697   6% /boot/efi/dev/loop5         51072    51072         0 100% /snap/snapd/18596/dev/loop6         56960    56960         0 100% /snap/core18/2721/dev/loop7         64896    64896         0 100% /snap/core20/1852/dev/loop8        341376   341376         0 100% /snap/google-cloud-cli/119tmpfs              98916        0     98916   0% /run/user/1003tmpfs              98916        0     98916   0% /run/user/1001/dev/sdb1       20134592 10285880   9832328  52% /mnt/disks/old-boot$ 
```

### LoggingエージェントからOpsエージェントへの移行

旧システムではアプリケーションのログを[Loggingエージェント](https://cloud.google.com/stackdriver/docs/solutions/agents/logging?hl=ja "Logging エージェント")でStackDriver Loggingに読み込んで、[BigQuery](https://cloud.google.com/bigquery?hl=ja "BigQuery")にシンクしていたのですが、Loggingエージェントの後継がCloud Loggingの[Opsエージェント](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent?hl=ja "Opsエージェント")になったようです。今後のこともあるので、新しいOpsエージェントに置き換えてみました。

旧システムのLoggingエージェントで追加設定していたファイルは以下の内容でした。

```
$ cat /etc/google-fluentd/config.d/wowhoneypot.conf  @type tail  format /^\[(?[^\]]*)\] (?[^ ]*) (?[^ ]*) "(?\S+)(?: +(?[^ ]*) +\S*)?" (?[^ ]*) (?[^ ]*) (?[^ ]*)$/  time_format %Y-%m-%d %H:%M:%S%z  path /opt/wowhoneypot/log/access_log  pos_file /var/lib/google-fluentd/pos/wowhoneypot.pos  read_from_head true  tag wowhoneypot-access
```

Opsエージェントは全く内容が異なるので、いろいろ試して以下の設定ファイルに落ち着きました。

```
$ cat /etc/google-cloud-ops-agent/config.yaml logging:  receivers:    wowhoneypot-access:      type: files      include_paths:      - /opt/wowhoneypot/log/access_log      record_log_file_path: true  service:    pipelines:      default_pipeline:        receivers: []      wow_pipeline:        receivers: [wowhoneypot-access]        processors: [wow_parse]  processors:    wow_parse:      type: parse_regex      regex: "^\[(?[^\]]*)\] (?[^ ]*) (?[^ ]*) \"(?\S+)(?: +(?[^ ]*) +\S*)?\" (?[^ ]*) (?[^ ]*) (?[^ ]*)$"     　time_key:    time     　time_format: "%Y-%m-%d %H:%M:%S%z"
```

これでデータがCloud Loggingに取り込まれ、BigQueryにもシンクしていることが確認できたので、Opsエージェントへの移行も完了です。

![gcp-gce-logexploer.png](images/gcp-gce-logexploer.png)

### まとめ

GCPなどのクラウドは変化が激しく、いつの間にか周りの仕組みが新しくなっているので久しぶりのシステム移行でやや戸惑いましたが、簡単な操作でさまざまな設定や操作もでき、マニュアルもある程度は揃っているのでやはりGCPは便利かなと思います。
