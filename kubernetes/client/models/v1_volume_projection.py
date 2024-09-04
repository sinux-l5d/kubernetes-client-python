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
from typing import Any, ClassVar, Dict, List, Optional
from kubernetes.client.models.v1_cluster_trust_bundle_projection import V1ClusterTrustBundleProjection
from kubernetes.client.models.v1_config_map_projection import V1ConfigMapProjection
from kubernetes.client.models.v1_downward_api_projection import V1DownwardAPIProjection
from kubernetes.client.models.v1_secret_projection import V1SecretProjection
from kubernetes.client.models.v1_service_account_token_projection import V1ServiceAccountTokenProjection
from typing import Optional, Set
from typing_extensions import Self

class V1VolumeProjection(BaseModel):
    """
    Projection that may be projected along with other supported volume types. Exactly one of these fields must be set.
    """ # noqa: E501
    cluster_trust_bundle: Optional[V1ClusterTrustBundleProjection] = Field(default=None, alias="clusterTrustBundle")
    config_map: Optional[V1ConfigMapProjection] = Field(default=None, alias="configMap")
    downward_api: Optional[V1DownwardAPIProjection] = Field(default=None, alias="downwardAPI")
    secret: Optional[V1SecretProjection] = None
    service_account_token: Optional[V1ServiceAccountTokenProjection] = Field(default=None, alias="serviceAccountToken")
    __properties: ClassVar[List[str]] = ["clusterTrustBundle", "configMap", "downwardAPI", "secret", "serviceAccountToken"]

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
        """Create an instance of V1VolumeProjection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cluster_trust_bundle
        if self.cluster_trust_bundle:
            _dict['clusterTrustBundle'] = self.cluster_trust_bundle.to_dict()
        # override the default output from pydantic by calling `to_dict()` of config_map
        if self.config_map:
            _dict['configMap'] = self.config_map.to_dict()
        # override the default output from pydantic by calling `to_dict()` of downward_api
        if self.downward_api:
            _dict['downwardAPI'] = self.downward_api.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secret
        if self.secret:
            _dict['secret'] = self.secret.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_account_token
        if self.service_account_token:
            _dict['serviceAccountToken'] = self.service_account_token.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1VolumeProjection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterTrustBundle": V1ClusterTrustBundleProjection.from_dict(obj["clusterTrustBundle"]) if obj.get("clusterTrustBundle") is not None else None,
            "configMap": V1ConfigMapProjection.from_dict(obj["configMap"]) if obj.get("configMap") is not None else None,
            "downwardAPI": V1DownwardAPIProjection.from_dict(obj["downwardAPI"]) if obj.get("downwardAPI") is not None else None,
            "secret": V1SecretProjection.from_dict(obj["secret"]) if obj.get("secret") is not None else None,
            "serviceAccountToken": V1ServiceAccountTokenProjection.from_dict(obj["serviceAccountToken"]) if obj.get("serviceAccountToken") is not None else None
        })
        return _obj


