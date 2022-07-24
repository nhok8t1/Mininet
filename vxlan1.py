from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info


def emptyNet():
    info('*** Adding Controller\n')
    net = Mininet()
    info('*** Adding Host\n')
    red1 = net.addHost('red1', ip='10.0.10.10', mac='00:00:00:00:00:01')
    blue1 = net.addHost('blue1', ip='10.0.10.10', mac='00:00:00:00:00:01')
    info('*** Adding Switch\n')
    s1 = net.addSwitch('s1')
    info('*** Creating Link\n')
    net.addLink(red1, s1)
    net.addLink(blue1, s1)
    info('*** Starting Network\n')
    net.start()
    info('*** Running CLI\n')
    CLI(net)
    info('*** Stopping Network\n')
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    emptyNet()
