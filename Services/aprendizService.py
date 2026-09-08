from flask import current_app, jsonify
from Models.Aprendiz import Aprendiz

class aprendizService:
    @staticmethod
    def get_all():
        sql = "SELECT * FROM T_APRENDIZ"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return jsonify(data)

    @staticmethod
    def get_by_id(id):
        sql = "SELECT * FROM T_APRENDIZ WHERE APR_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        return jsonify(data) if data else (jsonify({"error": "Aprendiz no encontrado"}), 404)

    @staticmethod
    def add(data):
        sql = """INSERT INTO T_APRENDIZ (APR_UUID, APR_FECHA_NAC, APR_PER_ID) 
                 VALUES (%s, %s, %s)"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get('APR_UUID'),
            data.get('APR_FECHA_NAC'),
            data.get('APR_PER_ID')
        ))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Aprendiz agregado correctamente"}), 201

    @staticmethod
    def update(id, data):
        sql = """UPDATE T_APRENDIZ SET APR_FECHA_NAC=%s, APR_PER_ID=%s 
                 WHERE APR_ID=%s"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get('APR_FECHA_NAC'),
            data.get('APR_PER_ID'),
            id
        ))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Aprendiz actualizado correctamente"})

    @staticmethod
    def delete(id):
        sql = "DELETE FROM T_APRENDIZ WHERE APR_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Aprendiz eliminado correctamente"})
