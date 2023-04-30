# Awara - the travel bucket list 

## Steps to run the app

- **Git clone** the repository
- **Create the Data base**
```
 createdb awara_bucketlist
```
- cd into db and run the psql command to create the tables
```
 psql -d awara_bucketlist -f awara_bucketlist.sql
```
- run console.py to populate the database
```
 python3 console.py
```
- run the **Flask App**
```
 flask run
```


