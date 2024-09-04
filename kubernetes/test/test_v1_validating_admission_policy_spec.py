# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_validating_admission_policy_spec import V1ValidatingAdmissionPolicySpec

class TestV1ValidatingAdmissionPolicySpec(unittest.TestCase):
    """V1ValidatingAdmissionPolicySpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ValidatingAdmissionPolicySpec:
        """Test V1ValidatingAdmissionPolicySpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ValidatingAdmissionPolicySpec`
        """
        model = V1ValidatingAdmissionPolicySpec()
        if include_optional:
            return V1ValidatingAdmissionPolicySpec(
                audit_annotations = [
                    kubernetes.client.models.v1/audit_annotation.v1.AuditAnnotation(
                        key = '', 
                        value_expression = '', )
                    ],
                failure_policy = '',
                match_conditions = [
                    kubernetes.client.models.v1/match_condition.v1.MatchCondition(
                        expression = '', 
                        name = '', )
                    ],
                match_constraints = kubernetes.client.models.v1/match_resources.v1.MatchResources(
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
                    object_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(), 
                    resource_rules = [
                        kubernetes.client.models.v1/named_rule_with_operations.v1.NamedRuleWithOperations(
                            scope = '', )
                        ], ),
                param_kind = kubernetes.client.models.v1/param_kind.v1.ParamKind(
                    api_version = '', 
                    kind = '', ),
                validations = [
                    kubernetes.client.models.v1/validation.v1.Validation(
                        expression = '', 
                        message = '', 
                        message_expression = '', 
                        reason = '', )
                    ],
                variables = [
                    kubernetes.client.models.v1/variable.v1.Variable(
                        expression = '', 
                        name = '', )
                    ]
            )
        else:
            return V1ValidatingAdmissionPolicySpec(
        )
        """

    def testV1ValidatingAdmissionPolicySpec(self):
        """Test V1ValidatingAdmissionPolicySpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
