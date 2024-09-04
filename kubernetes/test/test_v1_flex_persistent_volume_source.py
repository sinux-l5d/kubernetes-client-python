# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_flex_persistent_volume_source import V1FlexPersistentVolumeSource

class TestV1FlexPersistentVolumeSource(unittest.TestCase):
    """V1FlexPersistentVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1FlexPersistentVolumeSource:
        """Test V1FlexPersistentVolumeSource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1FlexPersistentVolumeSource`
        """
        model = V1FlexPersistentVolumeSource()
        if include_optional:
            return V1FlexPersistentVolumeSource(
                driver = '',
                fs_type = '',
                options = {
                    'key' : ''
                    },
                read_only = True,
                secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                    name = '', 
                    namespace = '', )
            )
        else:
            return V1FlexPersistentVolumeSource(
                driver = '',
        )
        """

    def testV1FlexPersistentVolumeSource(self):
        """Test V1FlexPersistentVolumeSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
