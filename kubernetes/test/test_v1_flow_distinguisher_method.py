# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_flow_distinguisher_method import V1FlowDistinguisherMethod

class TestV1FlowDistinguisherMethod(unittest.TestCase):
    """V1FlowDistinguisherMethod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1FlowDistinguisherMethod:
        """Test V1FlowDistinguisherMethod
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1FlowDistinguisherMethod`
        """
        model = V1FlowDistinguisherMethod()
        if include_optional:
            return V1FlowDistinguisherMethod(
                type = ''
            )
        else:
            return V1FlowDistinguisherMethod(
                type = '',
        )
        """

    def testV1FlowDistinguisherMethod(self):
        """Test V1FlowDistinguisherMethod"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
