import requests
import os
from flask import request, jsonify
from dotenv import load_dotenv
from flask_api import status

load_dotenv()

def configure_routes(app):
    @app.route('/temperature', methods=['GET'])
    def search_city():
        API_KEY = os.environ['API_KEY']
        city = request.args.get('city')  # city name passed as argument

        if 1:
            pass

        # call API and convert response into Python dictionary
        url = f'http://api.weatherapi.com/v1/current.json?q={city}&key={API_KEY}'
        response = requests.get(url).json()

        current_temperature = response.get('current', {}).get('temp_c')

        if current_temperature:
            temp = {city.title(): current_temperature}
            return jsonify(temp)
        else:
            return jsonify({"message": "Internal Server Error"})

    @app.route('/',methods=['POST'])
    @app.route('/temperature', methods=['POST'])
    def error():
        return jsonify({"message":"The method is not allowed for the requested URL."}), status.HTTP_405_METHOD_NOT_ALLOWED

    @app.route('/')
    def index():
        name = {"firstname":"civan","lastname":"akbas"}
        return jsonify(name)
