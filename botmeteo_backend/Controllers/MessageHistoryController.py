from flask_restful import reqparse, abort, Resource
from BLL.MessageHistoryBLL import MessageHistoryBLL

parser = reqparse.RequestParser()
parser.add_argument('message')
parser.add_argument('user')

class MessageHistoryController(Resource):
    def get(self):
        return ''
        # return MESSAGE_HISTORY