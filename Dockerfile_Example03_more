# First add the image to work with
FROM ubuntu
# Add the name of the author or maintainer
MAINTAINER Dipayn Dutta inbox.dipayan@gmail.com
# run the commands 
RUN apt-get update && apt-get install -y openssh-server && apt-get install -y vim
# create a directory
RUN mkdir -p /var/run/sshd
# change the file permission
RUN chmod 0755 /var/run/sshd
# copy a file from the host machine to the container
ADD sshd_config /etc/ssh/sshd_config
# command to start a process
CMD /usr/sbin/sshd -D

# Entrypoint same as CMD without using special flags
#ENTRYPOINT /us/sbin/sshd
#docker run --rm -it dipayandutta/dockerfile_example_sshd -D here -D will work as the argument of the ENTRYPOINT
#Normally use CMD than ENTRYPOINT

USER nobody #docker run --rm -it dipayandutta/dockerfile_example_sshd id
WORKDIR /tmp #docker run --rm -it dipayandutta/dockerfile_example_sshd pwd
ENV foobar "Hello World" #docker run --rm -it dipayandutta/dockerfile_example_sshd env


# EXPOSE a port
EXPOSE 2222
