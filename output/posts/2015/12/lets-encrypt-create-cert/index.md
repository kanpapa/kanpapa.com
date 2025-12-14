---
title: "Let's Encryptのサーバ証明書でhttps対応サイトにしてみた"
date: 2015-12-23
categories: 
  - "server"
---

[Let's Encrypt](https://letsencrypt.org/ "https://letsencrypt.org/")のサーバ証明書でこのkanpapa.comをhttps対応サイトにしてみました。

Let's Encryptは無償でSSL/TLSサーバー証明書の発行を行ってくれるサービスです。

SSL/TLS通信を行うためにはサーバー証明書を準備しなければなりませんが、通常はサーバー証明書は有償で発行していて、そのサーバの運営者情報まで確認できます。Let's Encryptで作成したサーバ証明書では運営者情報までは保証してくれません。このためサーバ証明書情報を確認すると「検証され信頼できる運営者情報はありません」となりますが、接続先が正しいサーバであることは証明でき、通信内容もSSL/TLSで暗号化されます。

サーバ証明書の作成方法は[Quick Start Guide](https://community.letsencrypt.org/t/quick-start-guide/1631/1 "Quick Start Guide")にも説明されていますが、まずはサーバー証明書の発行に必要なデータをホームディレクトリに持ってきます。

```
$ cd
$ git clone https://github.com/letsencrypt/letsencrypt

```

一旦httpdを停止します。

```
$ sudo /sbin/service httpd stop
Stopping httpd:                                   [  OK  ]
$
```

<!--more-->

作業ディレクトリに移動して、サーバ証明書の作成コマンドを実行します。

```
$ cd letsencrypt
$ ./letsencrypt-auto certonly --standalone -d kanpapa.com

```

途中メニュー画面が表示されますので指示通り入力します。（画面のキャプチャを忘れました・・）

メールアドレスを入力します。

```
Enter email address (used for urgent notices and lost key recovery)
（メールアドレスを入力）

```

続いて利用規約の確認です。

```
Please read the Terms of Service at
https://letsencrypt.org/documents/LE-SA-v1.0.1-July-27-2015.pdf. You
must agree in order to register with the ACME server at
https://acme-v01.api.letsencrypt.org/directory   　　 （了承する場合は、Agreeを選択）
```

  
処理が進み、次のメッセージが表示されれば、正常にサーバ証明書の作成が完了しています。

```
IMPORTANT NOTES:
- Congratulations! Your certificate and chain have been saved at
/etc/letsencrypt/live/www.kanpapa.com/fullchain.pem. Your cert will
expire on 2016-03-04. To obtain a new version of the certificate in
the future, simply run Let's Encrypt again.
- If like Let's Encrypt, please consider supporting our work by:   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate   Donating to EFF:                    https://eff.org/donate-le

```

サーバ証明書は/etc/letsencrypt/live/ドメイン名以下のディレクトリにできています。  
確認してみましょう。

```
$ sudo ls /etc/letsencrypt/live/kanpapa.com
cert.pem  chain.pem  fullchain.pem  privkey.pem

```

ここに作成されたサーバ証明書を/etc/httpd/conf.d/ssl.confに組み込みます。

```
SSLCertificateFile /etc/letsencrypt/live/kanpapa.com/cert.pem
SSLCertificateKeyFile /etc/letsencrypt/live/kanpapa.com/privkey.pem
SSLCertificateChainFile /etc/letsencrypt/live/kanpapa.com/chain.pem

```

あとはhttpdを起動すれば、httpsが使えるようになります。  
もし、iptableで443を閉じている場合は忘れずに開放しましょう。

しかし、このままだと http:// のパスが残っているところがあるので鍵のマークが表示されない場合があります。このため、MovableTypeの設定やコンテンツのパスをすべて https:// に変更する必要があります。それはまた次回で。
