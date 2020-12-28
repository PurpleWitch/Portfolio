from flask import Flask, request, jsonify
import os
import db

# define app as flask
app = Flask(__name__)

# get response for landing page
@app.route('/db', methods=['GET'])
def Hello():
    return "Hello!"

# locate the directory of the app file
basedir = os.path.abspath(os.path.dirname(__file__))

# database status test route
@app.route("/test")
def test():
    db.db.collection.insert_one({"database": "online"})
    return "Connected to the database!"

# run the flask app
if __name__ == '__main__':
    app.run(port=8000, debug=True)
