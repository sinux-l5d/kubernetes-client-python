# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_probe import V1Probe

class TestV1Probe(unittest.TestCase):
    """V1Probe unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1Probe:
        """Test V1Probe
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1Probe`
        """
        model = V1Probe()
        if include_optional:
            return V1Probe(
                var_exec = kubernetes.client.models.v1/exec_action.v1.ExecAction(
                    command = [
                        ''
                        ], ),
                failure_threshold = 56,
                grpc = kubernetes.client.models.v1/grpc_action.v1.GRPCAction(
                    port = 56, 
                    service = '', ),
                http_get = kubernetes.client.models.v1/http_get_action.v1.HTTPGetAction(
                    host = '', 
                    http_headers = [
                        kubernetes.client.models.v1/http_header.v1.HTTPHeader(
                            name = '', 
                            value = '', )
                        ], 
                    path = '', 
                    port = kubernetes.client.models.port.port(), 
                    scheme = '', ),
                initial_delay_seconds = 56,
                period_seconds = 56,
                success_threshold = 56,
                tcp_socket = kubernetes.client.models.v1/tcp_socket_action.v1.TCPSocketAction(
                    host = '', 
                    port = kubernetes.client.models.port.port(), ),
                termination_grace_period_seconds = 56,
                timeout_seconds = 56
            )
        else:
            return V1Probe(
        )
        """

    def testV1Probe(self):
        """Test V1Probe"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
