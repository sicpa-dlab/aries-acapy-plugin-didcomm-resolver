"""
    Aries Cloud Agent + didcomm_resolver Plugin

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.6.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import acapy_client
from acapy_client.api.resolver_api import ResolverApi  # noqa: E501


class TestResolverApi(unittest.TestCase):
    """ResolverApi unit test stubs"""

    def setUp(self):
        self.api = ResolverApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_resolve(self):
        """Test case for resolve

        Retrieve doc for requested did  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
