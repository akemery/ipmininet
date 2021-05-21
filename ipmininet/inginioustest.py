import unittest

class IPmininetUnitTest(unittest.TestCase):
    """ IPmininetUniTest on IPmininet network topo """
    def __init__(self, net):
        self.net = net
                
    def testPingAll(self):
        r = self.net.pingAll(10)
        assert(r == 0)
        
    def test_IPscfg(self, anwserIPs=[]):
        hostIPs = []
        for host in net.hosts:
            for intf in host.intfNames():
                hostIPs.append(host.IP(intf))
        assert(hostIPs == anwserIPs)
    
    def testHostCmd(host, hcmd, anwser):
        r = host.cmd(hcmd)
        assert(r  == anwser)
