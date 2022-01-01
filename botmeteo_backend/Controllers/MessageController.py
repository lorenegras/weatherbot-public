from flask_restful import reqparse, abort, Resource
from BLL.MessageBLL import MessagedBLL, abort_if_message_doesnt_exist

parser = reqparse.RequestParser()
parser.add_argument('message')
parser.add_argument('user')

class MessageController(Resource):
    def get(self, message_id=None):
        # GetById
        if message_id:
            if(abort_if_message_doesnt_exist(message_id)): 
                abort(404, message="Message {} doesn't exist".format(message_id))
            return MessagedBLL().getById(message_id)
        # GetAll
        else: 
            return MessagedBLL().getAll()
    
    def post(self): 
        args = parser.parse_args()
        messageBll = MessagedBLL()
        message = messageBll.post(args)
        return message, 201

    def put(self, message_id):
        args = parser.parse_args()
        messageBll = MessagedBLL()
        update_message = messageBll.put(message_id, args)
        return update_message, 201

    def delete(self, message_id):
        if(abort_if_message_doesnt_exist(message_id)): 
            abort(404, message="Message {} doesn't exist".format(message_id))
        messageBll = MessagedBLL()
        messageBll.delete(message_id)
        return '', 204
    