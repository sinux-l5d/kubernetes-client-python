# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_rule_with_operations import V1RuleWithOperations

class TestV1RuleWithOperations(unittest.TestCase):
    """V1RuleWithOperations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1RuleWithOperations:
        """Test V1RuleWithOperations
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1RuleWithOperations`
        """
        model = V1RuleWithOperations()
        if include_optional:
            return V1RuleWithOperations(
                api_groups = [
                    ''
                    ],
                api_versions = [
                    ''
                    ],
                operations = [
                    ''
                    ],
                resources = [
                    ''
                    ],
                scope = ''
            )
        else:
            return V1RuleWithOperations(
        )
        """

    def testV1RuleWithOperations(self):
        """Test V1RuleWithOperations"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
