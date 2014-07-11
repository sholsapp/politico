# politico

A visual tool for finding, following and contacting legislators powered by
https://www.govtrack.us/.

# developers

This tool is mostly a mashup of several API out there today. This section
discusses those API, viz., how to configure your *politico* instance to use
your own API keys.

## configuration

You'll need to obtain your own application keys for the API that we use in
politico.

### GovTrack.us

This API is the most extensive and useful API for general purprose information
about legislators and legislation, and provides primary keys to other API's
data sets like OpenSecrets.org.

You'll need to do nothing to start using GovTrack.us! Their API is free and
open for use for all. Check out the documentation at
https://www.govtrack.us/developers.

### OpenSecrets.org

This API is one that provides information about where legislators are receiving
funding from.

You'll need to obtain your own OpenSecrets.org API key before you can run
*politico* yourself. You can sign up at
https://www.opensecrets.org/resources/create/apis.php. When you're done, add a
config block like the following to your config file.

```python
[opensecrets]
  api_key = 'you-api-key'
  scheme = 'http'
  netloc = 'opensecrets.org'
  api_path = '/api'
```

### Twitter

This API is one that gives us access to public Twitter users' information, like
how active they are or how many statuses they've tweeted.

You'll need to obtain your own Twitter API key before you can run *politico
yourself. You can sign up at https://apps.twitter.com/. When you're done, add a
config block like the following to your config file.

```python
[twitter]
  consumer_key = 'your-consumer-key'
  consumer_secret = 'your-consumer-secret'
  scheme='https'
  netloc = 'api.twitter.com'
  api_path = '/'
```

## deployment

### virtualenv

Bootstrap your environment using virtualenv and pip:

```bash
mkdir ~/.virtualenvs
virtualenv ~/.virtualenvs/politico
source ~/.virtualenvs/bin/activate
```

### local

You can run *politico* yourself locally by running:

```bash
./manage.py runserver /path/to/config
```

Then in a web browser, access http://localhost:5000.

### heroku

You can run *politico* yourself locally with the heroku toolchain by running:

```bash
foreman run
```

Then in a web browser, access http://localhost:5000.

Stay tuned for instructions on deploying on a remote heroku instance!
