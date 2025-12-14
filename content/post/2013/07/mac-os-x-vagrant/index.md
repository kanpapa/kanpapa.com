---
title: "Mac OS XにVagrantをインストールしました"
date: 2013-07-07
slug: "mac-os-x-vagrant"
categories: 
  - "pc"
tags: 
  - "mac"
---

[Chef](http://www.opscode.com/chef/ "http://www.opscode.com/chef/")のテスト環境としてVagrantが良いという話なのでMacにインストールしてみました。

少し前だとgemでインストールしていたようですが、Vagrant version 1.2.2だとMac用に.dmgが提供されているので普通のMacのアプリケーションと同様のインストールです。

流れはこんな感じ。我が家のMac OS Xは10.8.4(Mountain Lion)です。

(1) Oracle VM VirtualBoxをダウンロードしてインストールする。  
　[https://www.virtualbox.org](https://www.virtualbox.org "https://www.virtualbox.org")  
　今回はVirtualBox 4.2.16 for OS X hostsを使いました。  
(2) Vagrantをダウンロードしてインストールする。  
　[http://downloads.vagrantup.com](http://downloads.vagrantup.com "http://downloads.vagrantup.com")  
　今回は1.2.2を使いました。  
(3) VMの本体は以下にあります。  
　[http://www.vagrantbox.es](http://www.vagrantbox.es "http://www.vagrantbox.es")  
　今回はCentOS 6.4 x86\_64 Minimal (VirtualBox Guest Additions 4.2.12, Chef 11.4.4, Puppet 3.1.1)を使うことにしました。  
(4) あとはターミナルを立ち上げて以下のように操作しました。

```
$ vagrant -v
Vagrant version 1.2.2
$ vagrant box add base http://developer.nrel.gov/downloads/vagrant-boxes/CentOS-6.4-x86_64-v20130427.box
Downloading or copying the box...
（VM本体がダウンロードされる。サイズが大きいので我が家だと40分ぐらいかかりましした。）
Successfully added box 'base' with provider 'virtualbox'!
$ mkdir ~/Vagrant
$ cd ~/Vagrant
$ vagrant init
A `Vagrantfile` has been placed in this directory. You are now
ready to `vagrant up` your first virtual environment! Please read
the comments in the Vagrantfile as well as documentation on
`vagrantup.com` for more information on using Vagrant.
$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
[default] Importing base box 'base'...
[default] Matching MAC address for NAT networking...
[default] Setting the name of the VM...
[default] Clearing any previously set forwarded ports...
[default] Creating shared folders metadata...
[default] Clearing any previously set network interfaces...
[default] Preparing network interfaces based on configuration...
[default] Forwarding ports...
[default] -- 22 => 2222 (adapter 1)
[default] Booting VM...
[default] Waiting for VM to boot. This can take a few minutes.
[default] VM booted and ready for use!
[default] Configuring and enabling network interfaces...
[default] Mounting shared folders...
[default] -- /vagrant
$ vagrant ssh
Last login: Sat Jul 6 22:34:58 2013 from 10.0.2.2
Welcome to your Vagrant-built virtual machine.
[vagrant@localhost ~]$
```

へ〜。簡単ですね。もうVMができちゃったです。  
でもChefのテスト環境として使うにはもう少しカスタマイズが必要のようです。
