# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_variable import V1Variable

class TestV1Variable(unittest.TestCase):
    """V1Variable unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1Variable:
        """Test V1Variable
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1Variable`
        """
        model = V1Variable()
        if include_optional:
            return V1Variable(
                expression = '',
                name = ''
            )
        else:
            return V1Variable(
                expression = '',
                name = '',
        )
        """

    def testV1Variable(self):
        """Test V1Variable"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
