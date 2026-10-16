from flask_restful import Resource, reqparse

lista_hoteis =[
    {"hotel_id": "sky","nome":"Hotel","estrelas": 4.8 ,"diaria":195.99, "cidade":"porto"},
    {"hotel_id": "sky1","nome":"Hotel1","estrelas": 4.8 ,"diaria":195.99, "cidade":"porto"},
    {"hotel_id": "sky2","nome":"Hotel2","estrelas": 4.8 ,"diaria":195.99, "cidade":"porto"}
    ]

class Hoteis(Resource):


    def get(self):
        return{"hoteis": lista_hoteis}

class Hoteis(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome", type=str, required=True, help="Nome do hotel é obrigatório")
    argumentos.add_argument("estrelas", type=float, required=True, help="Estrelas do hotel é obrigatório")
    argumentos.add_argument("diaria", type=float, required=True, help="Diária do hotel é obrigatória")
    argumentos.add_argument("cidade", type=str, required=True, help="Cidade do hotel é obrigatória")

    def get(self, id_hotel):
        for hotel in lista_hoteis:
            if hotel["hotel_id"] == id_hotel:
                return hotel, 200
        return{"message": "Hotel not found"}, 404

    def post(self, id_hotel):
        dados = Hoteis.argumentos.parse_args()
        for hotel in lista_hoteis:
            if hotel["hotel_id"] == id_hotel:
                return{"message": "Hotel id '{}' already exists.".format(id_hotel)}, 400

        novo_hotel = {"hotel_id": id_hotel, **dados}
        lista_hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, id_hotel):
        dados = Hoteis.argumentos.parse_args()
        for hotel in lista_hoteis:
            if hotel["hotel_id"] == id_hotel:
                hotel.update(dados)
                return hotel, 200
        return{"message": "Hotel not found"}, 404

    def delete(self, id_hotel):
        global lista_hoteis
        lista_hoteis = [hotel for hotel in lista_hoteis if hotel["hotel_id"] != id_hotel]
        return{"message": "Hotel deleted"}, 200
