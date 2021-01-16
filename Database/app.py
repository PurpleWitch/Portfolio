from flask import Flask, request, jsonify
from bson import json_util, ObjectId
from flask_cors import CORS
import json
import os
import db

# define app as flask
app = Flask(__name__)

# enables CORS
cors = CORS(app)

# get views from database
@app.route('/', methods=['GET'])
def Views():
    views=db.db.collection.find_one({"views":"views"})
    db.db.collection.update_one({"views": "views"},{'$set':{"count": views['count']+1}})
    return json.loads(json_util.dumps(views))

# locate the directory of the app file
basedir = os.path.abspath(os.path.dirname(__file__))

# run the flask app
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8000")
