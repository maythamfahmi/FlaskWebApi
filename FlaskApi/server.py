"""
Main module of the server file
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

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(host=HOST, port=PORT, debug=DEBUG)