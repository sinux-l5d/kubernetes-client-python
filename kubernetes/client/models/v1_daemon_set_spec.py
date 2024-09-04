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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from kubernetes.client.models.v1_daemon_set_update_strategy import V1DaemonSetUpdateStrategy
from kubernetes.client.models.v1_label_selector import V1LabelSelector
from kubernetes.client.models.v1_pod_template_spec import V1PodTemplateSpec
from typing import Optional, Set
from typing_extensions import Self

class V1DaemonSetSpec(BaseModel):
    """
    DaemonSetSpec is the specification of a daemon set.
    """ # noqa: E501
    min_ready_seconds: Optional[StrictInt] = Field(default=None, description="The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready).", alias="minReadySeconds")
    revision_history_limit: Optional[StrictInt] = Field(default=None, description="The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.", alias="revisionHistoryLimit")
    selector: V1LabelSelector
    template: V1PodTemplateSpec
    update_strategy: Optional[V1DaemonSetUpdateStrategy] = Field(default=None, alias="updateStrategy")
    __properties: ClassVar[List[str]] = ["minReadySeconds", "revisionHistoryLimit", "selector", "template", "updateStrategy"]

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
        """Create an instance of V1DaemonSetSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of selector
        if self.selector:
            _dict['selector'] = self.selector.to_dict()
        # override the default output from pydantic by calling `to_dict()` of template
        if self.template:
            _dict['template'] = self.template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of update_strategy
        if self.update_strategy:
            _dict['updateStrategy'] = self.update_strategy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1DaemonSetSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "minReadySeconds": obj.get("minReadySeconds"),
            "revisionHistoryLimit": obj.get("revisionHistoryLimit"),
            "selector": V1LabelSelector.from_dict(obj["selector"]) if obj.get("selector") is not None else None,
            "template": V1PodTemplateSpec.from_dict(obj["template"]) if obj.get("template") is not None else None,
            "updateStrategy": V1DaemonSetUpdateStrategy.from_dict(obj["updateStrategy"]) if obj.get("updateStrategy") is not None else None
        })
        return _obj


