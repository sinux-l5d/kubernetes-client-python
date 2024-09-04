# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_pod_disruption_budget_status import V1PodDisruptionBudgetStatus

class TestV1PodDisruptionBudgetStatus(unittest.TestCase):
    """V1PodDisruptionBudgetStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1PodDisruptionBudgetStatus:
        """Test V1PodDisruptionBudgetStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1PodDisruptionBudgetStatus`
        """
        model = V1PodDisruptionBudgetStatus()
        if include_optional:
            return V1PodDisruptionBudgetStatus(
                conditions = [
                    kubernetes.client.models.v1/condition.v1.Condition(
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        observed_generation = 56, 
                        reason = '', 
                        status = '', 
                        type = '', )
                    ],
                current_healthy = 56,
                desired_healthy = 56,
                disrupted_pods = {
                    'key' : datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                    },
                disruptions_allowed = 56,
                expected_pods = 56,
                observed_generation = 56
            )
        else:
            return V1PodDisruptionBudgetStatus(
                current_healthy = 56,
                desired_healthy = 56,
                disruptions_allowed = 56,
                expected_pods = 56,
        )
        """

    def testV1PodDisruptionBudgetStatus(self):
        """Test V1PodDisruptionBudgetStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
