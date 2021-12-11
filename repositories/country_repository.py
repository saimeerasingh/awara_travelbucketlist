from unittest import result
from db.run_sql import run_sql
from models.country import Country

def save(country):
    sql = "INSERT INTO countries (name,continent,visited) VALUES (%s ,%s ,%s)RETURNING id"
    values = [country.name,country.continent,country.visited]
    results = run_sql(sql,values)
    id = results[0]['id']
    country.id = id

def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row["name"],row["continent"],row["visited"],row['id'])
        countries.append(country)
    return countries

def select(id):
    