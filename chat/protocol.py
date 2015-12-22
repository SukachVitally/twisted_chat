from autobahn.twisted.websocket import WebSocketServerProtocol
from twisted.internet import defer
from chat.db import dbpool


class ChatProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        print 'connect'

    def onOpen(self):
        self.factory.connections.append(self)
        d1 = dbpool.runQuery("select * from messages")
        d2 = defer.Deferred()
        d2.addCallback(lambda number: self.sendMessage('Now {0} in chat\n'.format(number)))
        d2.callback(len(self.factory.connections))
        d = defer.DeferredList([d1, d2])
        d.addCallback(self.send_history)

    def onMessage(self, payload, isBinary):
        message = 'binnary' if isBinary else payload.decode('utf8')
        dbpool.runOperation("insert into messages(text) values('{0}')".format(message))
        d2 = defer.Deferred()
        d2.addCallback(self.factory.sendMessage)
        d2.callback(message)

    def onClose(self, wasClean, code, reason):
        for connection in self.factory.connections:
            if connection is self:
                self.factory.connections.remove(connection)

    def send_history(self, result):
        for row in result[0][1]:
            self.sendMessage('from history: {0}\n'.format(row[1]))
