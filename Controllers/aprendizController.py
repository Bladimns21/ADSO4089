<<<<<<< HEAD
from flask import request
from Services.aprendizService import aprendizService

class aprendizController:

    @staticmethod
    def get_all():
        return aprendizService.get_all()

    @staticmethod
    def get_by_id(id):
        return aprendizService.get_by_id(id)

    @staticmethod
    def add():
        data = request.get_json() or {}
        return aprendizService.add(data)
=======
from flask import request
from Services.aprendizService import aprendizService

class aprendizController:

    @staticmethod
    def get_all():
        return aprendizService.get_all()

    @staticmethod
    def get_by_id(id):
        return aprendizService.get_by_id(id)

    @staticmethod
    def add():
        data = request.get_json() or {}
        return aprendizService.add(data)

    @staticmethod
    def update(id):
        data = request.get_json() or {}
        return aprendizService.update(id, data)

    @staticmethod
    def delete(id):
        return aprendizService.delete(id)
>>>>>>> 1ec947b02867a883f1941a1d1892d20cd71fe47b
