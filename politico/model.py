from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


db = SQLAlchemy()


class Person(db.Model):
  __tablename__ = 'person'
  id = db.Column(db.Integer, primary_key=True)
  govtrack_id = db.Column(db.Integer, unique=True)
  osid_id = db.Column(db.Unicode(8), unique=True)
  firstname = db.Column(db.Unicode(64))
  lastname = db.Column(db.Unicode(64))
  twitterid = db.Column(db.Unicode(64))
  roles = db.relationship('Role', backref='person')
  twitter_profile = db.relationship('TwitterProfile', uselist=False, backref='person')


class Role(db.Model):
  __tablename__ = 'role'
  id = db.Column(db.Integer, primary_key=True)
  govtrack_id = db.Column(db.Integer, unique=True)
  person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
  state = db.Column(db.Unicode(3))
  role_type = db.Column(db.Unicode(64))
  start_date = db.Column(db.Unicode(64))
  end_date = db.Column(db.Unicode(64))


class TwitterProfile(db.Model):
  __tablename__ = 'twitter_profile'
  id = db.Column(db.Integer, primary_key=True)
  picture = db.Column(db.Unicode(512))
  statuses_count = db.Column(db.Integer)
  followers_count = db.Column(db.Integer)
  retweet_count = db.Column(db.Integer)
  person_id = db.Column(db.Integer, db.ForeignKey('person.id'))


def make_conn_str():
  """Make an in memory database for now."""
  return 'sqlite:///politico.db'
