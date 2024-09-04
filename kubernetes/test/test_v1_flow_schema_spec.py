# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_flow_schema_spec import V1FlowSchemaSpec

class TestV1FlowSchemaSpec(unittest.TestCase):
    """V1FlowSchemaSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1FlowSchemaSpec:
        """Test V1FlowSchemaSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1FlowSchemaSpec`
        """
        model = V1FlowSchemaSpec()
        if include_optional:
            return V1FlowSchemaSpec(
                distinguisher_method = kubernetes.client.models.v1/flow_distinguisher_method.v1.FlowDistinguisherMethod(
                    type = '', ),
                matching_precedence = 56,
                priority_level_configuration = kubernetes.client.models.v1/priority_level_configuration_reference.v1.PriorityLevelConfigurationReference(
                    name = '', ),
                rules = [
                    kubernetes.client.models.v1/policy_rules_with_subjects.v1.PolicyRulesWithSubjects(
                        non_resource_rules = [
                            kubernetes.client.models.v1/non_resource_policy_rule.v1.NonResourcePolicyRule(
                                non_resource_urls = [
                                    ''
                                    ], 
                                verbs = [
                                    ''
                                    ], )
                            ], 
                        resource_rules = [
                            kubernetes.client.models.v1/resource_policy_rule.v1.ResourcePolicyRule(
                                api_groups = [
                                    ''
                                    ], 
                                cluster_scope = True, 
                                namespaces = [
                                    ''
                                    ], 
                                resources = [
                                    ''
                                    ], 
                                verbs = [
                                    ''
                                    ], )
                            ], 
                        subjects = [
                            kubernetes.client.models.flowcontrol/v1/subject.flowcontrol.v1.Subject(
                                group = kubernetes.client.models.v1/group_subject.v1.GroupSubject(
                                    name = '', ), 
                                kind = '', 
                                service_account = kubernetes.client.models.v1/service_account_subject.v1.ServiceAccountSubject(
                                    name = '', 
                                    namespace = '', ), 
                                user = kubernetes.client.models.v1/user_subject.v1.UserSubject(
                                    name = '', ), )
                            ], )
                    ]
            )
        else:
            return V1FlowSchemaSpec(
                priority_level_configuration = kubernetes.client.models.v1/priority_level_configuration_reference.v1.PriorityLevelConfigurationReference(
                    name = '', ),
        )
        """

    def testV1FlowSchemaSpec(self):
        """Test V1FlowSchemaSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
