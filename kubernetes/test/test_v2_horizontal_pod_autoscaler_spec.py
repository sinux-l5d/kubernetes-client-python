# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v2_horizontal_pod_autoscaler_spec import V2HorizontalPodAutoscalerSpec

class TestV2HorizontalPodAutoscalerSpec(unittest.TestCase):
    """V2HorizontalPodAutoscalerSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2HorizontalPodAutoscalerSpec:
        """Test V2HorizontalPodAutoscalerSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2HorizontalPodAutoscalerSpec`
        """
        model = V2HorizontalPodAutoscalerSpec()
        if include_optional:
            return V2HorizontalPodAutoscalerSpec(
                behavior = kubernetes.client.models.v2/horizontal_pod_autoscaler_behavior.v2.HorizontalPodAutoscalerBehavior(
                    scale_down = kubernetes.client.models.v2/hpa_scaling_rules.v2.HPAScalingRules(
                        policies = [
                            kubernetes.client.models.v2/hpa_scaling_policy.v2.HPAScalingPolicy(
                                period_seconds = 56, 
                                type = '', 
                                value = 56, )
                            ], 
                        select_policy = '', 
                        stabilization_window_seconds = 56, ), 
                    scale_up = kubernetes.client.models.v2/hpa_scaling_rules.v2.HPAScalingRules(
                        select_policy = '', 
                        stabilization_window_seconds = 56, ), ),
                max_replicas = 56,
                metrics = [
                    kubernetes.client.models.v2/metric_spec.v2.MetricSpec(
                        container_resource = kubernetes.client.models.v2/container_resource_metric_source.v2.ContainerResourceMetricSource(
                            container = '', 
                            name = '', 
                            target = kubernetes.client.models.v2/metric_target.v2.MetricTarget(
                                average_utilization = 56, 
                                average_value = '', 
                                type = '', 
                                value = '', ), ), 
                        external = kubernetes.client.models.v2/external_metric_source.v2.ExternalMetricSource(
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
                                value = '', ), ), 
                        object = kubernetes.client.models.v2/object_metric_source.v2.ObjectMetricSource(
                            described_object = kubernetes.client.models.v2/cross_version_object_reference.v2.CrossVersionObjectReference(
                                api_version = '', 
                                kind = '', 
                                name = '', ), 
                            metric = kubernetes.client.models.v2/metric_identifier.v2.MetricIdentifier(
                                name = '', ), 
                            target = , ), 
                        pods = kubernetes.client.models.v2/pods_metric_source.v2.PodsMetricSource(
                            metric = , 
                            target = , ), 
                        resource = kubernetes.client.models.v2/resource_metric_source.v2.ResourceMetricSource(
                            name = '', 
                            target = , ), 
                        type = '', )
                    ],
                min_replicas = 56,
                scale_target_ref = kubernetes.client.models.v2/cross_version_object_reference.v2.CrossVersionObjectReference(
                    api_version = '', 
                    kind = '', 
                    name = '', )
            )
        else:
            return V2HorizontalPodAutoscalerSpec(
                max_replicas = 56,
                scale_target_ref = kubernetes.client.models.v2/cross_version_object_reference.v2.CrossVersionObjectReference(
                    api_version = '', 
                    kind = '', 
                    name = '', ),
        )
        """

    def testV2HorizontalPodAutoscalerSpec(self):
        """Test V2HorizontalPodAutoscalerSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
