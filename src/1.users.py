#!/usr/bin/python

from flask import Flask, jsonify

users = {
	0:{"name":"John","car":"BMW"},
	1:{"name":"Mary","car":"Audi"},
	2:{"name":"Tom","car":"Mercedes"},
	3:{"name":"Susan","car":"VW"}
}

app = Flask(__name__)

@app.route("/user/<int:id>/<property>")
def query(id,property):
	if id in users:
		if property in users[id]: 
			app.logger.debug("User id " + str(id) + " found in db, property " + users[id][property] + ".")
			return jsonify({property:users[id][property]})
		else:
			app.logger.debug("User id " + str(id) + " found in db, property not found.")
			return jsonify({property:"property not found"})
	else:
		app.logger.debug("User id " + str(id) + " not found in db.")
		return jsonify({property:"user not found"})


if __name__ == "__main__":
	app.debug = True
	app.run(port=5000)

