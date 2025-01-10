# api.py

from flask import Flask
from routes import register_all_routes

app = Flask(__name__)

# Register all routes using the utility function
register_all_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)