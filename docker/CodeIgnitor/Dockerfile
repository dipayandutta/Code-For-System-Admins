FROM centos
MAINTAINER dipayan
RUN yum update -y
RUN yum groupinstall "Development Tools" -y
#install apache application server
RUN yum install httpd -y

# INSTALL PHP
RUN yum install vim -y
RUN yum install yum-utils -y
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm  && rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
RUN yum install php php-pear php-pdo php-mysqli php-soap php-xmlrpc php-mbstring -y

COPY php_info.php /var/www/html

# Create the http starting point 
ENTRYPOINT ["/usr/sbin/httpd","-D","FOREGROUND"]