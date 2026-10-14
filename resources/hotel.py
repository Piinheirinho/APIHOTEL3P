from flask_restful import Resource

lista_hoteis =[
    {"hotal_id": "sky","nome":"Hotel","estrelas": 4.8 ,"diaria":195.99, "cidade":"porto"},
    {"hotal_id": "sky1","nome":"Hotel1","estrelas": 4.8 ,"diaria":195.99, "cidade":"porto"},
    {"hotal_id": "sky2","nome":"Hotel2","estrelas": 4.8 ,"diaria":195.99, "cidade":"porto"}
    ]

class Hoteis(Resource):
    def get(self):
        return{"hoteis": lista_hoteis}