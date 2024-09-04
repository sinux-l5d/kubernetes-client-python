# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_api_resource import V1APIResource

class TestV1APIResource(unittest.TestCase):
    """V1APIResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1APIResource:
        """Test V1APIResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1APIResource`
        """
        model = V1APIResource()
        if include_optional:
            return V1APIResource(
                categories = [
                    ''
                    ],
                group = '',
                kind = '',
                name = '',
                namespaced = True,
                short_names = [
                    ''
                    ],
                singular_name = '',
                storage_version_hash = '',
                verbs = [
                    ''
                    ],
                version = ''
            )
        else:
            return V1APIResource(
                kind = '',
                name = '',
                namespaced = True,
                singular_name = '',
                verbs = [
                    ''
                    ],
        )
        """

    def testV1APIResource(self):
        """Test V1APIResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
