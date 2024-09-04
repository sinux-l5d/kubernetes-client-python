# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_downward_api_volume_file import V1DownwardAPIVolumeFile

class TestV1DownwardAPIVolumeFile(unittest.TestCase):
    """V1DownwardAPIVolumeFile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DownwardAPIVolumeFile:
        """Test V1DownwardAPIVolumeFile
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DownwardAPIVolumeFile`
        """
        model = V1DownwardAPIVolumeFile()
        if include_optional:
            return V1DownwardAPIVolumeFile(
                field_ref = kubernetes.client.models.v1/object_field_selector.v1.ObjectFieldSelector(
                    api_version = '', 
                    field_path = '', ),
                mode = 56,
                path = '',
                resource_field_ref = kubernetes.client.models.v1/resource_field_selector.v1.ResourceFieldSelector(
                    container_name = '', 
                    divisor = '', 
                    resource = '', )
            )
        else:
            return V1DownwardAPIVolumeFile(
                path = '',
        )
        """

    def testV1DownwardAPIVolumeFile(self):
        """Test V1DownwardAPIVolumeFile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
