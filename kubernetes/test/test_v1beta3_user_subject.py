# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1beta3_user_subject import V1beta3UserSubject

class TestV1beta3UserSubject(unittest.TestCase):
    """V1beta3UserSubject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1beta3UserSubject:
        """Test V1beta3UserSubject
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1beta3UserSubject`
        """
        model = V1beta3UserSubject()
        if include_optional:
            return V1beta3UserSubject(
                name = ''
            )
        else:
            return V1beta3UserSubject(
                name = '',
        )
        """

    def testV1beta3UserSubject(self):
        """Test V1beta3UserSubject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
