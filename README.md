# politico

A visual tool for finding, following and contacting legislators powered by
OpenSecrets.org.

# developers

## configuration

You'll need to obtain your own application keys for the API that we use in
politico.

### OpenSecrets.org

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
