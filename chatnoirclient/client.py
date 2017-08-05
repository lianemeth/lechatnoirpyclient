import socket
import json


class ChatNoirClient(object):

    def __init__(self,  encoding='utf-8'):
        self.encoding = encoding
        self.sockz =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self, address, port, user_form):
        self.sockz.connect((address, port))
        self.name = user_form['name']
        new_client_dict = {'TYPE' : 'NEWCLIENT',
                           'NAME' : user_form['name'],
                           'INFO' : user_form['info']}
        new_client_message = json.dumps(new_client_dict)
        self.sockz.send(bytearray(new_client_message, encoding=self.encoding))
            
    def send_public_msg(self, message):
        public_message_dict = {'TYPE' : 'PUBLIC',
                               'FROM' : self.name,
                               'Message' : message}
        public_message = json.dumps(public_message_dict)
        self.sockz.send(bytearray(public_message, encoding=self.encoding))
