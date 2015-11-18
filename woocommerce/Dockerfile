FROM wordpress:latest
MAINTAINER Kristian Østergaard Martensen <km@shipbeat.com>

ENV WOOCOMMERCE_VERSION 2.4.10
ENV WOOCOMMERCE_UPSTREAM_VERSION 2.4.10
ENV FTP_VIRT_USER iamauser
ENV FTP_VIRT_PASS letmein

RUN apt-get update \
    && apt-get install -y --no-install-recommends unzip wget vsftpd db5.3-util \
    && wget https://downloads.wordpress.org/plugin/woocommerce.2.4.10.zip -O /tmp/temp.zip \
    && cd /usr/src/wordpress/wp-content/plugins \
    && unzip /tmp/temp.zip \
    && rm /tmp/temp.zip \
    && rm -rf /var/lib/apt/lists/*

# Download WordPress CLI
RUN curl -L "https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar" > /usr/bin/wp && \
    chmod +x /usr/bin/wp

VOLUME ["/var/www/html"]
