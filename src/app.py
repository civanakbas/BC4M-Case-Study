from flask import Flask
from routes import configure_routes
import os

app = Flask(__name__)

configure_routes(app)

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(debug=True, port=port, host="0.0.0.0")
