"""
    Aries Cloud Agent + didcomm_resolver Plugin

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.6.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import acapy_client
from acapy_client.model.aml_record import AMLRecord
from acapy_client.model.taa_acceptance import TAAAcceptance
from acapy_client.model.taa_record import TAARecord
globals()['AMLRecord'] = AMLRecord
globals()['TAAAcceptance'] = TAAAcceptance
globals()['TAARecord'] = TAARecord
from acapy_client.model.taa_info import TAAInfo


class TestTAAInfo(unittest.TestCase):
    """TAAInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTAAInfo(self):
        """Test TAAInfo"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TAAInfo()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
