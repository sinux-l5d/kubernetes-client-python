# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_config_map_key_selector import V1ConfigMapKeySelector

class TestV1ConfigMapKeySelector(unittest.TestCase):
    """V1ConfigMapKeySelector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ConfigMapKeySelector:
        """Test V1ConfigMapKeySelector
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ConfigMapKeySelector`
        """
        model = V1ConfigMapKeySelector()
        if include_optional:
            return V1ConfigMapKeySelector(
                key = '',
                name = '',
                optional = True
            )
        else:
            return V1ConfigMapKeySelector(
                key = '',
        )
        """

    def testV1ConfigMapKeySelector(self):
        """Test V1ConfigMapKeySelector"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
