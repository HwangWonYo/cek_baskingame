import logging
from flask import Flask

from baskin.main import app as baskin_app
from jpstudy.main import app as jpstudy_app

app = Flask(__name__)
app.register_blueprint(baskin_app)
app.register_blueprint(jpstudy_app)

logging.getLogger('flask_clova').setLevel(logging.DEBUG)


if __name__ == "__main__":
    app.config['CLOVA_VERIFY_REQUESTS'] = False
    app.config['CLOVA_PRETTY_DEBUG_LOGS'] = True
    app.run(host='0.0.0.0', port=80, debug=True)