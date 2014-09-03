#!/usr/bin/python

from flask import Flask, jsonify

cars = {
	"BMW":{"model":"X5","year":"2009"},
	"Audi":{"model":"A4","year":"2013","mpg":37},
	"Mercedes":{"model":"S Class","mpg":"27","cyl":6},
	"VW":{"model":"Beattle","year":1978}
}

app = Flask(__name__)

@app.route("/car/<id>/<property>")
def query(id,property):
	if id in cars:
		if property in cars[id]: 
			app.logger.debug("Car id " + id + " found in db, property " + cars[id][property] + ".")
			return jsonify({property:cars[id][property]})
		else:
			app.logger.debug("Car id " + str(id) + " found in db, property not found.")
			return jsonify({property:"property not found"})
	else:
		app.logger.debug("Car id " + str(id) + " not found in db.")
		return jsonify({property:"car not found"})


if __name__ == "__main__":
	app.debug = True
	app.run(port=5002)

