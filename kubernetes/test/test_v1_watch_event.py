# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_watch_event import V1WatchEvent

class TestV1WatchEvent(unittest.TestCase):
    """V1WatchEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1WatchEvent:
        """Test V1WatchEvent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1WatchEvent`
        """
        model = V1WatchEvent()
        if include_optional:
            return V1WatchEvent(
                object = None,
                type = ''
            )
        else:
            return V1WatchEvent(
                object = None,
                type = '',
        )
        """

    def testV1WatchEvent(self):
        """Test V1WatchEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
