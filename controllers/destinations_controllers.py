from flask import Flask, render_template, request, redirect
from flask import Blueprint
from controllers.cities_controllers import cities
from controllers.countries_controllers import countries
from models.city import City
from models.destination import Destination
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import sys
from models.country import Country

import repositories.destination_repository as destination_repository

destinations_blueprint = Blueprint("destinations",__name__)

@destinations_blueprint.route('/destinations')
def destinations():
    destinations = destination_repository.select_all()
    return render_template('destinations/index.html', all_destinations = destinations)

# NEW
# GET '/destinations/new'
@destinations_blueprint.route('/destinations/new', methods = ['POST'])
def new_destinations():
    country =  Country(request.form['country'],request.form['continent'],False)
    country_id = country_repository.save(country)
    print(countries,file=sys.stderr)

    city = City(request.form['city'],False,country_id=country_id)
    city_repository.save(city)
    return redirect('/')
    

# CREATE
# POST '/countries

# SHOW
# GET '/countries/<id>'

# EDIT
# GET '/countries/<id>/edit'

# UPDATE
# PUT '/countries/<id>'

# DELETE
# DELETE '/countries/<id>'

