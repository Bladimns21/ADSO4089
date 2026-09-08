from flask import Blueprint
from Controllers.matEvaController import matEvaController

mat_eva_bp = Blueprint('mat_eva_bp', __name__)

@mat_eva_bp.route('/', methods=['GET'])
def get_all():
    return matEvaController.get_all()

@mat_eva_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    return matEvaController.get_by_id(id)

@mat_eva_bp.route('/', methods=['POST'])
def add():
    return matEvaController.add()

@mat_eva_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    return matEvaController.update(id)

@mat_eva_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return matEvaController.delete(id)
