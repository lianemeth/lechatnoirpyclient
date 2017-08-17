import unittest
import socket

import mock
from chatnoirclient import client

class TestChatNoirclient(unittest.TestCase):

    @mock.patch('socket.socket')
    def setUp(self, mock_socket):
        self.lechat = client.ChatNoirClient()
        mock_socket.assert_called_once_with(socket.AF_INET, socket.SOCK_STREAM)


    def test_connect(self):
        self.lechat.connect('localhost', 8080,
                       {'name': 'maria',
                        'info': 'you gotta see her'})
        self.assertEqual(self.lechat.name, 'maria')

    def test_send_public_msg(self):
        self.lechat.send_public_msg('hello!')
        self.lechat.sockz.send.assert_called()
