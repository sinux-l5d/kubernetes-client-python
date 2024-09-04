# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_match_resources import V1MatchResources

class TestV1MatchResources(unittest.TestCase):
    """V1MatchResources unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1MatchResources:
        """Test V1MatchResources
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1MatchResources`
        """
        model = V1MatchResources()
        if include_optional:
            return V1MatchResources(
                exclude_resource_rules = [
                    kubernetes.client.models.v1/named_rule_with_operations.v1.NamedRuleWithOperations(
                        api_groups = [
                            ''
                            ], 
                        api_versions = [
                            ''
                            ], 
                        operations = [
                            ''
                            ], 
                        resource_names = [
                            ''
                            ], 
                        resources = [
                            ''
                            ], 
                        scope = '', )
                    ],
                match_policy = '',
                namespace_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                    match_expressions = [
                        kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                            key = '', 
                            operator = '', 
                            values = [
                                ''
                                ], )
                        ], 
                    match_labels = {
                        'key' : ''
                        }, ),
                object_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                    match_expressions = [
                        kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                            key = '', 
                            operator = '', 
                            values = [
                                ''
                                ], )
                        ], 
                    match_labels = {
                        'key' : ''
                        }, ),
                resource_rules = [
                    kubernetes.client.models.v1/named_rule_with_operations.v1.NamedRuleWithOperations(
                        api_groups = [
                            ''
                            ], 
                        api_versions = [
                            ''
                            ], 
                        operations = [
                            ''
                            ], 
                        resource_names = [
                            ''
                            ], 
                        resources = [
                            ''
                            ], 
                        scope = '', )
                    ]
            )
        else:
            return V1MatchResources(
        )
        """

    def testV1MatchResources(self):
        """Test V1MatchResources"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
