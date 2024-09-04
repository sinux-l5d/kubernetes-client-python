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
from kubernetes.client.models.v1_daemon_set_condition import V1DaemonSetCondition
from typing import Optional, Set
from typing_extensions import Self

class V1DaemonSetStatus(BaseModel):
    """
    DaemonSetStatus represents the current status of a daemon set.
    """ # noqa: E501
    collision_count: Optional[StrictInt] = Field(default=None, description="Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.", alias="collisionCount")
    conditions: Optional[List[V1DaemonSetCondition]] = Field(default=None, description="Represents the latest available observations of a DaemonSet's current state.")
    current_number_scheduled: StrictInt = Field(description="The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/", alias="currentNumberScheduled")
    desired_number_scheduled: StrictInt = Field(description="The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/", alias="desiredNumberScheduled")
    number_available: Optional[StrictInt] = Field(default=None, description="The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds)", alias="numberAvailable")
    number_misscheduled: StrictInt = Field(description="The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/", alias="numberMisscheduled")
    number_ready: StrictInt = Field(description="numberReady is the number of nodes that should be running the daemon pod and have one or more of the daemon pod running with a Ready Condition.", alias="numberReady")
    number_unavailable: Optional[StrictInt] = Field(default=None, description="The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds)", alias="numberUnavailable")
    observed_generation: Optional[StrictInt] = Field(default=None, description="The most recent generation observed by the daemon set controller.", alias="observedGeneration")
    updated_number_scheduled: Optional[StrictInt] = Field(default=None, description="The total number of nodes that are running updated daemon pod", alias="updatedNumberScheduled")
    __properties: ClassVar[List[str]] = ["collisionCount", "conditions", "currentNumberScheduled", "desiredNumberScheduled", "numberAvailable", "numberMisscheduled", "numberReady", "numberUnavailable", "observedGeneration", "updatedNumberScheduled"]

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
        """Create an instance of V1DaemonSetStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item_conditions in self.conditions:
                if _item_conditions:
                    _items.append(_item_conditions.to_dict())
            _dict['conditions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1DaemonSetStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "collisionCount": obj.get("collisionCount"),
            "conditions": [V1DaemonSetCondition.from_dict(_item) for _item in obj["conditions"]] if obj.get("conditions") is not None else None,
            "currentNumberScheduled": obj.get("currentNumberScheduled"),
            "desiredNumberScheduled": obj.get("desiredNumberScheduled"),
            "numberAvailable": obj.get("numberAvailable"),
            "numberMisscheduled": obj.get("numberMisscheduled"),
            "numberReady": obj.get("numberReady"),
            "numberUnavailable": obj.get("numberUnavailable"),
            "observedGeneration": obj.get("observedGeneration"),
            "updatedNumberScheduled": obj.get("updatedNumberScheduled")
        })
        return _obj


