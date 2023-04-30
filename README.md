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

## App Home page

![alt text for screen readers](images/first.png "Text to show on mouseover").


## Bucket list page

![alt text for screen readers](images/first1.png "Text to show on mouseover").

## Adding destination to bucket list

![alt text for screen readers](images/second.png "Text to show on mouseover").

## Select from existing country drop down from data base/ entering a new country

![alt text for screen readers](images/third.png "Text to show on mouseover").

## Select from existing city drop down from data base/ entering a new city

![alt text for screen readers](images/forth.png "Text to show on mouseover").

## Enter the destination

![alt text for screen readers](images/fifth.png "Text to show on mouseover").

## Find the destination in the bucket list

![alt text for screen readers](images/sixth.png "Text to show on mouseover").

## Delete or Mark destination as visited

![alt text for screen readers](images/seventh.png "Text to show on mouseover").

