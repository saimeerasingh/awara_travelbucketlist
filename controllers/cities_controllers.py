from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City

import repositories.country_repository as country_repository
import repositories.destination_repository as destination_repository

import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities = cities)

# SHOW
@cities_blueprint.route('/cities/<id>', methods =['GET'])
def show_destinations(id):
    destinations = destination_repository.select_all()
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template('destinations/index.html', all_destinations = destinations, all_countries = countries, all_cities = cities)