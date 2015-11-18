shipbeat/proftpd
================

Essentially a fork from https://hub.docker.com/r/morrisjobke/docker-proftpd/ with very few modifications  
At shipbeat we use this container specifically for ftp'ing into a webserver, running in another container  
Like this:  

    docker run -p 21:21 -p 20:20 -p 12000-12005:12000-12005 \  
    --env USERNAME=username --env PASSWORD=password \  
    --volumes-from woocommerce:rw \  
    shipbeat/proftpd

    ftp -p $(docker-machine ip devbox) 21
    Name (192.168.99.100:kristian): username
    Password:
    ftp> ls

Have fun!
