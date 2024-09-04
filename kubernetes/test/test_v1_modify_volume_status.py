# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_modify_volume_status import V1ModifyVolumeStatus

class TestV1ModifyVolumeStatus(unittest.TestCase):
    """V1ModifyVolumeStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ModifyVolumeStatus:
        """Test V1ModifyVolumeStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ModifyVolumeStatus`
        """
        model = V1ModifyVolumeStatus()
        if include_optional:
            return V1ModifyVolumeStatus(
                status = '',
                target_volume_attributes_class_name = ''
            )
        else:
            return V1ModifyVolumeStatus(
                status = '',
        )
        """

    def testV1ModifyVolumeStatus(self):
        """Test V1ModifyVolumeStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
