from flask import Blueprint, jsonify, request

blueprint = Blueprint('routes', __name__)

tasks = []

@blueprint.route('/api/tasks', methods=['GET'])
def getTasks():
    return jsonify(tasks)

@blueprint.route('api/tasks', methods=['POST'])
def addTasks():
    data = request.get_json()
    tasks.append(data)
    return jsonify({'message': 'Tarefa adicionada!'}), 201