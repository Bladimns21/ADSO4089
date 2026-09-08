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