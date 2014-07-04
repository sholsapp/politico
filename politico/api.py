from flask import Blueprint, jsonify
import requests
import urllib
import urlparse


config = None


api = Blueprint('api', __name__, template_folder='templates')


@api.record
def get_config(setup_state):
  """Get's the main app's configuration.

  The OpenSecrets.org API client requires a key that we load at startup and
  store in the application's configuration. We store it here so we can use the
  client here.

  """
  global config
  config = setup_state.app.config


@api.route('/legislators/<state>')
def legislators(state):

  query = urllib.urlencode({
    'method': 'getLegislators',
    'id': state,
    'apikey': config['opensecrets']['api_key'],
    'output': 'json',
  })

  # This is pretty janky, but the urlparse
  # documents are available for reference at
  # https://docs.python.org/2/library/urlparse.html#urlparse.urlunparse,
  # where you can validate this tuple ordering.
  url = urlparse.urlunparse((
    config['opensecrets']['scheme'],
    config['opensecrets']['netloc'],
    config['opensecrets']['api_path'],
    None,
    query,
    None,
  ))

  return jsonify({
    'state': state,
    'legislators': requests.get(url).json()['response']['legislator'],
  })
