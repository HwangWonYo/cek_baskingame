"""
    Extension server for several services
    1. baskin robins
    2. japan word study
    3. sora godong nim

    Mainly use Flask and flask-clova module
    Two applications are registered by blueprint
"""
import logging
from flask import Flask

from baskin.main import app as baskin_app
from jpstudy.main import app as jpstudy_app
from soragodong.main import app as godong_app

app = Flask(__name__)
app.register_blueprint(baskin_app)
app.register_blueprint(jpstudy_app)
app.register_blueprint(godong_app)

logging.getLogger('flask_clova').setLevel(logging.DEBUG)


if __name__ == "__main__":
    app.config['CLOVA_VERIFY_REQUESTS'] = False
    app.config['CLOVA_PRETTY_DEBUG_LOGS'] = True
    app.run(host='0.0.0.0', port=80, debug=True)