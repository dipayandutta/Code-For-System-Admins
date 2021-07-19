FROM centos
MAINTAINER dipayan
RUN yum update -y
RUN yum groupinstall "Development Tools" -y
RUN yum install httpd -y
ENTRYPOINT ["/usr/sbin/httpd","-D","FOREGROUND"]
