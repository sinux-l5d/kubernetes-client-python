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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kubernetes.client.models.v1_group_version_for_discovery import V1GroupVersionForDiscovery
from kubernetes.client.models.v1_server_address_by_client_cidr import V1ServerAddressByClientCIDR
from typing import Optional, Set
from typing_extensions import Self

class V1APIGroup(BaseModel):
    """
    APIGroup contains the name, the supported versions, and the preferred version of a group.
    """ # noqa: E501
    api_version: Optional[StrictStr] = Field(default=None, description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources", alias="apiVersion")
    kind: Optional[StrictStr] = Field(default=None, description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds")
    name: StrictStr = Field(description="name is the name of the group.")
    preferred_version: Optional[V1GroupVersionForDiscovery] = Field(default=None, alias="preferredVersion")
    server_address_by_client_cidrs: Optional[List[V1ServerAddressByClientCIDR]] = Field(default=None, description="a map of client CIDR to server address that is serving this group. This is to help clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the client can match. For example: the master will return an internal IP CIDR only, if the client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the client IP.", alias="serverAddressByClientCIDRs")
    versions: List[V1GroupVersionForDiscovery] = Field(description="versions are the versions supported in this group.")
    __properties: ClassVar[List[str]] = ["apiVersion", "kind", "name", "preferredVersion", "serverAddressByClientCIDRs", "versions"]

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
        """Create an instance of V1APIGroup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of preferred_version
        if self.preferred_version:
            _dict['preferredVersion'] = self.preferred_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in server_address_by_client_cidrs (list)
        _items = []
        if self.server_address_by_client_cidrs:
            for _item_server_address_by_client_cidrs in self.server_address_by_client_cidrs:
                if _item_server_address_by_client_cidrs:
                    _items.append(_item_server_address_by_client_cidrs.to_dict())
            _dict['serverAddressByClientCIDRs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in versions (list)
        _items = []
        if self.versions:
            for _item_versions in self.versions:
                if _item_versions:
                    _items.append(_item_versions.to_dict())
            _dict['versions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1APIGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "apiVersion": obj.get("apiVersion"),
            "kind": obj.get("kind"),
            "name": obj.get("name"),
            "preferredVersion": V1GroupVersionForDiscovery.from_dict(obj["preferredVersion"]) if obj.get("preferredVersion") is not None else None,
            "serverAddressByClientCIDRs": [V1ServerAddressByClientCIDR.from_dict(_item) for _item in obj["serverAddressByClientCIDRs"]] if obj.get("serverAddressByClientCIDRs") is not None else None,
            "versions": [V1GroupVersionForDiscovery.from_dict(_item) for _item in obj["versions"]] if obj.get("versions") is not None else None
        })
        return _obj


