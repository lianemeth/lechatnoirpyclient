from __future__ import print_function
import socket
import threading

def new_client(name, info):
    return "NEW;{name};{info}".format(name=name, info=info)

def new_public_message(message):
    return "PUB;;{message}".format(message=message)


class ChatNoirConnection(object):

    def __init__(self, address, port, output, encoding='utf-8', max_length=512):
        self.encoding = encoding
        self.max_length = max_length
        self.output = output
        self.CONNECTED = True
        self.message_queue = []

        self.sockz = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockz.connect((address, port))
        self.sockz.setblocking(0)
        self.thread = threading.Thread(target=self.loop)
        self.thread.start()

    def disconnect(self):
        self.CONNECTED = False

    def _send_message(self, message):
        self.sockz.send(bytearray(message, encoding=self.encoding))
    
    def send_message(self, message):
        self.message_queue.insert(0, message)

    def loop(self):
        while self.CONNECTED:
            if len(self.message_queue) > 0:
                self._send_message(self.message_queue.pop())
            try:
                data = self.sockz.recv(self.max_length)
            except socket.error:
                pass
            else:
                self.output(data)
        self.sockz.close()

class ChatNoirClient(object):

    def __init__(self, output=None, encoding='utf-8'):
        self.encoding = encoding
        self.output = output or print_function

    def connect(self, address, port, user_form):
        self.name = user_form['name']
        self.conn = ChatNoirConnection(address, port, self.output, self.encoding)
        new_client_msg = new_client(user_form['name'], user_form['info'])
        self.conn.send_message(new_client_msg)

    def send_public_msg(self, message):
        public_message = new_public_message(message)
        self.conn.send_message(public_message)
