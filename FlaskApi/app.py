"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

#connexion doc
#https://pypi.org/project/connexion/
#swagger doc
#./api/ui
from flask import render_template
from flask import jsonify
import connexion

DEBUG = True
app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/secure")
def secure():
    return render_template("secure.html")

@app.route('/api/token')
def get_auth_token():
    json = jsonify({'token': '242424363424254242424'})
    return json


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(host=HOST, port=PORT, debug=DEBUG)