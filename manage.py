from autobahn.twisted.websocket import WebSocketServerProtocol
from autobahn.twisted.websocket import WebSocketServerFactory
from twisted.enterprise import adbapi
from twisted.python import util


class ChatProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        print 'connect'

    def onOpen(self):
        print("WebSocket connection open.")
        d = self.factory.dbpool.runQuery("select user")
        d.addCallback(lambda result: util.println('user', result))
        self.factory.connections.append(self)
        self.sendMessage('Now {0} in chat\n'.format(len(self.factory.connections)))

    def onMessage(self, payload, isBinary):
        message = 'binnary' if isBinary else payload.decode('utf8')

        for connection in self.factory.connections:
            connection.sendMessage('--| {0}\n'.format(message))

    def onClose(self, wasClean, code, reason):
        for connection in self.factory.connections:
            if connection is self:
                self.factory.connections.remove(connection)


class ChatFactory(WebSocketServerFactory):

    protocol = ChatProtocol
    connections = []


def main():
    import sys
    from twisted.python import log
    from twisted.internet import reactor

    log.startLogging(sys.stdout)
    factory = ChatFactory(u"ws://127.0.0.1:8000", debug=False)
    factory.dbpool = adbapi.ConnectionPool("psycopg2", dbname='twisted', host='10.0.2.2', user='sukach',
                                           password='204839')
    reactor.listenTCP(8000, factory)
    reactor.run()

if __name__ == '__main__':
    main()
