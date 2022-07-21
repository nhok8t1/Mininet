from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import Link, TCLink


def emptyNet():
    net = Mininet()
    info('*** Adding Controller\n')
    info('*** Adding Host\n')
    red2 = net.addHost('red2', ip='10.0.10.20', mac='00:00:00:00:00:02')
    blue2 = net.addHost('blue2', ip='10.0.10.20', mac='00:00:00:00:00:02')
    info('*** Adding Switch\n')
    s22 = net.addSwitch('s22')
    info('*** Creating Link\n')
    net.addLink(red2, s22)
    net.addLink(blue2, s22)
    info('*** Starting Network\n')
    net.start()
    info('*** Running CLI\n')
    CLI(net)
    info('*** Stopping Network\n')
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    emptyNet()
