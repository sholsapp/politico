from flask import Blueprint, abort, jsonify
import logging
import requests
import urllib
import urlparse


log = logging.getLogger(__name__)


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

  rsp = requests.get(url)

  if rsp.ok:
    legislators = []
    # This deconstructs the response from the OpenSecrets.org response, which
    # uses some funky not-especially-help keys.
    for legislator in rsp.json()['response']['legislator']:
      legislators.append(legislator['@attributes'])
    return jsonify({
      'state': state,
      'legislators': legislators,
    })

  else:
    log.info('OpenSecrets.org responded with a %s!', rsp.status_code)
    # TODO(sholsapp): add paradigm for graceful API failure, we want to return
    # something nice to our client, not just 500.
    abort(500)
