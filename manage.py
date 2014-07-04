#!/usr/bin/env python


"""Scripts for interacting with the politico web server.

.. note::

  The scripts contained in this module are only useful when operating outside
  of the Heroku environment. When operating inside of the Heroku environment,
  one should use `foreman` -- a tool included with the Heroku toolchain.

"""

from configobj import ConfigObj
from validate import Validator
from flask.ext.script import Manager

from politico import app, init_webapp


manager = Manager(app)


@manager.command
def runserver(*args, **kwargs):
  """Override default `runserver` to init webapp before running."""
  app = init_webapp()
  # TODO(sholsapp): parameterize this, but don't clobber the *args, **kwargs
  # space, because it's annoying to have to pass these in to the `run` method.
  config = ConfigObj('config/sample.config', configspec='config/sample.configspec')
  app.config_obj = config
  print app.config_obj
  print args
  print kwargs
  app.run(*args, **kwargs)


if __name__ == "__main__":
  manager.run()
