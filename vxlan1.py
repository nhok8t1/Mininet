from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import Link, TCLink


def emptyNet():
    info('*** Adding Controller\n')
    net = Mininet(controller=RemoteController, link=TCLink, switch=OVSKernelSwitch)
    info('*** Adding Host\n')
    red1 = net.addHost('red1', ip='10.0.10.10', mac='00:00:00:00:00:01')
    blue1 = net.addHost('blue1', ip='10.0.10.10', mac='00:00:00:00:00:01')
    info('*** Adding Switch\n')
    s111 = net.addSwitch('s111')
    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)
    info('*** Creating Link\n')
    net.addLink(red1, s111)
    net.addLink(blue1, s111)
    info('*** Starting Network\n')
    net.build()
    c0.start()
    s111.start([c0])
    info('*** Running CLI\n')
    CLI(net)
    info('*** Stopping Network\n')
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    emptyNet()
