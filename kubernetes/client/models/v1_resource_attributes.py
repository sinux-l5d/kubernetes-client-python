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
from kubernetes.client.models.v1_field_selector_attributes import V1FieldSelectorAttributes
from kubernetes.client.models.v1_label_selector_attributes import V1LabelSelectorAttributes
from typing import Optional, Set
from typing_extensions import Self

class V1ResourceAttributes(BaseModel):
    """
    ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface
    """ # noqa: E501
    field_selector: Optional[V1FieldSelectorAttributes] = Field(default=None, alias="fieldSelector")
    group: Optional[StrictStr] = Field(default=None, description="Group is the API Group of the Resource.  \"*\" means all.")
    label_selector: Optional[V1LabelSelectorAttributes] = Field(default=None, alias="labelSelector")
    name: Optional[StrictStr] = Field(default=None, description="Name is the name of the resource being requested for a \"get\" or deleted for a \"delete\". \"\" (empty) means all.")
    namespace: Optional[StrictStr] = Field(default=None, description="Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces \"\" (empty) is defaulted for LocalSubjectAccessReviews \"\" (empty) is empty for cluster-scoped resources \"\" (empty) means \"all\" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview")
    resource: Optional[StrictStr] = Field(default=None, description="Resource is one of the existing resource types.  \"*\" means all.")
    subresource: Optional[StrictStr] = Field(default=None, description="Subresource is one of the existing resource types.  \"\" means none.")
    verb: Optional[StrictStr] = Field(default=None, description="Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  \"*\" means all.")
    version: Optional[StrictStr] = Field(default=None, description="Version is the API Version of the Resource.  \"*\" means all.")
    __properties: ClassVar[List[str]] = ["fieldSelector", "group", "labelSelector", "name", "namespace", "resource", "subresource", "verb", "version"]

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
        """Create an instance of V1ResourceAttributes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of field_selector
        if self.field_selector:
            _dict['fieldSelector'] = self.field_selector.to_dict()
        # override the default output from pydantic by calling `to_dict()` of label_selector
        if self.label_selector:
            _dict['labelSelector'] = self.label_selector.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1ResourceAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fieldSelector": V1FieldSelectorAttributes.from_dict(obj["fieldSelector"]) if obj.get("fieldSelector") is not None else None,
            "group": obj.get("group"),
            "labelSelector": V1LabelSelectorAttributes.from_dict(obj["labelSelector"]) if obj.get("labelSelector") is not None else None,
            "name": obj.get("name"),
            "namespace": obj.get("namespace"),
            "resource": obj.get("resource"),
            "subresource": obj.get("subresource"),
            "verb": obj.get("verb"),
            "version": obj.get("version")
        })
        return _obj


