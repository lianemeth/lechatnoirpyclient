import socket
import threading

class NotConnectedException(Exception):
    pass

def new_client(name, info):
    return "NEW;{name};{info}".format(name=name, info=info)

def new_public_message(message):
    return "PUB;;{message}".format(message=message)


MESSAGE_QUEUE = []

class ChatNoirConnection(threading.Thread):

    def __init__(self, address, port, output, encoding='utf-8', max_length=512):
        super().__init__()
        self.encoding = encoding
        self.max_length = max_length
        self.output = output
        self.CONNECTED = True
        self.message_queue = []

        self.sockz = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockz.connect((address, port))
        self.sockz.setblocking(0)

        self.daemon = True

    def _send_message(self, message):
        self.sockz.send(bytearray(message, encoding=self.encoding))
    
    def run(self):
        if len(MESSAGE_QUEUE) > 0:
            self._send_message(MESSAGE_QUEUE.pop())
        try:
            data = self.sockz.recv(self.max_length)
        except socket.error as e: 
            if "Resource temporarily unavailable" not in repr(e):
                self.output(e)
        else:
            self.output(data)


class ChatNoirClient(object):

    def __init__(self, output=None, encoding='utf-8'):
        self.encoding = encoding
        self.output = output or print
        self.conn = None

    def connect(self, address, port, user_form):
        self.name = user_form['name']
        self.conn = ChatNoirConnection(address, port, self.output, self.encoding)
        self.conn.start()
        new_client_msg = new_client(user_form['name'], user_form['info'])
        self.queue_message(new_client_msg)

    def send_public_msg(self, message):
        if not self.conn:
            raise NotConnectedException
        public_message = new_public_message(message)
        self.queue_message(public_message)

    def queue_message(self, message):
        MESSAGE_QUEUE.insert(0, message)
