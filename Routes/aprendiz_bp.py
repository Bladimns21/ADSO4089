# blueprint  
from flask import Blueprint
from Controllers.aprendizController import aprendizController

apr_bp = Blueprint('apr_bp', __name__)

@apr_bp.route('/', methods=['GET'])
def get_all():
    return aprendizController.get_all()

@apr_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    return aprendizController.get_by_id(id)

@apr_bp.route('/', methods=['POST'])
def add():
    return aprendizController.add()

@apr_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    return aprendizController.update(id)

@apr_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return aprendizController.delete(id)