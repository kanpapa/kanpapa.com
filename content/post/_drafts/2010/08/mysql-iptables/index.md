---
title: "２日目 DBサーバとiptablesのセットアップ"
date: 2010-08-22
slug: "mysql-iptables"
draft: true
---

MySQLをインストールします。  
  

```
$ sudo yum -y install mysql-server 
[sudo] password for xxxxxxxx: 
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * addons: rsync.atworks.co.jp
 * base: rsync.atworks.co.jp
 * extras: rsync.atworks.co.jp
 * updates: rsync.atworks.co.jp
Setting up Install Process
Resolving Dependencies
--> Running transaction check
---> Package mysql-server.x86_64 0:5.0.77-4.el5_5.3 set to be updated
--> Processing Dependency: mysql = 5.0.77-4.el5_5.3 for package: mysql-server
--> Processing Dependency: perl-DBD-MySQL for package: mysql-server
--> Processing Dependency: libmysqlclient.so.15(libmysqlclient_15)(64bit) for package: mysql-server
--> Processing Dependency: libmysqlclient_r.so.15(libmysqlclient_15)(64bit) for package: mysql-server
--> Processing Dependency: perl(DBI) for package: mysql-server
--> Processing Dependency: perl-DBI for package: mysql-server
--> Processing Dependency: libmysqlclient_r.so.15()(64bit) for package: mysql-server
--> Processing Dependency: libmysqlclient.so.15()(64bit) for package: mysql-server
--> Running transaction check
---> Package mysql.x86_64 0:5.0.77-4.el5_5.3 set to be updated
---> Package perl-DBD-MySQL.x86_64 0:3.0007-2.el5 set to be updated
---> Package perl-DBI.x86_64 0:1.52-2.el5 set to be updated
--> Finished Dependency Resolution
Dependencies Resolved
================================================================================
 Package              Arch         Version                  Repository     Size
================================================================================
Installing:
 mysql-server         x86_64       5.0.77-4.el5_5.3         updates       9.8 M
Installing for dependencies:
 mysql                x86_64       5.0.77-4.el5_5.3         updates       4.8 M
 perl-DBD-MySQL       x86_64       3.0007-2.el5             base          148 k
 perl-DBI             x86_64       1.52-2.el5               base          600 k
Transaction Summary
================================================================================
Install       4 Package(s)
Upgrade       0 Package(s)
Total download size: 15 M
Downloading Packages:
(1/4): perl-DBD-MySQL-3.0007-2.el5.x86_64.rpm            | 148 kB     00:00     
(2/4): perl-DBI-1.52-2.el5.x86_64.rpm                    | 600 kB     00:00     
(3/4): mysql-5.0.77-4.el5_5.3.x86_64.rpm                 | 4.8 MB     00:00     
(4/4): mysql-server-5.0.77-4.el5_5.3.x86_64.rpm          | 9.8 MB     00:01     
--------------------------------------------------------------------------------
Total                                           8.5 MB/s |  15 MB     00:01     
Running rpm_check_debug
Running Transaction Test
Finished Transaction Test
Transaction Test Succeeded
Running Transaction
  Installing     : perl-DBI                                                 1/4 
  Installing     : mysql                                                    2/4 
  Installing     : perl-DBD-MySQL                                           3/4 
  Installing     : mysql-server                                             4/4 
Installed:
  mysql-server.x86_64 0:5.0.77-4.el5_5.3                                        
Dependency Installed:
  mysql.x86_64 0:5.0.77-4.el5_5.3      perl-DBD-MySQL.x86_64 0:3.0007-2.el5     
  perl-DBI.x86_64 0:1.52-2.el5        
Complete!

```

  
次はMovable Typeで使用するImageMagickをインストール  
  

```
$ sudo yum -y install ImageMagick-perl
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * addons: rsync.atworks.co.jp
 * base: rsync.atworks.co.jp
 * extras: rsync.atworks.co.jp
 * updates: rsync.atworks.co.jp
Setting up Install Process
Resolving Dependencies
--> Running transaction check
---> Package ImageMagick-perl.x86_64 0:6.2.8.0-4.el5_1.1 set to be updated
updates/filelists_db                                     | 1.3 MB     00:00     
--> Processing Dependency: ImageMagick = 6.2.8.0-4.el5_1.1 for package: ImageMagick-perl
--> Processing Dependency: libMagick.so.10()(64bit) for package: ImageMagick-perl
--> Processing Dependency: liblcms.so.1()(64bit) for package: ImageMagick-perl
--> Running transaction check
---> Package ImageMagick.x86_64 0:6.2.8.0-4.el5_1.1 set to be updated
--> Processing Dependency: librsvg-2.so.2()(64bit) for package: ImageMagick
--> Processing Dependency: libgs.so.8()(64bit) for package: ImageMagick
--> Processing Dependency: libwmflite-0.2.so.7()(64bit) for package: ImageMagick
---> Package lcms.x86_64 0:1.18-0.1.beta1.el5_3.2 set to be updated
--> Running transaction check
---> Package ghostscript.x86_64 0:8.15.2-9.11.el5 set to be updated
--> Processing Dependency: urw-fonts >= 1.1 for package: ghostscript
--> Processing Dependency: ghostscript-fonts for package: ghostscript
---> Package librsvg2.x86_64 0:2.16.1-1.el5 set to be updated
--> Processing Dependency: libgsf >= 1.6.0 for package: librsvg2
--> Processing Dependency: libcroco >= 0.6.1 for package: librsvg2
--> Processing Dependency: libgsf-1.so.114()(64bit) for package: librsvg2
--> Processing Dependency: libcroco-0.6.so.3()(64bit) for package: librsvg2
---> Package libwmf.x86_64 0:0.2.8.4-10.2 set to be updated
--> Processing Dependency: gd >= 2.0.21 for package: libwmf
--> Running transaction check
---> Package gd.x86_64 0:2.0.33-9.4.el5_4.2 set to be updated
---> Package ghostscript-fonts.noarch 0:5.50-13.1.1 set to be updated
---> Package libcroco.x86_64 0:0.6.1-2.1 set to be updated
---> Package libgsf.x86_64 0:1.14.1-6.1 set to be updated
---> Package urw-fonts.noarch 0:2.3-6.1.1 set to be updated
--> Finished Dependency Resolution
Dependencies Resolved
================================================================================
 Package                Arch        Version                     Repository
                                                                           Size
================================================================================
Installing:
 ImageMagick-perl       x86_64      6.2.8.0-4.el5_1.1           base      147 k
Installing for dependencies:
 ImageMagick            x86_64      6.2.8.0-4.el5_1.1           base      3.3 M
 gd                     x86_64      2.0.33-9.4.el5_4.2          base      155 k
 ghostscript            x86_64      8.15.2-9.11.el5             base      5.9 M
 ghostscript-fonts      noarch      5.50-13.1.1                 base      801 k
 lcms                   x86_64      1.18-0.1.beta1.el5_3.2      base      177 k
 libcroco               x86_64      0.6.1-2.1                   base      129 k
 libgsf                 x86_64      1.14.1-6.1                  base      113 k
 librsvg2               x86_64      2.16.1-1.el5                base      178 k
 libwmf                 x86_64      0.2.8.4-10.2                base      832 k
 urw-fonts              noarch      2.3-6.1.1                   base      4.5 M
Transaction Summary
================================================================================
Install      11 Package(s)
Upgrade       0 Package(s)
Total download size: 16 M
Downloading Packages:
(1/11): libgsf-1.14.1-6.1.x86_64.rpm                     | 113 kB     00:00     
(2/11): libcroco-0.6.1-2.1.x86_64.rpm                    | 129 kB     00:00     
(3/11): ImageMagick-perl-6.2.8.0-4.el5_1.1.x86_64.rpm    | 147 kB     00:00     
(4/11): gd-2.0.33-9.4.el5_4.2.x86_64.rpm                 | 155 kB     00:00     
(5/11): lcms-1.18-0.1.beta1.el5_3.2.x86_64.rpm           | 177 kB     00:00     
(6/11): librsvg2-2.16.1-1.el5.x86_64.rpm                 | 178 kB     00:00     
(7/11): ghostscript-fonts-5.50-13.1.1.noarch.rpm         | 801 kB     00:00     
(8/11): libwmf-0.2.8.4-10.2.x86_64.rpm                   | 832 kB     00:00     
(9/11): ImageMagick-6.2.8.0-4.el5_1.1.x86_64.rpm         | 3.3 MB     00:00     
(10/11): urw-fonts-2.3-6.1.1.noarch.rpm                  | 4.5 MB     00:00     
(11/11): ghostscript-8.15.2-9.11.el5.x86_64.rpm          | 5.9 MB     00:00     
--------------------------------------------------------------------------------
Total                                           6.9 MB/s |  16 MB     00:02     
Running rpm_check_debug
Running Transaction Test
Finished Transaction Test
Transaction Test Succeeded
Running Transaction
  Installing     : lcms                                                    1/11 
  Installing     : libcroco                                                2/11 
  Installing     : gd                                                      3/11 
  Installing     : libwmf                                                  4/11 
  Installing     : libgsf                                                  5/11 
  Installing     : librsvg2                                                6/11 
  Installing     : urw-fonts                                               7/11 
  Installing     : ghostscript                                             8/11 
  Installing     : ImageMagick                                             9/11 
  Installing     : ghostscript-fonts                                      10/11 
  Installing     : ImageMagick-perl                                       11/11 
Installed:
  ImageMagick-perl.x86_64 0:6.2.8.0-4.el5_1.1                                   
Dependency Installed:
  ImageMagick.x86_64 0:6.2.8.0-4.el5_1.1 gd.x86_64 0:2.0.33-9.4.el5_4.2        
  ghostscript.x86_64 0:8.15.2-9.11.el5   ghostscript-fonts.noarch 0:5.50-13.1.1
  lcms.x86_64 0:1.18-0.1.beta1.el5_3.2   libcroco.x86_64 0:0.6.1-2.1           
  libgsf.x86_64 0:1.14.1-6.1             librsvg2.x86_64 0:2.16.1-1.el5        
  libwmf.x86_64 0:0.2.8.4-10.2           urw-fonts.noarch 0:2.3-6.1.1          
Complete!

```

  
そうそう、MySQLを動かさないと  
  

```
$ sudo /etc/rc.d/init.d/mysqld start 
Initializing MySQL database:  Installing MySQL system tables...
OK
Filling help tables...
OK
To start mysqld at boot time you have to copy
support-files/mysql.server to the right place for your system
PLEASE REMEMBER TO SET A PASSWORD FOR THE MySQL root USER !
To do so, start the server, then issue the following commands:
/usr/bin/mysqladmin -u root password 'new-password'
/usr/bin/mysqladmin -u root -h xxxxxxxx.sakura.ne.jp password 'new-password'
Alternatively you can run:
/usr/bin/mysql_secure_installation
which will also give you the option of removing the test
databases and anonymous user created by default.  This is
strongly recommended for production servers.
See the manual for more instructions.
You can start the MySQL daemon with:
cd /usr ; /usr/bin/mysqld_safe &
You can test the MySQL daemon with mysql-test-run.pl
cd mysql-test ; perl mysql-test-run.pl
Please report any problems with the /usr/bin/mysqlbug script!
The latest information about MySQL is available on the web at
http://www.mysql.com
Support MySQL by buying support/licenses at http://shop.mysql.com
                                                           [  OK  ]
Starting MySQL:                                            [  OK  ]
$ sudo /usr/bin/mysql_secure_installation
NOTE: RUNNING ALL PARTS OF THIS SCRIPT IS RECOMMENDED FOR ALL MySQL
      SERVERS IN PRODUCTION USE!  PLEASE READ EACH STEP CAREFULLY!
In order to log into MySQL to secure it, we'll need the current
password for the root user.  If you've just installed MySQL, and
you haven't set the root password yet, the password will be blank,
so you should just press enter here.
Enter current password for root (enter for none): 
OK, successfully used password, moving on...
Setting the root password ensures that nobody can log into the MySQL
root user without the proper authorisation.
You already have a root password set, so you can safely answer 'n'.
Change the root password? [Y/n] n
 ... skipping.
By default, a MySQL installation has an anonymous user, allowing anyone
to log into MySQL without having to have a user account created for
them.  This is intended only for testing, and to make the installation
go a bit smoother.  You should remove them before moving into a
production environment.
Remove anonymous users? [Y/n] Y
 ... Success!
Normally, root should only be allowed to connect from 'localhost'.  This
ensures that someone cannot guess at the root password from the network.
Disallow root login remotely? [Y/n] Y
 ... Success!
By default, MySQL comes with a database named 'test' that anyone can
access.  This is also intended only for testing, and should be removed
before moving into a production environment.
Remove test database and access to it? [Y/n] Y
 - Dropping test database...
 ... Success!
 - Removing privileges on test database...
 ... Success!
Reloading the privilege tables will ensure that all changes made so far
will take effect immediately.
Reload privilege tables now? [Y/n] Y
 ... Success!
Cleaning up...
All done!  If you've completed all of the above steps, your MySQL
installation should now be secure.
Thanks for using MySQL!

```

  
次はiptablesの設定と。初期値はこんな感じ  
  

```
# iptables -n -L -v 
Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         
Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         
Chain OUTPUT (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         
#

```

  
安全を考え、まずはこんな設定にしてみました。 最低限のところしか開けません。  
  

```
# iptables -n -L -v
Chain INPUT (policy DROP 7 packets, 324 bytes)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 ACCEPT     all  --  lo     *       0.0.0.0/0            0.0.0.0/0           
    0     0 DROP       all  --  *      *       10.0.0.0/8           0.0.0.0/0           
    0     0 DROP       all  --  *      *       172.16.0.0/12        0.0.0.0/0           
    0     0 DROP       all  --  *      *       192.168.0.0/16       0.0.0.0/0           
  508 37088 ACCEPT     tcp  --  *      *       0.0.0.0/0            0.0.0.0/0           tcp dpt:22 
  164 12181 ACCEPT     tcp  --  *      *       0.0.0.0/0            0.0.0.0/0           tcp dpt:80 
    0     0 ACCEPT     tcp  --  *      *       0.0.0.0/0            0.0.0.0/0           tcp dpt:443 
   57 14728 ACCEPT     all  --  *      *       0.0.0.0/0            0.0.0.0/0           state RELATED,ESTABLISHED 
Chain FORWARD (policy DROP 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         
Chain OUTPUT (policy ACCEPT 764 packets, 618K bytes)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 ACCEPT     all  --  *      lo      0.0.0.0/0            0.0.0.0/0           
# iptables-save > /etc/sysconfig/iptables

```
