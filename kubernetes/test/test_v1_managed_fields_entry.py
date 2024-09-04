# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_managed_fields_entry import V1ManagedFieldsEntry

class TestV1ManagedFieldsEntry(unittest.TestCase):
    """V1ManagedFieldsEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ManagedFieldsEntry:
        """Test V1ManagedFieldsEntry
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ManagedFieldsEntry`
        """
        model = V1ManagedFieldsEntry()
        if include_optional:
            return V1ManagedFieldsEntry(
                api_version = '',
                fields_type = '',
                fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(),
                manager = '',
                operation = '',
                subresource = '',
                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return V1ManagedFieldsEntry(
        )
        """

    def testV1ManagedFieldsEntry(self):
        """Test V1ManagedFieldsEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
