import optparse
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.protocol import ServerFactory


def parse_args():
    usage = """
    python manage.py [hostname]:port
    """

    parser = optparse.OptionParser(usage)

    help = "The port to listen on. Default to a random available port."
    parser.add_option('--port', type='int', help=help)

    options, args = parser.parse_args()

    if len(args) != 1:
        parser.error('Provide exactly one server address.')

    def parse_address(addr):
        if ':' not in addr:
            host = '127.0.0.1'
            port = addr
        else:
            host, port = addr.split(':', 1)

        if not port.isdigit():
            parser.error('Ports must be integers.')

        return host, int(port)

    return options, parse_address(args[0])


class ChatProtocol(Protocol):

    def connectionMade(self):
        self.factory.connections.append(self)
        self.transport.write('Now {0} in chat\n'.format(len(self.factory.connections)))

    def connectionLost(self, reason):
        for connection in self.factory.connections:
            if connection is self:
                self.factory.connections.remove(connection)

    def dataReceived(self, data):
        for connection in self.factory.connections:
            connection.transport.write('--| {0}\n'.format(data))


class ChatFactory(ServerFactory):

    protocol = ChatProtocol
    connections = []


def main():
    options, server_addr = parse_args()
    print 'Start server', options, server_addr
    factory = ChatFactory()
    reactor.listenTCP(server_addr[1], factory)
    reactor.run()

if __name__ == '__main__':
    main()
