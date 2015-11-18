FROM ubuntu
MAINTAINER Kristian Østergaard Martensen <km@shipbeat.com>

RUN apt-get update -y
RUN apt-get install -y proftpd

ADD launch /launch
ADD proftpd.conf /etc/proftpd/proftpd.conf
RUN sudo chown root:root /etc/proftpd/proftpd.conf

EXPOSE 20 21
EXPOSE 12000-12005

ENTRYPOINT /launch
