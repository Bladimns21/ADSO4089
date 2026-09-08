from flask import Blueprint
from Controllers.cursoController import cursoController

curso_bp = Blueprint('curso_bp', __name__)

@curso_bp.route('/', methods=['GET'])
def get_all():
    return cursoController.get_all()

@curso_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    return cursoController.get_by_id(id)

@curso_bp.route('/', methods=['POST'])
def add():
    return cursoController.add()

@curso_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    return cursoController.update(id)

@curso_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return cursoController.delete(id)
