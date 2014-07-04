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
from flask.ext.script import Manager, Command, Option

from politico import app, init_webapp


manager = Manager(app)


@manager.command
def runserver(config):
  """Override default `runserver` to init webapp before running."""
  config_obj = ConfigObj(config, configspec='config/politico.configspec')
  app.config.update(config_obj)
  init_webapp()
  app.run(debug=True)


if __name__ == "__main__":
  manager.run()
