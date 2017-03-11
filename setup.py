from setuptools import setup, find_packages

setup(
    name="piglatin",
    discription="Translate from English to Pig Latin",
    install_requires=['Flask', 'flask-cors'],
    packages=find_packages(exclude=['tests*'])
    )
