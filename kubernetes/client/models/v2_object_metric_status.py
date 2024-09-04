# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from kubernetes.client.models.v2_cross_version_object_reference import V2CrossVersionObjectReference
from kubernetes.client.models.v2_metric_identifier import V2MetricIdentifier
from kubernetes.client.models.v2_metric_value_status import V2MetricValueStatus
from typing import Optional, Set
from typing_extensions import Self

class V2ObjectMetricStatus(BaseModel):
    """
    ObjectMetricStatus indicates the current value of a metric describing a kubernetes object (for example, hits-per-second on an Ingress object).
    """ # noqa: E501
    current: V2MetricValueStatus
    described_object: V2CrossVersionObjectReference = Field(alias="describedObject")
    metric: V2MetricIdentifier
    __properties: ClassVar[List[str]] = ["current", "describedObject", "metric"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V2ObjectMetricStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of current
        if self.current:
            _dict['current'] = self.current.to_dict()
        # override the default output from pydantic by calling `to_dict()` of described_object
        if self.described_object:
            _dict['describedObject'] = self.described_object.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metric
        if self.metric:
            _dict['metric'] = self.metric.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V2ObjectMetricStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "current": V2MetricValueStatus.from_dict(obj["current"]) if obj.get("current") is not None else None,
            "describedObject": V2CrossVersionObjectReference.from_dict(obj["describedObject"]) if obj.get("describedObject") is not None else None,
            "metric": V2MetricIdentifier.from_dict(obj["metric"]) if obj.get("metric") is not None else None
        })
        return _obj


