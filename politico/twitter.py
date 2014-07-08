"""Yet another Twitter client."""

import base64
import requests

from brownie.caching import cached_property


class TwitterClient(object):
  """An application-only Twitter client.

  Why an application-only Twitter client? First, it's read-only. Second, it's
  simple REST. If the need comes about for a more complicated client, consider
  using python-twitter or twython. Until then, this will just keep things
  simple.

  Read more at https://dev.twitter.com/docs/auth/application-only-auth.

  """
  def __init__(self, consumer_key=None, consumer_secret=None):
    self.consumer_key = consumer_key
    self.consumer_secret = consumer_secret

  @cached_property
  def access_token(self):
    """The bearer access token required for API requests.

    This method fetches the access_token from the /oauth2/token endpoint by
    following the directions at
    https://dev.twitter.com/docs/auth/application-only-auth.

    """

    secret = base64.b64encode('%s:%s' % (self.consumer_key, self.consumer_secret))

    rsp = requests.post(
      'https://api.twitter.com/oauth2/token',
      headers={
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Authorization': 'Basic %s' % secret,
      },
      data='grant_type=client_credentials',
    )

    if not rsp.ok:
      raise RuntimeError('Failed to get access token from /oauth2/token endpoint!')

    return rsp.json()['access_token']

  def lookup(self, username):
    """Lookup a user's Twitter information.

    Read more at https://dev.twitter.com/docs/api/1/get/users/lookup.

    :param username: The user's Twitter screen name.

    """

    rsp = requests.get(
      'https://api.twitter.com/1.1/users/lookup.json?screen_name=%s' % username,
      headers={'Authorization': 'Bearer %s' % self.access_token},
    )

    return rsp.json()
