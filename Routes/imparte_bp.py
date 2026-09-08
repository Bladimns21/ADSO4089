from flask import Blueprint
from Controllers.imparteController import imparteController

imparte_bp = Blueprint('imparte_bp', __name__)

@imparte_bp.route('/', methods=['GET'])
def get_all():
    return imparteController.get_all()

@imparte_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    return imparteController.get_by_id(id)

@imparte_bp.route('/', methods=['POST'])
def add():
    return imparteController.add()

@imparte_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    return imparteController.update(id)

@imparte_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return imparteController.delete(id)
