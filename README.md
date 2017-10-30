# Flask-Blog
A simple flask blog application.

## 1. Prequisites
Docker

## 2. Setup mariadb image
    $ docker run --name <image's name:db> -e MYSQL_ROOT_PASSWORD=anything -d -p 8080:8080 mariadb
    $ docker run --name mysql-client -it --link <image's name:db>:mysql --rm mariadb sh -c 'exec mysql -uroot -p<password> -hmysql'

## 3. Setup flask_blog image
    $ docker build -t <image:flask_blog> .
    $ docker run -id -p 5000:5000 -v <folder_source>:/opt/flask_blog --name --link <image's name:blog> db:mysql <image:flask_blog> bash

## 4. Connect mariadb
    $ docker exec -it db /bin/bash
### 4.1. In terminal run
    $ export TERM=$(TERM:-dumb)
    $ mysql -u root -p

## 5. Connect blog
    $ docker exec -it blog bash

### 5.1. DB Migrations - create database 'blog' first 
    $ python manage.py db init
    $ python manage.py db migrate
    $ python manage.py db upgrade

### 5.2. Run - localhost
    $ python manage.py runserver
