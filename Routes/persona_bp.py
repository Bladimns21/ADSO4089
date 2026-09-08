from flask import Blueprint
from Controllers.personaController import personaController

persona_bp = Blueprint('persona_bp', __name__)

@persona_bp.route('/', methods=['GET'])
def get_all():
    return personaController.get_all()

@persona_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    return personaController.get_by_id(id)

@persona_bp.route('/', methods=['POST'])
def add():
    return personaController.add()

@persona_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    return personaController.update(id)

@persona_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return personaController.delete(id)
