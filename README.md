# pig_latin_translation

Tools used:
- python 2.7
- pew
- flask
- httpie

Instructions for installing and running the microservice and test suite.


1. Install pew (details: https://github.com/berdario/pew):
`pip install pew`

2. Create a new environment, in $WORKON_HOME.

`usage: pew new [-hd] [-p PYTHON] [-i PACKAGES] [-a PROJECT] [-r REQUIREMENTS] envname`

`pew new piglatin`

3. Use created virtual environment

`usage: pew workon [environment_name]`

`pew workon piglatin`

4. Install tools:

- wed framework:
`pip install Flask`

- The Cross-Origin Resource Sharing (CORS) mechanism gives web servers
cross-domain access controls, which enable secure cross-domain data transfers.

`pip install -U flask-cors`

- Testing tool

`pip install httpie`

5. Run microservice:

`sudo python run.py`

6. Run test suite.
