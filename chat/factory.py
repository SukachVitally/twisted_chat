from autobahn.twisted.websocket import WebSocketServerFactory
from chat.protocol import ChatProtocol


class ChatFactory(WebSocketServerFactory):

    protocol = ChatProtocol
    connections = []

    def send_message(self, message):
        for connection in self.connections:
            connection.sendMessage('--| {0}\n'.format(message))

