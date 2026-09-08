from flask import Blueprint
from Controllers.instructorController import instructorController

instructor_bp = Blueprint('instructor_bp', __name__)

@instructor_bp.route('/', methods=['GET'])
def get_all():
    return instructorController.get_all()

@instructor_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    return instructorController.get_by_id(id)

@instructor_bp.route('/', methods=['POST'])
def add():
    return instructorController.add()

@instructor_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    return instructorController.update(id)

@instructor_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return instructorController.delete(id)