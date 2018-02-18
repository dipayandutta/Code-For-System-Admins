#!/usr/bin/env bash

export DEBIAN_FRONTEND=noninteractive

wget http://dev.mysql.com/get/mysql-apt-config_0.6.0-1_all.deb

echo mysql-apt-config mysql-apt-config/repo-distro select ubuntu | debconf-set-selections
echo mysql-apt-config mysql-apt-config/repo-codename select trusty | debconf-set-selections
echo mysql-apt-config mysql-apt-config/select-server select mysql-5.7 | debconf-set-selections
echo mysql-community-server mysql-community-server/root-pass password securePassword | debconf-set-selections
echo mysql-community-server mysql-community-server/re-root-pass password securePassword | debconf-set-selections

dpkg -i mysql-apt-config_0.6.0-1_all.deb

apt-get update
apt-get install -y mysql-server --force-yes

apt-get install -y augeas-tools

augtool set /files/etc/mysql/my.cnf/target[3]/character-set-server utf8
augtool set /files/etc/mysql/my.cnf/target[3]/collation-server utf8_unicode_ci

service mysql restart
