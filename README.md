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
sudo piglatin
```

###Run unit tests

```
python tests/test_piglatin.py
```

###Test POST request

```
http POST "0.0.0.0:80" < test.txt
```
