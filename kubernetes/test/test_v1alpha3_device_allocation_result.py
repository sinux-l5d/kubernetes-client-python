# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1alpha3_device_allocation_result import V1alpha3DeviceAllocationResult

class TestV1alpha3DeviceAllocationResult(unittest.TestCase):
    """V1alpha3DeviceAllocationResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha3DeviceAllocationResult:
        """Test V1alpha3DeviceAllocationResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha3DeviceAllocationResult`
        """
        model = V1alpha3DeviceAllocationResult()
        if include_optional:
            return V1alpha3DeviceAllocationResult(
                config = [
                    kubernetes.client.models.v1alpha3/device_allocation_configuration.v1alpha3.DeviceAllocationConfiguration(
                        opaque = kubernetes.client.models.v1alpha3/opaque_device_configuration.v1alpha3.OpaqueDeviceConfiguration(
                            driver = '', 
                            parameters = kubernetes.client.models.parameters.parameters(), ), 
                        requests = [
                            ''
                            ], 
                        source = '', )
                    ],
                results = [
                    kubernetes.client.models.v1alpha3/device_request_allocation_result.v1alpha3.DeviceRequestAllocationResult(
                        device = '', 
                        driver = '', 
                        pool = '', 
                        request = '', )
                    ]
            )
        else:
            return V1alpha3DeviceAllocationResult(
        )
        """

    def testV1alpha3DeviceAllocationResult(self):
        """Test V1alpha3DeviceAllocationResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
