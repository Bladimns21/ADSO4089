from flask import Blueprint
from Controllers.matriculaController import matriculaController

matricula_bp = Blueprint('matricula_bp', __name__)

@matricula_bp.route('/', methods=['GET'])
def get_all():
    return matriculaController.get_all()

@matricula_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    return matriculaController.get_by_id(id)

@matricula_bp.route('/', methods=['POST'])
def add():
    return matriculaController.add()

@matricula_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    return matriculaController.update(id)

@matricula_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return matriculaController.delete(id)
