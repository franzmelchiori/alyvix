import sys
import unittest

from tests.client_test import *
from tests.protocol_test import *

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(ProtocolParserTest))
    test_suite.addTest(unittest.makeSuite(ClientUtilsTest))
    test_suite.addTest(unittest.makeSuite(ClientTest))
    test_suite.addTest(unittest.makeSuite(ClientAuthTest))
    test_suite.addTest(unittest.makeSuite(ClientTLSTest))

    # Skip verify tests unless on Python 2.7
    if sys.version_info >= (2, 7):
        test_suite.addTest(unittest.makeSuite(ClientTLSCertsTest))

    runner = unittest.TextTestRunner(stream=sys.stdout)
    result = runner.run(test_suite)
    if not result.wasSuccessful():
        sys.exit(1)
