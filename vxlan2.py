from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info


def emptyNet():
    info('*** Adding Controller\n')
    net = Mininet()
    info('*** Adding Host\n')
    red2 = net.addHost('red2', ip='10.0.10.20', mac='00:00:00:00:00:02')
    blue2 = net.addHost('blue2', ip='10.0.10.20', mac='00:00:00:00:00:02')
    info('*** Adding Switch\n')
    s2 = net.addSwitch('s2')
    info('*** Creating Link\n')
    net.addLink(red2, s2)
    net.addLink(blue2, s2)
    info('*** Starting Network\n')
    net.start()
    info('*** Running CLI\n')
    CLI(net)
    info('*** Stopping Network\n')
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    emptyNet()
