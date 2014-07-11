from flask import Flask, render_template, jsonify
from flask.ext.bootstrap import Bootstrap
from flask.ext.restless import APIManager

from politico.apis.osid import osid_blueprint
from politico.model import make_conn_str, db, Messages


app = Flask(__name__)


app.register_blueprint(osid_blueprint, url_prefix='/api/osid')


manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Messages, methods=['GET', 'POST'])


Bootstrap(app)


def init_webapp():
  app.config['SQLALCHEMY_DATABASE_URI'] = make_conn_str()
  db.app = app
  db.init_app(app)
  db.create_all()
  return app


@app.route('/')
def index():
  return render_template('index.html')
