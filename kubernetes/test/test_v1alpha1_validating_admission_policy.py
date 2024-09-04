# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1alpha1_validating_admission_policy import V1alpha1ValidatingAdmissionPolicy

class TestV1alpha1ValidatingAdmissionPolicy(unittest.TestCase):
    """V1alpha1ValidatingAdmissionPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha1ValidatingAdmissionPolicy:
        """Test V1alpha1ValidatingAdmissionPolicy
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha1ValidatingAdmissionPolicy`
        """
        model = V1alpha1ValidatingAdmissionPolicy()
        if include_optional:
            return V1alpha1ValidatingAdmissionPolicy(
                api_version = '',
                kind = '',
                metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                    annotations = {
                        'key' : ''
                        }, 
                    creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deletion_grace_period_seconds = 56, 
                    deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    finalizers = [
                        ''
                        ], 
                    generate_name = '', 
                    generation = 56, 
                    labels = {
                        'key' : ''
                        }, 
                    managed_fields = [
                        kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                            api_version = '', 
                            fields_type = '', 
                            fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                            manager = '', 
                            operation = '', 
                            subresource = '', 
                            time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    name = '', 
                    namespace = '', 
                    owner_references = [
                        kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                            api_version = '', 
                            block_owner_deletion = True, 
                            controller = True, 
                            kind = '', 
                            name = '', 
                            uid = '', )
                        ], 
                    resource_version = '', 
                    self_link = '', 
                    uid = '', ),
                spec = kubernetes.client.models.v1alpha1/validating_admission_policy_spec.v1alpha1.ValidatingAdmissionPolicySpec(
                    audit_annotations = [
                        kubernetes.client.models.v1alpha1/audit_annotation.v1alpha1.AuditAnnotation(
                            key = '', 
                            value_expression = '', )
                        ], 
                    failure_policy = '', 
                    match_conditions = [
                        kubernetes.client.models.v1alpha1/match_condition.v1alpha1.MatchCondition(
                            expression = '', 
                            name = '', )
                        ], 
                    match_constraints = kubernetes.client.models.v1alpha1/match_resources.v1alpha1.MatchResources(
                        exclude_resource_rules = [
                            kubernetes.client.models.v1alpha1/named_rule_with_operations.v1alpha1.NamedRuleWithOperations(
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
                            kubernetes.client.models.v1alpha1/named_rule_with_operations.v1alpha1.NamedRuleWithOperations(
                                scope = '', )
                            ], ), 
                    param_kind = kubernetes.client.models.v1alpha1/param_kind.v1alpha1.ParamKind(
                        api_version = '', 
                        kind = '', ), 
                    validations = [
                        kubernetes.client.models.v1alpha1/validation.v1alpha1.Validation(
                            expression = '', 
                            message = '', 
                            message_expression = '', 
                            reason = '', )
                        ], 
                    variables = [
                        kubernetes.client.models.v1alpha1/variable.v1alpha1.Variable(
                            expression = '', 
                            name = '', )
                        ], ),
                status = kubernetes.client.models.v1alpha1/validating_admission_policy_status.v1alpha1.ValidatingAdmissionPolicyStatus(
                    conditions = [
                        kubernetes.client.models.v1/condition.v1.Condition(
                            last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            message = '', 
                            observed_generation = 56, 
                            reason = '', 
                            status = '', 
                            type = '', )
                        ], 
                    observed_generation = 56, 
                    type_checking = kubernetes.client.models.v1alpha1/type_checking.v1alpha1.TypeChecking(
                        expression_warnings = [
                            kubernetes.client.models.v1alpha1/expression_warning.v1alpha1.ExpressionWarning(
                                field_ref = '', 
                                warning = '', )
                            ], ), )
            )
        else:
            return V1alpha1ValidatingAdmissionPolicy(
        )
        """

    def testV1alpha1ValidatingAdmissionPolicy(self):
        """Test V1alpha1ValidatingAdmissionPolicy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
