import pytest

from ipmininet.inginious import IPmininetUnitTest
from mininet.log import lg as log

class TestInginious:
    """ Test IPmininetUniTest on IPmininet network topo """
    def __init__(self, routers, hosts):
        self.routers = routers
        self.hosts   = hosts
        
    @pytest.fixture
    def newTest(self):
        test = IPmininetUnitTest(self.routers, self.hosts)
        
    def testPing(self):
        try:
            test = IPmininetUnitTest(self.routers, self.hosts)
            assert test.testPingAll() == 1
        except AssertionError as e:
            print("testPing", e.__class__, "ping.")
            
    def testServiceUp(self, router, serviceName):
        try:
            test = IPmininetUnitTest(self.routers, self.hosts)
            assert test.testDaemonUp(router, serviceName) == 1
        except AssertionError as e:
            print("testServiceUp Failed for " + serviceName, e.__class__, "on router " + router)
            
         
    def testRoutingPath(self, router, path):
        try:
            test = IPmininetUnitTest(self.routers, self.hosts)
            assert test.testPathinRoutingTable(router, path) == 1 
        except AssertionError as e:
            print("testRoutingPath", e.__class__, "testRoutingPath")
            
    def testRoutingTables(self, routingTables):
        try:
            test = IPmininetUnitTest(self.routers, self.hosts)
            assert test.testAllRoutingTables(routingTables) == 1
        except AssertionError as e:
            print("testRoutingTables Failed", e.__class__, "" ) 
                                   
    def testAll(self):
        test = IPmininetUnitTest(self.routers, self.hosts)
        answers = test.buildRoutingTables()
        self.testRoutingTables(answers)
        path = "2001:db8:1341:12::/64 dev r1-eth0 proto kernel metric 256 pref medium"
        self.testPing()
        self.testRoutingPath("r2", path)
        self.testServiceUp("r2", "zebra")
        self.testServiceUp("r2", "ospf6d") 
        self.testServiceUp("r2", "ospfd")
        self.testServiceUp("r2", "apache2")
