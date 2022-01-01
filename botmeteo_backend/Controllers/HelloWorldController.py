
from flask_restful import Resource

from BLL.HelloWorldBLL import HelloWorldBLL

#Les Controller sert uniquement à faire la passerelle entre le frontend et ma BLL
# Il récupère la saisit du user, le donne à la BLL et renvoit au user la réponse de la BLL
# Méthode SOC en informatique, 1 fichier, 1 classe, 1 tâche 
class HelloWorldController(Resource):
    def get(self):
        helloWorldBll = HelloWorldBLL()
        result = helloWorldBll.get('Cazou')
        return {'hello': result}