# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v2_object_metric_source import V2ObjectMetricSource

class TestV2ObjectMetricSource(unittest.TestCase):
    """V2ObjectMetricSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2ObjectMetricSource:
        """Test V2ObjectMetricSource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2ObjectMetricSource`
        """
        model = V2ObjectMetricSource()
        if include_optional:
            return V2ObjectMetricSource(
                described_object = kubernetes.client.models.v2/cross_version_object_reference.v2.CrossVersionObjectReference(
                    api_version = '', 
                    kind = '', 
                    name = '', ),
                metric = kubernetes.client.models.v2/metric_identifier.v2.MetricIdentifier(
                    name = '', 
                    selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
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
                            }, ), ),
                target = kubernetes.client.models.v2/metric_target.v2.MetricTarget(
                    average_utilization = 56, 
                    average_value = '', 
                    type = '', 
                    value = '', )
            )
        else:
            return V2ObjectMetricSource(
                described_object = kubernetes.client.models.v2/cross_version_object_reference.v2.CrossVersionObjectReference(
                    api_version = '', 
                    kind = '', 
                    name = '', ),
                metric = kubernetes.client.models.v2/metric_identifier.v2.MetricIdentifier(
                    name = '', 
                    selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
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
                            }, ), ),
                target = kubernetes.client.models.v2/metric_target.v2.MetricTarget(
                    average_utilization = 56, 
                    average_value = '', 
                    type = '', 
                    value = '', ),
        )
        """

    def testV2ObjectMetricSource(self):
        """Test V2ObjectMetricSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
