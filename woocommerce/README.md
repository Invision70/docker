Essentially a fork from https://hub.docker.com/r/agrothberg/docker-woocommerce/ with some modifications to it.  
At shipbeat we use this container specifically for testing our woocommerce integration.  

This container has to be linked with a mysql container, and can be started like this:  

    docker run --name woobeat --link some-mysql:mysql -d shipbeat/woocommerce

But I'd say the best option is to start it with Docker Compose.  
A docker-compose.yml like this one will do the trick:  

    webserver:
       container_name: woocommerce
       image: shipbeat/woocommerce
       links:
        - dbserver:mysql
       ports:
        - 8080:80

    dbserver:
       container_name: woo_mariadb
       image: mariadb
       environment:
        MYSQL_ROOT_PASSWORD: example
       ports:
        - 3307:3306

By then, you'll be able to access your freshly installed wordpress on port 8080.

    curl http://$(docker-machine ip devbox):8080

You may want to check out https://hub.docker.com/_/wordpress/ for further documentation.  
Have fun!
