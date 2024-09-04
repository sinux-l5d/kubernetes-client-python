# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_network_policy_egress_rule import V1NetworkPolicyEgressRule

class TestV1NetworkPolicyEgressRule(unittest.TestCase):
    """V1NetworkPolicyEgressRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1NetworkPolicyEgressRule:
        """Test V1NetworkPolicyEgressRule
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1NetworkPolicyEgressRule`
        """
        model = V1NetworkPolicyEgressRule()
        if include_optional:
            return V1NetworkPolicyEgressRule(
                ports = [
                    kubernetes.client.models.v1/network_policy_port.v1.NetworkPolicyPort(
                        end_port = 56, 
                        port = kubernetes.client.models.port.port(), 
                        protocol = '', )
                    ],
                to = [
                    kubernetes.client.models.v1/network_policy_peer.v1.NetworkPolicyPeer(
                        ip_block = kubernetes.client.models.v1/ip_block.v1.IPBlock(
                            cidr = '', 
                            except = [
                                ''
                                ], ), 
                        namespace_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                            match_expressions = [
                                kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                                    key = '', 
                                    operator = '', 
                                    values = [
                                        ''
                                        ], )
                                ], 
                            match_labels = {
                                'key' : ''
                                }, ), 
                        pod_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(), )
                    ]
            )
        else:
            return V1NetworkPolicyEgressRule(
        )
        """

    def testV1NetworkPolicyEgressRule(self):
        """Test V1NetworkPolicyEgressRule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
