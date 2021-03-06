# Copyright 2008 (C) Nicira, Inc.
# 
# This file is part of NOX.
# 
# NOX is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# NOX is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with NOX.  If not, see <http://www.gnu.org/licenses/>.
import array
from nox.lib.packet.ethernet import *
from nox.apps.tests import unittest

pyunit = __import__('unittest')

lldp_str = \
"""\
\x01\x80\xc2\x00\x00\x0e\x00\x01\x30\xf9\xad\xa0\x88\xcc\x02\x07\
\x04\x00\x01\x30\xf9\xad\xa0\x04\x04\x05\x31\x2f\x31\x06\x02\x00\
\x78\x08\x17\x53\x75\x6d\x6d\x69\x74\x33\x30\x30\x2d\x34\x38\x2d\
\x50\x6f\x72\x74\x20\x31\x30\x30\x31\x00\x0a\x0d\x53\x75\x6d\x6d\
\x69\x74\x33\x30\x30\x2d\x34\x38\x00\x0c\x4c\x53\x75\x6d\x6d\x69\
\x74\x33\x30\x30\x2d\x34\x38\x20\x2d\x20\x56\x65\x72\x73\x69\x6f\
\x6e\x20\x37\x2e\x34\x65\x2e\x31\x20\x28\x42\x75\x69\x6c\x64\x20\
\x35\x29\x20\x62\x79\x20\x52\x65\x6c\x65\x61\x73\x65\x5f\x4d\x61\
\x73\x74\x65\x72\x20\x30\x35\x2f\x32\x37\x2f\x30\x35\x20\x30\x34\
\x3a\x35\x33\x3a\x31\x31\x00\x0e\x04\x00\x14\x00\x14\x10\x0e\x07\
\x06\x00\x01\x30\xf9\xad\xa0\x02\x00\x00\x03\xe9\x00\xfe\x07\x00\
\x12\x0f\x02\x07\x01\x00\xfe\x09\x00\x12\x0f\x01\x03\x6c\x00\x00\
\x10\xfe\x09\x00\x12\x0f\x03\x01\x00\x00\x00\x00\xfe\x06\x00\x12\
\x0f\x04\x05\xf2\xfe\x06\x00\x80\xc2\x01\x01\xe8\xfe\x07\x00\x80\
\xc2\x02\x01\x00\x00\xfe\x17\x00\x80\xc2\x03\x01\xe8\x10\x76\x32\
\x2d\x30\x34\x38\x38\x2d\x30\x33\x2d\x30\x35\x30\x35\x00\xfe\x05\
\x00\x80\xc2\x04\x00\x00\x00\
"""


lldp_str_2 = \
"""\
\x01\x80\xc2\x00\x00\x0e\x00\x1f\x28\x20\x58\xff\x88\xcc\x02\x07\
\x04\x00\x1f\x28\x20\x48\x00\x04\x02\x07\x31\x06\x02\x00\x78\x08\
\x02\x41\x31\x0a\x0c\x67\x61\x74\x65\x73\x2d\x73\x77\x2d\x33\x2d\
\x32\x0c\x69\x50\x72\x6f\x43\x75\x72\x76\x65\x20\x4a\x38\x36\x39\
\x37\x41\x20\x53\x77\x69\x74\x63\x68\x20\x35\x34\x30\x36\x7a\x6c\
\x2c\x20\x72\x65\x76\x69\x73\x69\x6f\x6e\x20\x4b\x2e\x31\x34\x2e\
\x58\x58\x2c\x20\x52\x4f\x4d\x20\x4b\x2e\x31\x32\x2e\x31\x32\x20\
\x28\x2f\x73\x77\x2f\x63\x6f\x64\x65\x2f\x62\x75\x69\x6c\x64\x2f\
\x62\x74\x6d\x28\x6a\x65\x61\x6e\x74\x5f\x6f\x70\x65\x6e\x66\x6c\
\x6f\x77\x5f\x6e\x6f\x63\x68\x65\x63\x6b\x29\x29\x0e\x04\x00\x14\
\x00\x04\x10\x0e\x07\x06\x00\x1f\x28\x20\x48\x00\x02\x00\x00\x00\
\x00\x00\xfe\x09\x00\x12\x0f\x01\x03\x6c\x01\x00\x0f\x00\x00\
"""

class LLDPTestCase(unittest.NoxTestCase):

    def getInterface(self):
        return str(LLDPTestCase)    

    def setUp(self):
        pass 
 
    def tearDown(self):
        pass

    def testLLDP(self):
        eth = ethernet(lldp_str)
        lldph = eth.find('lldp')
        assert(lldph)
        assert(len(lldph.tlvs) == 17) 
        assert(array_to_octstr(lldph.tlvs[0].id) == "00:01:30:f9:ad:a0")
        assert(lldph.tlvs[1].id.tostring() == '1/1')
        assert(lldph.tlvs[2].ttl == 120)

    def testLLDPConstruct(self):
        eth = ethernet(lldp_str)
        lldph = eth.find('lldp')
        assert(len(eth.tostring()) == len(lldp_str))
        assert(eth.tostring() == lldp_str)

    def testLLDPConstruct2(self):
        eth = ethernet(lldp_str_2)
        lldph = eth.find('lldp')
        assert(len(eth.tostring()) == len(lldp_str_2))
        assert(eth.tostring() == lldp_str_2)

def suite(ctxt):
    suite = pyunit.TestSuite()
    suite.addTest(LLDPTestCase("testLLDP", ctxt))
    suite.addTest(LLDPTestCase("testLLDPConstruct", ctxt))
    suite.addTest(LLDPTestCase("testLLDPConstruct2", ctxt))
    return suite
