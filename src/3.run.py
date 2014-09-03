#!/usr/bin/python

import requests

# what is name and model of a car of user id 2

name = requests.get("http://localhost:5000/user/2/name")
print name.json()["name"]

car = requests.get("http://localhost:5000/user/2/car")

model = requests.get("http://localhost:5002/car/" + car.json()["car"] + "/model")
print model.json()["model"]
