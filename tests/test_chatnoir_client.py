import unittest
import socket

from unittest import mock
import time
from chatnoirclient import client

class TestChatNoirclient(unittest.TestCase):

    @mock.patch('socket.socket')
    def test_connect(self, mock_socket):
        lechat = client.ChatNoirClient()
        lechat.connect('localhost', 8080,
                       {'name': 'maria',
                        'info': 'you gotta see her'})
        mock_socket.assert_called_once_with(socket.AF_INET, socket.SOCK_STREAM)
        self.assertEqual(lechat.name, 'maria')

    @mock.patch('socket.socket')
    @mock.patch.object(client.ChatNoirConnection, '_send_message')
    def test_send_public_msg(self, mock_send_msg, mock_socket):
        lechat = client.ChatNoirClient()
        with self.assertRaises(client.NotConnectedException):
            lechat.send_public_msg('hello!')
        lechat.connect('localhost', 8080,
                       {'name': 'maria',
                        'info': 'you gotta see her'})
        lechat.send_public_msg('hello!')
        self.assertTrue(mock_send_msg.called)
        mock_send_msg.assert_called_with('NEW;maria;you gotta see her')
        self.assertTrue(mock_socket.called)
