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
from kubernetes.client.models.v1_condition import V1Condition
from kubernetes.client.models.v1alpha1_type_checking import V1alpha1TypeChecking
from typing import Optional, Set
from typing_extensions import Self

class V1alpha1ValidatingAdmissionPolicyStatus(BaseModel):
    """
    ValidatingAdmissionPolicyStatus represents the status of a ValidatingAdmissionPolicy.
    """ # noqa: E501
    conditions: Optional[List[V1Condition]] = Field(default=None, description="The conditions represent the latest available observations of a policy's current state.")
    observed_generation: Optional[StrictInt] = Field(default=None, description="The generation observed by the controller.", alias="observedGeneration")
    type_checking: Optional[V1alpha1TypeChecking] = Field(default=None, alias="typeChecking")
    __properties: ClassVar[List[str]] = ["conditions", "observedGeneration", "typeChecking"]

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
        """Create an instance of V1alpha1ValidatingAdmissionPolicyStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of type_checking
        if self.type_checking:
            _dict['typeChecking'] = self.type_checking.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1alpha1ValidatingAdmissionPolicyStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "conditions": [V1Condition.from_dict(_item) for _item in obj["conditions"]] if obj.get("conditions") is not None else None,
            "observedGeneration": obj.get("observedGeneration"),
            "typeChecking": V1alpha1TypeChecking.from_dict(obj["typeChecking"]) if obj.get("typeChecking") is not None else None
        })
        return _obj


