from unittest import result
from db.run_sql import run_sql
from models.destination import Destination
from models.country import Country
import repositories.country_repository as country_repository
from models.city import City
import repositories.city_repository as city_repository
from tests import country_test

def save(destination):
    sql = "INSERT INTO destinations (name, visited,city_id,country_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [destination.name,destination.visited,destination.city.id,destination.country.id]
    results = run_sql(sql,values)
    id = results[0]['id']
    destination.id = id
    return destination

def select_all():
    destinations = []
    sql = "SELECT * FROM destinations"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row["country_id"])
        city = city_repository.select(row["city_id"])
        destionation = Destination(row["name"],row["visited"],country,city,row["id"])
        destinations.append(destionation)
    return destinations

def select(id):
    sql = "SELECT * FROM destinations WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    country = country_repository.select(result["country_id"])
    city = city_repository.select(result["city_id"])
    destionation = Destination(result["name"],result["visited"],country,city,result["id"])
    return destionation

def delete_all():
    sql = "DELETE FROM destinations"
    run_sql(sql)

def delete(id):
    sql = "DELETE * FROM destinations WHERE id =%s"
    values = [id]
    run_sql(sql,values)

def update(destination):
    sql = "UPDATE destionations SET(name,visited,country_id,city_id) VALUES (%s, %s, %s, %s) WHERE id = %s"
    values = [destination.name,destination.visited, destination.country.id,destination.city.id,]
    run_sql(sql,values)





