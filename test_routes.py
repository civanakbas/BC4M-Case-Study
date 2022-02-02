from flask import Flask
from routes import configure_routes


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'
    response = client.get(url)

    assert response.status_code == 200


def test_temperature_route():
    app = Flask(__name__)

    configure_routes(app)
    client = app.test_client()
    url = '/temperature?city=istanbul'

    response = client.get(url)
    assert response.status_code == 200
