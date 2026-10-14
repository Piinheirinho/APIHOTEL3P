from flask import Flask
from flask_restful import Resource,Api
from resources.hotel import Hoteis

app =Flask(__name__)
api = Api(app)

#Configuraçoes

#Rotas
api.add_resource(Hoteis,"/hoteis")

#iniciar a plicaçao
if __name__ == "__main__":
    app.run(debug=True  )