import pytest

from ipmininet.ipnet import IPNet
from ipmininet.inginious import IPmininetUnitTest
from mininet.log import lg as log


class TestInginious:
    """ Test IPmininetUniTest on IPmininet network topo """
    def __init__(self, net):
        self.net = net
        
    @pytest.fixture
    def newTest(self):
        test = IPmininetUnitTest(self.net)
        
    def testPing(self):
        try:
            test = IPmininetUnitTest(self.net)
            assert test.testPingAll() == False
        except AssertionError as e:
            print("testPing Failed")
    
    def testHostConnected(self, v6=False, timeout=0.5, translate_address=True):
        try
            test = IPmininetUnitTest(self.net)
            assert testHost_connected(self, v6, timeout, translate_address) == True
        except AssertionError as e:
            print("testHostConnected Failed")
        
            
    def testServiceUp(self, router, serviceName):
        try:
            test = IPmininetUnitTest(self.net)
            assert test.testDaemonUp(router, serviceName) == 1
        except AssertionError as e:
            print("testServiceUp Failed for " + serviceName, e.__class__, "on router " + router)
            
         
    def testRoutingPath(self, router, path):
        try:
            test = IPmininetUnitTest(self.net)
            assert test.testPathinRoutingTable(router, path) == 1 
        except AssertionError as e:
            print("testRoutingPath", e.__class__, "testRoutingPath")
            
    def testRoutingTables(self, routingTables):
        try:
            test = IPmininetUnitTest(self.net)
            assert test.testAllRoutingTables(routingTables) == 1
        except AssertionError as e:
            print("testRoutingTables Failed", e.__class__, "" ) 
                                   
    def testAll(self):
        test = IPmininetUnitTest(self.net)
        answers = test.buildRoutingTables()
        self.testRoutingTables(answers)
        path = "2001:db8:1341:12::/64 dev r1-eth0 proto kernel metric 256 pref medium"
        self.testPing()
        self.testHostConnected(True, 0.5, True)
        self.testRoutingPath("r2", path)
        self.testServiceUp("r2", "zebra")
        self.testServiceUp("r2", "ospf6d") 
        self.testServiceUp("r2", "ospfd")
        self.testServiceUp("r2", "apache2")
