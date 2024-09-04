# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_persistent_volume_claim_status import V1PersistentVolumeClaimStatus

class TestV1PersistentVolumeClaimStatus(unittest.TestCase):
    """V1PersistentVolumeClaimStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1PersistentVolumeClaimStatus:
        """Test V1PersistentVolumeClaimStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1PersistentVolumeClaimStatus`
        """
        model = V1PersistentVolumeClaimStatus()
        if include_optional:
            return V1PersistentVolumeClaimStatus(
                access_modes = [
                    ''
                    ],
                allocated_resource_statuses = {
                    'key' : ''
                    },
                allocated_resources = {
                    'key' : ''
                    },
                capacity = {
                    'key' : ''
                    },
                conditions = [
                    kubernetes.client.models.v1/persistent_volume_claim_condition.v1.PersistentVolumeClaimCondition(
                        last_probe_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        reason = '', 
                        status = '', 
                        type = '', )
                    ],
                current_volume_attributes_class_name = '',
                modify_volume_status = kubernetes.client.models.v1/modify_volume_status.v1.ModifyVolumeStatus(
                    status = '', 
                    target_volume_attributes_class_name = '', ),
                phase = ''
            )
        else:
            return V1PersistentVolumeClaimStatus(
        )
        """

    def testV1PersistentVolumeClaimStatus(self):
        """Test V1PersistentVolumeClaimStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
