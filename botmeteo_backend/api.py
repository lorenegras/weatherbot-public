from flask import Flask
from flask_restful import  Api
from flask_cors import CORS

from Controllers.HelloWorldController import HelloWorldController
from Controllers.MessageController import MessageController
from Controllers.MessageHistoryController import MessageHistoryController

app = Flask(__name__)
api = Api(app)

cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

api.add_resource(HelloWorldController,'/')
api.add_resource(MessageHistoryController, '/messagehistory')
api.add_resource(MessageController, '/messages', '/messages/<message_id>')

if __name__ == '__main__':
    app.run(debug=True)