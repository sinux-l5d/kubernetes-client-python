# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1beta1_validating_admission_policy_binding_spec import V1beta1ValidatingAdmissionPolicyBindingSpec

class TestV1beta1ValidatingAdmissionPolicyBindingSpec(unittest.TestCase):
    """V1beta1ValidatingAdmissionPolicyBindingSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1beta1ValidatingAdmissionPolicyBindingSpec:
        """Test V1beta1ValidatingAdmissionPolicyBindingSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1beta1ValidatingAdmissionPolicyBindingSpec`
        """
        model = V1beta1ValidatingAdmissionPolicyBindingSpec()
        if include_optional:
            return V1beta1ValidatingAdmissionPolicyBindingSpec(
                match_resources = kubernetes.client.models.v1beta1/match_resources.v1beta1.MatchResources(
                    exclude_resource_rules = [
                        kubernetes.client.models.v1beta1/named_rule_with_operations.v1beta1.NamedRuleWithOperations(
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
                        kubernetes.client.models.v1beta1/named_rule_with_operations.v1beta1.NamedRuleWithOperations(
                            scope = '', )
                        ], ),
                param_ref = kubernetes.client.models.v1beta1/param_ref.v1beta1.ParamRef(
                    name = '', 
                    namespace = '', 
                    parameter_not_found_action = '', 
                    selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
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
                            }, ), ),
                policy_name = '',
                validation_actions = [
                    ''
                    ]
            )
        else:
            return V1beta1ValidatingAdmissionPolicyBindingSpec(
        )
        """

    def testV1beta1ValidatingAdmissionPolicyBindingSpec(self):
        """Test V1beta1ValidatingAdmissionPolicyBindingSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
