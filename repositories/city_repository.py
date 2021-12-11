from unittest import result
from db.run_sql import run_sql
from models.city import City
from models.country import Country
import repositories.country_repository as country_repository
from models.destination import Destination
import repositories.destination_repository as destination_repository

def save(city):
    sql ="INSERT INTO cities (name,visited) VALUES (%s ,%s) RETURNING id"
    values = [city.name,city.visited]
    results = run_sql(sql,values)
    id = results[0]['id']
    city.id = id

def select_all():
    cities = []
    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row["country_id"])
        city = City(row["name"],row["visited"],country,row["id"])
        cities.append(city)
    return cities

def select(id):
    sql = "SELECT * FROM cities WHERE id = %s "
    values = [id]
    result = run_sql(sql,values)[0]
    country = country_repository.select(result["country_id"])
    city = City(result["name"],result["visited"],country,result["id"])
    return city




