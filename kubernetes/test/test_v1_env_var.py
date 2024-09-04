# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_env_var import V1EnvVar

class TestV1EnvVar(unittest.TestCase):
    """V1EnvVar unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1EnvVar:
        """Test V1EnvVar
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1EnvVar`
        """
        model = V1EnvVar()
        if include_optional:
            return V1EnvVar(
                name = '',
                value = '',
                value_from = kubernetes.client.models.v1/env_var_source.v1.EnvVarSource(
                    config_map_key_ref = kubernetes.client.models.v1/config_map_key_selector.v1.ConfigMapKeySelector(
                        key = '', 
                        name = '', 
                        optional = True, ), 
                    field_ref = kubernetes.client.models.v1/object_field_selector.v1.ObjectFieldSelector(
                        api_version = '', 
                        field_path = '', ), 
                    resource_field_ref = kubernetes.client.models.v1/resource_field_selector.v1.ResourceFieldSelector(
                        container_name = '', 
                        divisor = '', 
                        resource = '', ), 
                    secret_key_ref = kubernetes.client.models.v1/secret_key_selector.v1.SecretKeySelector(
                        key = '', 
                        name = '', 
                        optional = True, ), )
            )
        else:
            return V1EnvVar(
                name = '',
        )
        """

    def testV1EnvVar(self):
        """Test V1EnvVar"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
