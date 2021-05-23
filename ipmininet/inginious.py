class IPmininetUnitTest:
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
                            r = hosti.cmd(cmd)
                            if "100% packet loss" in r:
                                return 0 
                        ip6 = hostj.intf(intf).ip6
                        if ip6 != None:
                            cmd = "ping -6 -c 1 "+ ip6
                            r = hosti.cmd(cmd)
                            if "100% packet loss" in r:
                                return 0 
        return 1
                        
    
    def testRoutingTable(self, router, answer):
        cmd = "ip route"
        cmd6 = "ip -6 route"
        r  = router.cmd(cmd)
        r6 = router.cmd(cmd6)
        if r == answer or r6 == answer:
            return 1
        return 0    
        
    def buildRoutingTables(self):
        cmd = "ip -6 route"
        answers = []
        for router in self.routers:
            answers.append(router.cmd(cmd))
        return answers
        
    def testAllRoutingTables(self, answers=[]):
        for router, answer in zip(self.routers, answers):
            if self.testRoutingTable(router, answer) == 0:
                return 0
        return 1  
              
    def test_IPscfg(self, anwserIPs=[]):
        hostIPs = []
        for host in self.hosts:
            for intf in host.intfNames():
                hostIPs.append(host.IP(intf))
        assert(hostIPs == anwserIPs)
    
    def testHostCmd(host, hcmd, anwser):
        r = host.cmd(hcmd)
        assert(r  == anwser)
        
    def testPathinRoutingTable(self, routerName, path):
        for router in self.routers:
            if router.name == routerName:
                cmd  = "ip route"
                cmd6 = "ip -6 route"
                r  = router.cmd(cmd)
                r6 = router.cmd(cmd6)
                if path in r or path in r6:
                    return 1
        return 0
        
    def testDaemonUp(self, routerName, daemonName):
        for router in self.routers:
            if router.name == routerName:
                cmd  = "netstat -anp"
                r  = router.cmd(cmd)
                if daemonName in r:
                    return 1
        return 0            
