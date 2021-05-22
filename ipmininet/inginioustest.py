import unittest

class IPmininetUnitTest(unittest.TestCase):
    """ IPmininetUniTest on IPmininet network topo """
    def __init__(self, routers, hosts):
        self.routers = routers
        self.hosts   = hosts
                
    def testPingAll(self):
        for hosti in self.hosts:
            for hostj in self.hosts:
                if(hosti != hostj):
                    for intf in hostj.intfNames():
                        print(intf)
                        ip = hostj.IP(intf)
                        if ip != None:
                            cmd = "ping  -c 1 "+ ip
                            print(hosti.cmd(cmd))
                        ip6 = hostj.intf(intf).ip6
                        if ip6 != None:
                            cmd = "ping -6 -c 1 "+ ip6
                            print(hosti.cmd(cmd))
                        
    
    def testRoutingTable(self, router, answer):
        cmd = "ip -6 route"
        r = router.cmd(cmd)
        print(r)
        assert( r == answer)
        
    def buildRoutingTables(self):
        cmd = "ip -6 route"
        answers = []
        for router in self.routers:
            answers.append(router.cmd(cmd))
        return answers
        
    def testAllRoutingTables(self, answers=[]):
        for router, answer in zip(self.routers, answers):
            self.testRoutingTable(router, answer)  
              
    def test_IPscfg(self, anwserIPs=[]):
        hostIPs = []
        for host in self.hosts:
            for intf in host.intfNames():
                hostIPs.append(host.IP(intf))
        assert(hostIPs == anwserIPs)
    
    def testHostCmd(host, hcmd, anwser):
        r = host.cmd(hcmd)
        assert(r  == anwser)
