# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_exempt_priority_level_configuration import V1ExemptPriorityLevelConfiguration

class TestV1ExemptPriorityLevelConfiguration(unittest.TestCase):
    """V1ExemptPriorityLevelConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ExemptPriorityLevelConfiguration:
        """Test V1ExemptPriorityLevelConfiguration
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ExemptPriorityLevelConfiguration`
        """
        model = V1ExemptPriorityLevelConfiguration()
        if include_optional:
            return V1ExemptPriorityLevelConfiguration(
                lendable_percent = 56,
                nominal_concurrency_shares = 56
            )
        else:
            return V1ExemptPriorityLevelConfiguration(
        )
        """

    def testV1ExemptPriorityLevelConfiguration(self):
        """Test V1ExemptPriorityLevelConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
