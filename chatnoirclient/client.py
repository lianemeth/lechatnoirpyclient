import socket


def new_client(name, info):
    return "NEW;{name};{info}".format(name=name, info=info)


def new_public_message(message):
    return "PUB;;{message}".format(message=message)


class ChatNoirClient(object):

    def __init__(self, encoding='utf-8'):
        self.encoding = encoding
        self.sockz = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, address, port, user_form):
        self.sockz.connect((address, port))
        self.name = user_form['name']
        new_client_msg = new_client(user_form['name'], user_form['info'])
        self.sockz.send(bytearray(new_client_msg, encoding=self.encoding))

    def send_public_msg(self, message):
        public_message = new_public_message(message)
        self.sockz.send(bytearray(public_message, encoding=self.encoding))
