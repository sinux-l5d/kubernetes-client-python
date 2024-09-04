# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_csi_volume_source import V1CSIVolumeSource

class TestV1CSIVolumeSource(unittest.TestCase):
    """V1CSIVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1CSIVolumeSource:
        """Test V1CSIVolumeSource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1CSIVolumeSource`
        """
        model = V1CSIVolumeSource()
        if include_optional:
            return V1CSIVolumeSource(
                driver = '',
                fs_type = '',
                node_publish_secret_ref = kubernetes.client.models.v1/local_object_reference.v1.LocalObjectReference(
                    name = '', ),
                read_only = True,
                volume_attributes = {
                    'key' : ''
                    }
            )
        else:
            return V1CSIVolumeSource(
                driver = '',
        )
        """

    def testV1CSIVolumeSource(self):
        """Test V1CSIVolumeSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
