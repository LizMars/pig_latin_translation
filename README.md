#Pig Latin Translation Microservice

###Tools used:
- python 2.7
- flask web framework
- httpie

###Installation:

```
pip install piglatin
```

###Run microservice:

```
sudo python run.py
```

###Run unit tests

```
python tests/test_piglatin.py
```

###Test POST request

```
http -a POST "127.0.0.1:80" body='test sentence'
```
