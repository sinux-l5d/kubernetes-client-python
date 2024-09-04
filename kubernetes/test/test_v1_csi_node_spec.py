# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_csi_node_spec import V1CSINodeSpec

class TestV1CSINodeSpec(unittest.TestCase):
    """V1CSINodeSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1CSINodeSpec:
        """Test V1CSINodeSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1CSINodeSpec`
        """
        model = V1CSINodeSpec()
        if include_optional:
            return V1CSINodeSpec(
                drivers = [
                    kubernetes.client.models.v1/csi_node_driver.v1.CSINodeDriver(
                        allocatable = kubernetes.client.models.v1/volume_node_resources.v1.VolumeNodeResources(
                            count = 56, ), 
                        name = '', 
                        node_id = '', 
                        topology_keys = [
                            ''
                            ], )
                    ]
            )
        else:
            return V1CSINodeSpec(
                drivers = [
                    kubernetes.client.models.v1/csi_node_driver.v1.CSINodeDriver(
                        allocatable = kubernetes.client.models.v1/volume_node_resources.v1.VolumeNodeResources(
                            count = 56, ), 
                        name = '', 
                        node_id = '', 
                        topology_keys = [
                            ''
                            ], )
                    ],
        )
        """

    def testV1CSINodeSpec(self):
        """Test V1CSINodeSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
