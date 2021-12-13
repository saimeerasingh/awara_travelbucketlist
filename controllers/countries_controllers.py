from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("mybucketlist", __name__)

@countries_blueprint.route("/mybucketlist")
def countries():
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template("mybucketlist/index.html", all_countries = countries, all_cities = cities)

# NEW
# GET '/countries/new'
# @countries_blueprint.route('/mybucketlist/new', methods =['GET'])
# def new_country():
#     countries = country_repository.select_all
#     return render_template("mybucketlist/index.html", all_countries = countries)

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
