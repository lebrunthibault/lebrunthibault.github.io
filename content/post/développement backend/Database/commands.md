# MySql

- import : `mysql -u username -p dbname < file.sql`
- export : `/usr/bin/mysqldump -u dbusername -p'dbpassword' dbname > /path/backup.sql`



# Postgres

- import : `cat nom_de_la_base.pgdump | psql -d nom_de_la_base`
- export : `pg_dump nom_de_la_base > nom_de_la_base.pgdump`