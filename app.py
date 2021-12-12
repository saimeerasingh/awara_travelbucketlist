from flask import Flask, render_template

from controllers.countries_controllers import countries_blueprint
from controllers.cities_controllers import cities_blueprint
from controllers.destinations_controllers import destinations_blueprint

app = Flask(__name__)

app.register_blueprint(countries_blueprint)
app.register_blueprint(cities_blueprint)
app.register_blueprint(destinations_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)