# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_csi_node import V1CSINode

class TestV1CSINode(unittest.TestCase):
    """V1CSINode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1CSINode:
        """Test V1CSINode
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1CSINode`
        """
        model = V1CSINode()
        if include_optional:
            return V1CSINode(
                api_version = '',
                kind = '',
                metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                    annotations = {
                        'key' : ''
                        }, 
                    creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deletion_grace_period_seconds = 56, 
                    deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    finalizers = [
                        ''
                        ], 
                    generate_name = '', 
                    generation = 56, 
                    labels = {
                        'key' : ''
                        }, 
                    managed_fields = [
                        kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                            api_version = '', 
                            fields_type = '', 
                            fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                            manager = '', 
                            operation = '', 
                            subresource = '', 
                            time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    name = '', 
                    namespace = '', 
                    owner_references = [
                        kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                            api_version = '', 
                            block_owner_deletion = True, 
                            controller = True, 
                            kind = '', 
                            name = '', 
                            uid = '', )
                        ], 
                    resource_version = '', 
                    self_link = '', 
                    uid = '', ),
                spec = kubernetes.client.models.v1/csi_node_spec.v1.CSINodeSpec(
                    drivers = [
                        kubernetes.client.models.v1/csi_node_driver.v1.CSINodeDriver(
                            allocatable = kubernetes.client.models.v1/volume_node_resources.v1.VolumeNodeResources(
                                count = 56, ), 
                            name = '', 
                            node_id = '', 
                            topology_keys = [
                                ''
                                ], )
                        ], )
            )
        else:
            return V1CSINode(
                spec = kubernetes.client.models.v1/csi_node_spec.v1.CSINodeSpec(
                    drivers = [
                        kubernetes.client.models.v1/csi_node_driver.v1.CSINodeDriver(
                            allocatable = kubernetes.client.models.v1/volume_node_resources.v1.VolumeNodeResources(
                                count = 56, ), 
                            name = '', 
                            node_id = '', 
                            topology_keys = [
                                ''
                                ], )
                        ], ),
        )
        """

    def testV1CSINode(self):
        """Test V1CSINode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
