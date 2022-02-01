from flask import Flask
from routes import configure_routes

app = Flask(__name__)

configure_routes(app)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
