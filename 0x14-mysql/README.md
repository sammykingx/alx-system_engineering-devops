# 0x14-mysql

![mysql](https://www.simplilearn.com/ice9/free_resources_article_thumb/difference_between_sql_and_mysql.jpg)

The MySQL server provides a database management system with querying and connectivity capabilities, as well as the ability to have excellent data structure and integration with many different platforms.

## Needed Knowledge

- [What is a primary-replica cluster](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication)

- [MySQL primary replica setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql)

- [Build a robust database backup strategy](https://www.databasejournal.com/ms-sql/developing-a-sql-server-backup-strategy/)

- `mysqldump`

## Learning Objectives

- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- What operation should you regularly perform to make sure that your database backup strategy actually works

## Project Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on `Ubuntu 16.04 LTS`
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck __(version 0.3.7-5~ubuntu16.04.1 via apt-get)__ without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Installation Guide for mysql 5.7.*

- First go to site [dev.mysql.com](https://dev.mysql.com/doc/refman/5.7/en/checking-gpg-signature.html) and copy the PGP PUBLIC KEY just immediately under the _Notice_ section to your clipboard.

- Create a new file in your terminal with a .key extension and paste the PGP PUB KEY copied to clipboard.
- Then do the following

```bash
$ sudo apt-key add name_of_file.key
OK

# adding it to the apt repo
$ sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'

# updating the apt repo to add the url i added earlier
$ sudo apt-get update

# now check your available versions
$ sudo apt-cache policy mysql-server
mysql-server:
  Installed: (none)
  Candidate: 8.0.31-0ubuntu0.20.04.2
  Version table:
     8.0.31-0ubuntu0.20.04.2 500
        500 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages
     8.0.31-0ubuntu0.20.04.1 500
        500 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages
     8.0.19-0ubuntu5 500
        500 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 Packages
     5.7.40-1ubuntu18.04 500
        500 http://repo.mysql.com/apt/ubuntu bionic/mysql-5.7 amd64 Packages

# Now am installing mysql 5.7.*
$ sudo apt-get install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7* -y
```
