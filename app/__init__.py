import traceback
from datetime import datetime

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask.json import JSONEncoder

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from pymongo import MongoClient

from app.tool import dbg
from config import config

# from flask_session import Session
# session = Session()

# mongodb = MongoClient(config.MONGODB_ADDRESS)
db = SQLAlchemy()
lm = LoginManager()
lm.session_protection = 'strong'
lm.login_view = 'auth.unlogin'


class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, datetime):
                ts = int(obj.timestamp())
                if ts < 0:
                    ts = 0
                return ts
            if isinstance(obj, float):
                return round(obj, 3)
            iterable = iter(obj)
        except TypeError:
            traceback.print_exc()
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config.config_list[config_name])
    config.config_list[config_name].init_app(app)

    # app.config['SESSION_MONGODB'] = mongodb
    # session.init_app(app)

    db.init_app(app)
    lm.init_app(app)

    # custome json encoder
    app.json_encoder = CustomJSONEncoder

    # request hook
    @app.before_request
    def before_request_demo():
        dbg(current_user.__dict__)
        dbg(session.get('_id'))

    # ======= some blueprints ========
    from .main import main_blueprint
    from .auth import auth_blueprint
    from .test import test_blueprint


    from .api_site  import api_site_blueprint
    from .api_backend import api_backend_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(test_blueprint, url_prefix='/test')

    app.register_blueprint(api_site_blueprint, url_prefix=config.API_SITE_PREFIX)
    app.register_blueprint(api_backend_blueprint, url_prefix=config.API_BACKEND_PREFIX)

    return app
