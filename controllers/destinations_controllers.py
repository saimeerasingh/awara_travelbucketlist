import sys
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from controllers.cities_controllers import cities
from controllers.countries_controllers import countries
from models.city import City
from models.destination import Destination
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

from models.country import Country

import repositories.destination_repository as destination_repository

destinations_blueprint = Blueprint("destinations",__name__)

@destinations_blueprint.route('/destinations')
def destinations():
    destinations = destination_repository.select_all()
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template('destinations/index.html', all_destinations = destinations, all_countries = countries,all_cities = cities)

# NEW
# GET '/destinations/new'
@destinations_blueprint.route('/destinations/new', methods = ['GET'])
def new_destinations():
    # country =  Country(request.form['country'],request.form['continent'],False)
    destinations = destination_repository.select_all()
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template('destinations/index.html', all_destinations = destinations, all_countries = countries, all_cities = cities)
    
    

# CREATE
# POST '/destinations
@destinations_blueprint.route('/destinations/new', methods = ['POST'])
def create_destination():
    country_id = request.form['country']
    city_id = request.form['city']
    dest_dest = request.form['destination']
    visited = True if 'visited' in request.form else False
    country = country_repository.select(country_id)
    city = city_repository.select(city_id)
    destination = Destination(name=dest_dest,visited= visited,city=city,country=country,id=id)
    destination_repository.save(destination)
    return redirect ('/mybucketlist')

@destinations_blueprint.route('/mybucketlist/<id>',methods = ['POST'])
def update_destination(id):
    country_id = request.form['country']
    city_id = request.form['city']
    dest_dest = request.form['destination']
    visited = True if 'visited' in request.form else False
    country = country_repository.select(country_id)
    city = city_repository.select(city_id)
    destination = Destination(name=dest_dest,visited= visited,city=city,country=country,id =id)
    destination_repository.update(destination)
    return redirect('/mybucketlist')

@destinations_blueprint.route('/mybucketlist/<id>/set/not/visted', methods =['POST'])
def set_not_visited_destination(id):
    destination = destination_repository.select(id)
    destination.visited = False
    print("not visisted", destination.id , destination.name , destination.visited, file=sys.stderr)
    destination_repository.update(destination)
    return redirect('/mybucketlist')

@destinations_blueprint.route('/mybucketlist/<id>/set/visted', methods =['POST'])
def set_visited_destination(id):
    destination = destination_repository.select(id)
    destination.visited = True
    destination_repository.update(destination)
    return redirect('/mybucketlist')

@destinations_blueprint.route('/mybucketlist/<id>/delete', methods =['POST'])
def delete_destination(id):
    destination_repository.delete(id)
    return redirect('/mybucketlist')

@destinations_blueprint.route('/mybucketlist/search', methods =['POST'])
def search_destination():
    print(request.form,file=sys.stderr)
    search_name = request.form['search']
    search_result = destination_repository.search_all(search_name)
    print(search_result,file=sys.stderr)
    # destination_repository.delete(id)
    return redirect('/mybucketlist')

