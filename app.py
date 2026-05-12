from flask import Flask
from flask_cors import CORS

from routes.alert_routes import alert_routes

app = Flask(__name__)

CORS(app)

app.register_blueprint(alert_routes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)