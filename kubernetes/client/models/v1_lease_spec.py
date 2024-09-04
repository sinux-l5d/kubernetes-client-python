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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class V1LeaseSpec(BaseModel):
    """
    LeaseSpec is a specification of a Lease.
    """ # noqa: E501
    acquire_time: Optional[datetime] = Field(default=None, description="acquireTime is a time when the current lease was acquired.", alias="acquireTime")
    holder_identity: Optional[StrictStr] = Field(default=None, description="holderIdentity contains the identity of the holder of a current lease. If Coordinated Leader Election is used, the holder identity must be equal to the elected LeaseCandidate.metadata.name field.", alias="holderIdentity")
    lease_duration_seconds: Optional[StrictInt] = Field(default=None, description="leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measured against the time of last observed renewTime.", alias="leaseDurationSeconds")
    lease_transitions: Optional[StrictInt] = Field(default=None, description="leaseTransitions is the number of transitions of a lease between holders.", alias="leaseTransitions")
    preferred_holder: Optional[StrictStr] = Field(default=None, description="PreferredHolder signals to a lease holder that the lease has a more optimal holder and should be given up. This field can only be set if Strategy is also set.", alias="preferredHolder")
    renew_time: Optional[datetime] = Field(default=None, description="renewTime is a time when the current holder of a lease has last updated the lease.", alias="renewTime")
    strategy: Optional[StrictStr] = Field(default=None, description="Strategy indicates the strategy for picking the leader for coordinated leader election. If the field is not specified, there is no active coordination for this lease. (Alpha) Using this field requires the CoordinatedLeaderElection feature gate to be enabled.")
    __properties: ClassVar[List[str]] = ["acquireTime", "holderIdentity", "leaseDurationSeconds", "leaseTransitions", "preferredHolder", "renewTime", "strategy"]

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
        """Create an instance of V1LeaseSpec from a JSON string"""
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
        """Create an instance of V1LeaseSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "acquireTime": obj.get("acquireTime"),
            "holderIdentity": obj.get("holderIdentity"),
            "leaseDurationSeconds": obj.get("leaseDurationSeconds"),
            "leaseTransitions": obj.get("leaseTransitions"),
            "preferredHolder": obj.get("preferredHolder"),
            "renewTime": obj.get("renewTime"),
            "strategy": obj.get("strategy")
        })
        return _obj


