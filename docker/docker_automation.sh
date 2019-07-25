#!/bin/bash

PROJECT_CONTAINER=ubuntuimg
IMAGE_NAME=ubuntu

docker run --name $PROJECT_CONTAINER -it -d ubuntu
docker exec -it $PROJECT_CONTAINER uname -a 
docker exec -it $PROJECT_CONTAINER apt-get update -y
docker exec -it $PROJECT_CONTAINER apt-get install net-tools -y
docker exec -it $PROJECT_CONTAINER apt-get install build-essential -y 
docker exec -it $PROJECT_CONTAINER apt-get install vim -y
docker exec -it $PROJECT_CONTAINER apt-get install python-software-properties -y
docker exec -it $PROJECT_CONTAINER apt-get install debconf-utils -y
docker exec -it $PROJECT_CONTAINER apt-get install software-properties-common -y

#Automate java installation
docker exec -it $PROJECT_CONTAINER add-apt-repository -y ppa:webupd8team/java 
docker exec -it $PROJECT_CONTAINER apt-get update -y
docker exec -it $PROJECT_CONTAINER echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | sudo debconf-set-selections
docker exec -it $PROJECT_CONTAINER echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 seen true" | debconf-set-selections
docker exec -it $PROJECT_CONTAINER  apt-get --assume-yes install oracle-java8-installer 
#docker exec -it $PROJECT_CONTAINER apt-get install oracle-java8-installer -y


#Automate mysql installation

MYSQL_PASS="secret"

docker exec -it $PROJECT_CONTAINER "mysql-community-server mysql-community-server/data-dir select ''" | sudo debconf-set-selections
docker exec -it $PROJECT_CONTAINER "mysql-community-server mysql-community-server/root-pass password $MYSQL_PASS" | sudo debconf-set-selections
docker exec -it $PROJECT_CONTAINER "mysql-community-server mysql-community-server/re-root-pass password $MYSQL_PASS" | sudo debconf-set-selections

docker exec -it $PROJECT_CONTAINER apt-get install -y mysql-server-5.7

#Commit Changes and make a new image
docker commit d41a9ab5d81a dipayandutta/ubuntu-java-mysql_install:1.0


#stop the container
docker stop ubuntuimg