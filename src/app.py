from datetime import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)


# TEST END POINT
@app.route('/')
def index():
    return json.loads('{"message": "Working OK"}')

# NEW TASK
@app.route('/tasks', methods=['POST'])
def createTask():

    # INSERT INTO .TXT FILE WITH THE ID NAME
    file = open('db.json', 'r+')
    oldJson = file.read()
    jsonString = (",\n"'{"task": "'+request.json['task']+'", "date": "'+str(datetime.today())+'", "state": 0}')
    file.write(jsonString)
    file.close()

    return json.loads('{"message" : "Task posted Ok!"}')

# GET ALL TASKS
@app.route('/tasks', methods=['GET'])
def getTasks():
    file = open('db.json', 'r')
    jsonString = "[\n"+str(file.read())+"\n]"
    file.close()
    return jsonString

if __name__ == '__main__':
    app.run(debug=True)
    