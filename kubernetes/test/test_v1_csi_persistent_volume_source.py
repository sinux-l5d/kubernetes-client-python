# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_csi_persistent_volume_source import V1CSIPersistentVolumeSource

class TestV1CSIPersistentVolumeSource(unittest.TestCase):
    """V1CSIPersistentVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1CSIPersistentVolumeSource:
        """Test V1CSIPersistentVolumeSource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1CSIPersistentVolumeSource`
        """
        model = V1CSIPersistentVolumeSource()
        if include_optional:
            return V1CSIPersistentVolumeSource(
                controller_expand_secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                    name = '', 
                    namespace = '', ),
                controller_publish_secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                    name = '', 
                    namespace = '', ),
                driver = '',
                fs_type = '',
                node_expand_secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                    name = '', 
                    namespace = '', ),
                node_publish_secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                    name = '', 
                    namespace = '', ),
                node_stage_secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                    name = '', 
                    namespace = '', ),
                read_only = True,
                volume_attributes = {
                    'key' : ''
                    },
                volume_handle = ''
            )
        else:
            return V1CSIPersistentVolumeSource(
                driver = '',
                volume_handle = '',
        )
        """

    def testV1CSIPersistentVolumeSource(self):
        """Test V1CSIPersistentVolumeSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
