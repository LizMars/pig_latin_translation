Pig Latin Translation Microservice
==================================

Tools used
----------

- Python 2.7
- Flask web framework
- httpie client

Installation
------------

```
pip install piglatin
```
### Run production instance:

```
sudo gunicorn -w 4 -b 0.0.0.0:80 piglatin:app
```

Development
-----------

### Run development server
```
sudo piglatin
```

### Run unit tests

```
python tests/test_piglatin.py
```

### Test POST request

```
pip install httpie
http 127.0.0.1 < text.txt
```
