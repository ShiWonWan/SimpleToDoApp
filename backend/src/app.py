from datetime import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
import json, uuid


app = Flask(__name__)
CORS(app)


# TEST END POINT
@app.route('/')
def index():
    return json.loads('{"message": "Working OK"}')

# NEW TASK
@app.route('/tasks', methods=['POST'])
def createTask():

    # INSERT INTO .JSON FILE
    file = open('db.json', 'r+', encoding="utf-8")
    oldJson = json.loads(file.read())
    idUnique = uuid.uuid4()
    oldJson.append({
        "id" : str(idUnique),
        "task" : request.json['task'],
        "date" : str(datetime.today()),
        "state" : 0
    })
    file.truncate(0)
    file.close()
    file = open('db.json', 'r+')
    file.write(json.dumps(oldJson))
    file.close()

    return json.loads('{"message" : "Task posted Ok!", "id" : "'+str(idUnique)+'"}')

# GET ALL TASKS
@app.route('/tasks', methods=['GET'])
def getTasks():
    file = open('db.json', 'r')
    jsonString = file.read()
    file.close()
    return jsonString

# COMPLETE TASK
@app.route('/tasks/checked/<id>', methods=['PUT'])
def completeActivity(id):
    file = open('db.json', 'r+', encoding="utf-8")
    oldJson = json.loads(file.read())
    for doc in oldJson:
        if doc["id"] == id:
            doc["state"] = 1
    file.truncate(0)
    file.close()
    file = open('db.json', 'r+', encoding="utf-8")
    file.write(json.dumps(oldJson))
    file.close()
    return json.loads('{"checked" : "done"}')


if __name__ == '__main__':
    app.run(debug=True)
    