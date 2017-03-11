Pig Latin Translation Microservice
==================================

Tools used
----------

- python 2.7
- flask web framework
- httpie

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
curl -X POST -H "Content-Type:plain/text" -d "@test.txt" http://127.0.0.1
```
