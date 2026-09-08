from Services.instructorService import instructorService

class instructorController:

    def get_all():
        data = instructorService.get_all()
        return data

    def get_by_id(id):
        data = instructorService.get_by_id(id)
        return data

    def add():
        data = instructorService.add()
        return data

    def update(id):
        data = instructorService.update(id)
        return data

    def delete(id):
        data = instructorService.delete(id)
        return data