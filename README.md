# politico

A visual tool for finding, following and contacting legislators powered by
OpenSecrets.org.

# developers

## configuration

You'll need to obtain your own OpenSecrets.org API key before you can run
politico yourself. You can sign up at
https://www.opensecrets.org/resources/create/apis.php. It only takes a few
minutes. When you're done, create a configuration file that you can pass to
Flask-Script that looks like:

```python
[opensecrets]
  api_key = 'you-api-key'
  scheme = 'http'
  netloc = 'opensecrets.org'
  api_path = '/api'
```
