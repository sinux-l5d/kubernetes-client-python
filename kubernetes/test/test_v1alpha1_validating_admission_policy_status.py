# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1alpha1_validating_admission_policy_status import V1alpha1ValidatingAdmissionPolicyStatus

class TestV1alpha1ValidatingAdmissionPolicyStatus(unittest.TestCase):
    """V1alpha1ValidatingAdmissionPolicyStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha1ValidatingAdmissionPolicyStatus:
        """Test V1alpha1ValidatingAdmissionPolicyStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha1ValidatingAdmissionPolicyStatus`
        """
        model = V1alpha1ValidatingAdmissionPolicyStatus()
        if include_optional:
            return V1alpha1ValidatingAdmissionPolicyStatus(
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
                        ], )
            )
        else:
            return V1alpha1ValidatingAdmissionPolicyStatus(
        )
        """

    def testV1alpha1ValidatingAdmissionPolicyStatus(self):
        """Test V1alpha1ValidatingAdmissionPolicyStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
