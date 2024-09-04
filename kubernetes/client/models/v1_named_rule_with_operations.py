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
from typing import Optional, Set
from typing_extensions import Self

class V1NamedRuleWithOperations(BaseModel):
    """
    NamedRuleWithOperations is a tuple of Operations and Resources with ResourceNames.
    """ # noqa: E501
    api_groups: Optional[List[StrictStr]] = Field(default=None, description="APIGroups is the API groups the resources belong to. '*' is all groups. If '*' is present, the length of the slice must be one. Required.", alias="apiGroups")
    api_versions: Optional[List[StrictStr]] = Field(default=None, description="APIVersions is the API versions the resources belong to. '*' is all versions. If '*' is present, the length of the slice must be one. Required.", alias="apiVersions")
    operations: Optional[List[StrictStr]] = Field(default=None, description="Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added. If '*' is present, the length of the slice must be one. Required.")
    resource_names: Optional[List[StrictStr]] = Field(default=None, description="ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.", alias="resourceNames")
    resources: Optional[List[StrictStr]] = Field(default=None, description="Resources is a list of resources this rule applies to.  For example: 'pods' means pods. 'pods/log' means the log subresource of pods. '*' means all resources, but not subresources. 'pods/*' means all subresources of pods. '*/scale' means all scale subresources. '*/*' means all resources and their subresources.  If wildcard is present, the validation rule will ensure resources do not overlap with each other.  Depending on the enclosing object, subresources might not be allowed. Required.")
    scope: Optional[StrictStr] = Field(default=None, description="scope specifies the scope of this rule. Valid values are \"Cluster\", \"Namespaced\", and \"*\" \"Cluster\" means that only cluster-scoped resources will match this rule. Namespace API objects are cluster-scoped. \"Namespaced\" means that only namespaced resources will match this rule. \"*\" means that there are no scope restrictions. Subresources match the scope of their parent resource. Default is \"*\".")
    __properties: ClassVar[List[str]] = ["apiGroups", "apiVersions", "operations", "resourceNames", "resources", "scope"]

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
        """Create an instance of V1NamedRuleWithOperations from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1NamedRuleWithOperations from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "apiGroups": obj.get("apiGroups"),
            "apiVersions": obj.get("apiVersions"),
            "operations": obj.get("operations"),
            "resourceNames": obj.get("resourceNames"),
            "resources": obj.get("resources"),
            "scope": obj.get("scope")
        })
        return _obj


