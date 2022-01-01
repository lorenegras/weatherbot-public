
class HelloWorldBLL():
    def get(firstName):
        result = 'world'
        # Traitement code métier
        if(firstName != ''):
            result = firstName
        return {'hello': result}