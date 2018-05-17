import logging

from flask import Flask
from baskin import app as baskin_app

app = Flask(__name__)
app.register_blueprint(baskin_app)

logging.getLogger('flask_clova').setLevel(logging.DEBUG)


if __name__ == "__main__":
    app.config['CLOVA_VERIFY_REQUESTS'] = False
    app.run(host='0.0.0.0', port='80')