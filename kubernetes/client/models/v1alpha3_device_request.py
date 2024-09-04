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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kubernetes.client.models.v1alpha3_device_selector import V1alpha3DeviceSelector
from typing import Optional, Set
from typing_extensions import Self

class V1alpha3DeviceRequest(BaseModel):
    """
    DeviceRequest is a request for devices required for a claim. This is typically a request for a single resource like a device, but can also ask for several identical devices.  A DeviceClassName is currently required. Clients must check that it is indeed set. It's absence indicates that something changed in a way that is not supported by the client yet, in which case it must refuse to handle the request.
    """ # noqa: E501
    admin_access: Optional[StrictBool] = Field(default=None, description="AdminAccess indicates that this is a claim for administrative access to the device(s). Claims with AdminAccess are expected to be used for monitoring or other management services for a device.  They ignore all ordinary claims to the device with respect to access modes and any resource allocations.", alias="adminAccess")
    allocation_mode: Optional[StrictStr] = Field(default=None, description="AllocationMode and its related fields define how devices are allocated to satisfy this request. Supported values are:  - ExactCount: This request is for a specific number of devices.   This is the default. The exact number is provided in the   count field.  - All: This request is for all of the matching devices in a pool.   Allocation will fail if some devices are already allocated,   unless adminAccess is requested.  If AlloctionMode is not specified, the default mode is ExactCount. If the mode is ExactCount and count is not specified, the default count is one. Any other requests must specify this field.  More modes may get added in the future. Clients must refuse to handle requests with unknown modes.", alias="allocationMode")
    count: Optional[StrictInt] = Field(default=None, description="Count is used only when the count mode is \"ExactCount\". Must be greater than zero. If AllocationMode is ExactCount and this field is not specified, the default is one.")
    device_class_name: StrictStr = Field(description="DeviceClassName references a specific DeviceClass, which can define additional configuration and selectors to be inherited by this request.  A class is required. Which classes are available depends on the cluster.  Administrators may use this to restrict which devices may get requested by only installing classes with selectors for permitted devices. If users are free to request anything without restrictions, then administrators can create an empty DeviceClass for users to reference.", alias="deviceClassName")
    name: StrictStr = Field(description="Name can be used to reference this request in a pod.spec.containers[].resources.claims entry and in a constraint of the claim.  Must be a DNS label.")
    selectors: Optional[List[V1alpha3DeviceSelector]] = Field(default=None, description="Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this request. All selectors must be satisfied for a device to be considered.")
    __properties: ClassVar[List[str]] = ["adminAccess", "allocationMode", "count", "deviceClassName", "name", "selectors"]

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
        """Create an instance of V1alpha3DeviceRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in selectors (list)
        _items = []
        if self.selectors:
            for _item_selectors in self.selectors:
                if _item_selectors:
                    _items.append(_item_selectors.to_dict())
            _dict['selectors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1alpha3DeviceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "adminAccess": obj.get("adminAccess"),
            "allocationMode": obj.get("allocationMode"),
            "count": obj.get("count"),
            "deviceClassName": obj.get("deviceClassName"),
            "name": obj.get("name"),
            "selectors": [V1alpha3DeviceSelector.from_dict(_item) for _item in obj["selectors"]] if obj.get("selectors") is not None else None
        })
        return _obj


