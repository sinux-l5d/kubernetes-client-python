# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_flocker_volume_source import V1FlockerVolumeSource

class TestV1FlockerVolumeSource(unittest.TestCase):
    """V1FlockerVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1FlockerVolumeSource:
        """Test V1FlockerVolumeSource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1FlockerVolumeSource`
        """
        model = V1FlockerVolumeSource()
        if include_optional:
            return V1FlockerVolumeSource(
                dataset_name = '',
                dataset_uuid = ''
            )
        else:
            return V1FlockerVolumeSource(
        )
        """

    def testV1FlockerVolumeSource(self):
        """Test V1FlockerVolumeSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
