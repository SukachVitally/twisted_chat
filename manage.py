import sys

from twisted.python import log
from twisted.internet import reactor
from chat.factory import ChatFactory


def main():
    log.startLogging(sys.stdout)
    factory = ChatFactory(u"ws://127.0.0.1:8000", debug=False)
    reactor.listenTCP(8000, factory)
    reactor.run()

if __name__ == '__main__':
    main()
