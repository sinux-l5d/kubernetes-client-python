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
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class VersionInfo(BaseModel):
    """
    Info contains versioning information. how we'll want to distribute that information.
    """ # noqa: E501
    build_date: StrictStr = Field(alias="buildDate")
    compiler: StrictStr
    git_commit: StrictStr = Field(alias="gitCommit")
    git_tree_state: StrictStr = Field(alias="gitTreeState")
    git_version: StrictStr = Field(alias="gitVersion")
    go_version: StrictStr = Field(alias="goVersion")
    major: StrictStr
    minor: StrictStr
    platform: StrictStr
    __properties: ClassVar[List[str]] = ["buildDate", "compiler", "gitCommit", "gitTreeState", "gitVersion", "goVersion", "major", "minor", "platform"]

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
        """Create an instance of VersionInfo from a JSON string"""
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
        """Create an instance of VersionInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "buildDate": obj.get("buildDate"),
            "compiler": obj.get("compiler"),
            "gitCommit": obj.get("gitCommit"),
            "gitTreeState": obj.get("gitTreeState"),
            "gitVersion": obj.get("gitVersion"),
            "goVersion": obj.get("goVersion"),
            "major": obj.get("major"),
            "minor": obj.get("minor"),
            "platform": obj.get("platform")
        })
        return _obj


