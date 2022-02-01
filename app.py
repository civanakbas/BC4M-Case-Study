import requests
import os
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/temperature/city')
def search_city():
    API_KEY = os.environ['API_KEY']
    city = request.args.get('q')  # city name passed as argument

    # call API and convert response into Python dictionary
    url = f'http://api.weatherapi.com/v1/current.json?q={city}&key={API_KEY}'
    response = requests.get(url).json()

    current_temperature = response.get('current', {}).get('temp_c')

    if current_temperature:
        return f'Current temperature of {city.title()} is {current_temperature} &#8451;'
    else:
        return f'Error getting temperature for {city.title()}'


@app.route('/')
def index():
    return '<h1>Welcome to weather app</h1>'


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
