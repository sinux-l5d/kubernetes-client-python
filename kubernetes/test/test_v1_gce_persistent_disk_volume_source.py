# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_gce_persistent_disk_volume_source import V1GCEPersistentDiskVolumeSource

class TestV1GCEPersistentDiskVolumeSource(unittest.TestCase):
    """V1GCEPersistentDiskVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1GCEPersistentDiskVolumeSource:
        """Test V1GCEPersistentDiskVolumeSource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1GCEPersistentDiskVolumeSource`
        """
        model = V1GCEPersistentDiskVolumeSource()
        if include_optional:
            return V1GCEPersistentDiskVolumeSource(
                fs_type = '',
                partition = 56,
                pd_name = '',
                read_only = True
            )
        else:
            return V1GCEPersistentDiskVolumeSource(
                pd_name = '',
        )
        """

    def testV1GCEPersistentDiskVolumeSource(self):
        """Test V1GCEPersistentDiskVolumeSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
