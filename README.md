# StealthNinja
The stealthiest browser module for python, without browser drivers (under development)

# Updates
1.0.0 - Beginning, literally just 46 lines of code. Contributions appreciated :)

# Documentation
To make a client instance, start with this - <br />
```py
from stealthninja import cli
client = cli()

```
<br />

GET request to server, returns a request response from the website url. <br />
```py
response = client.get('https://example.com')
print(response.text)
# <html><head></head...
```
<br />
POST request to server, sends a post request and returns a request response from the website url. <br />

```py
response = client.get('https://example.com')
print(response.text)
```

# End

I'll appreciate any contributions on this project
