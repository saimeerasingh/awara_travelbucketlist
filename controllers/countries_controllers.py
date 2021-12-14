from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.destination_repository as destination_repository
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("mybucketlist", __name__)

@countries_blueprint.route("/mybucketlist")
def countries():
    destinations = destination_repository.select_all()
    return render_template("mybucketlist/index.html", all_destinations = destinations)

# @countries_blueprint.route('/mybucketlist/<id>/delete', methods =['POST'])
# def delete_destination(id):
#     # destinations = destination_repository.select_all()
#     destination_repository.delete(id)
#     # render_template("mybucketlist/index.html", all_destinations = destinations)
#     return redirect('/mybucketlist')