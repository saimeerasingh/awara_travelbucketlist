from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.destination import Destination

import repositories.destination_repository as destination_repository

destinations_blueprint = Blueprint("destinations",__name__)

@destinations_blueprint.route('/destinations')
def destinations():
    destinations = destination_repository.select_all()
    return render_template('destinations/index.html', destinations = destinations)
    