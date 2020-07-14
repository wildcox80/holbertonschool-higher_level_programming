<h1 align="center">0x0E-SQL_more_queries</h1>
<p align="center"> <img src="https://i.imgur.com/Kw6nfhY.png" /></p>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

[![Twitter Wilder](https://img.shields.io/twitter/follow/WildsRincon?label=Wilder_Rincon&style=social)](https://twitter.com/WildsRincon)

## Resources :notebook:

Read or watch:

- [How To Create a New User and Grant Permissions in MySQL](https://intranet.hbtn.io/rltoken/u4h2MXcCQfadszlRMQy-gw)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://intranet.hbtn.io/rltoken/9JjDTdvflUSxwxLNfW8sPg)
- [MySQL constraints](https://intranet.hbtn.io/rltoken/u1P3WmgxehiqwcLBMlksUA)
- [SQL technique: subqueries](https://intranet.hbtn.io/rltoken/YYpPtkqFeKSCsAU4Y_y3Og)
- [Basic query operation: the join](https://intranet.hbtn.io/rltoken/npLCp3WasK0SUSUQqCF25A)
- [SQL technique: multiple joins and the distinct keyword](https://intranet.hbtn.io/rltoken/GmRLMhkY-pPvjcpzyDvmRg)
- [SQL technique: join types](https://intranet.hbtn.io/rltoken/ryjyRRN7696rJV0maP03Xw)
- [SQL technique: union and minus](https://intranet.hbtn.io/rltoken/L7Fi5w8GZG5MSdQZ19e88g)
- [MySQL Cheat Sheet](https://intranet.hbtn.io/rltoken/V9vpLbtkFwV4EZYoiz2NBA)
- [The Seven Types of SQL Joins](https://intranet.hbtn.io/rltoken/ySKSdhFeMDddea07XrDzeQ)
- [MySQL Tutorial](https://intranet.hbtn.io/rltoken/-uqP0a89xUl3SsmV_ZtxRA)
- [SQL Style Guide](https://intranet.hbtn.io/rltoken/jn4SHgwVtOJF0LQYPEIs-g)
- [MySQL 5.7 SQL Statement Syntax](https://intranet.hbtn.io/rltoken/YjNAE7DcadDbT_a7iI0sYw)


## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a PRIMARY KEY
- What’s a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are JOIN and UNION


## Requirements

### General :minidisc:

- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
-A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc


 
## More Info

### Comments for your SQL file:

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

### Install MySQL 5.7 on Ubuntu 14.04 LTS

```
$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
...
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
$
```

<p><b>Don’t forget your root password</b></p>

Connect to your MySQL server:

```
$ mysql -hlocalhost -uroot -p
Password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 42
Server version: 5.7.8-rc MySQL Community Server (GPL)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
mysql> quit
Bye
$
```

If you have some issues to upgrade to 5.7, don’t hesitate to cleanup your server of any MySQL packages: sudo apt-get remove --purge mysql-server mysql-client mysql-common

### Use “container-on-demand” to run MySQL

- Ask for container Ubuntu 14.04 - Python 3.4
- Connect via SSH
- OR connect via the Web terminal
- In the container, you should start MySQL before playing with it:

```
$ service mysql start
 * MySQL Community Server 5.7.8-rc is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$
```

<p><b>In the container, credentials are root/root</b></p>

### How to import a SQL dump

```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

![images](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/3/bc2575fee3303b731031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20200714%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200714T140842Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=25e63418ba2525e663406ce1dbf94370331ffb72ac2ed87d324dfee1071f15b8)


## Task :notebook:

### Mandatory :heavy_check_mark:
- My privileges! 
- Root user
- Read user
- Always a name
- ID can't be null 
- Unique ID
- States table
- Cities table
- Cities of California
- Cities by States
- Genre ID by show
- Genre ID for all shows
- No genre
- Number of shows by genre
- My genres
- Only Comedy
- List shows and genres

### Advanced :red_circle:
- Not my genre
- No Comedy tonight!
- Rotten tomatoes
- Best genre
- How Do SQL Database Engines Work?

## Authors :busts_in_silhouette: 
[@Wilder Rincón - Github](https://github.com/wildcox80)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/wildcox80/holberton-system_engineering-devops.svg?style=plastic
[contributors-url]: https://github.com/wildcox80/holberton-system_engineering-devops/graphs/contributors
[license-shield]: https://img.shields.io/github/license/wildcox80/holberton-system_engineering-devops.svg?style=plastic
[license-url]: https://github.com/wildcox80/holberton-system_engineering-devops/blob/master/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=plastic&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/wildsrincon