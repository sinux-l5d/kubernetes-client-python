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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kubernetes.client.models.storage_v1_token_request import StorageV1TokenRequest
from typing import Optional, Set
from typing_extensions import Self

class V1CSIDriverSpec(BaseModel):
    """
    CSIDriverSpec is the specification of a CSIDriver.
    """ # noqa: E501
    attach_required: Optional[StrictBool] = Field(default=None, description="attachRequired indicates this CSI volume driver requires an attach operation (because it implements the CSI ControllerPublishVolume() method), and that the Kubernetes attach detach controller should call the attach volume interface which checks the volumeattachment status and waits until the volume is attached before proceeding to mounting. The CSI external-attacher coordinates with CSI volume driver and updates the volumeattachment status when the attach operation is complete. If the CSIDriverRegistry feature gate is enabled and the value is specified to false, the attach operation will be skipped. Otherwise the attach operation will be called.  This field is immutable.", alias="attachRequired")
    fs_group_policy: Optional[StrictStr] = Field(default=None, description="fsGroupPolicy defines if the underlying volume supports changing ownership and permission of the volume before being mounted. Refer to the specific FSGroupPolicy values for additional details.  This field was immutable in Kubernetes < 1.29 and now is mutable.  Defaults to ReadWriteOnceWithFSType, which will examine each volume to determine if Kubernetes should modify ownership and permissions of the volume. With the default policy the defined fsGroup will only be applied if a fstype is defined and the volume's access mode contains ReadWriteOnce.", alias="fsGroupPolicy")
    pod_info_on_mount: Optional[StrictBool] = Field(default=None, description="podInfoOnMount indicates this CSI volume driver requires additional pod information (like podName, podUID, etc.) during mount operations, if set to true. If set to false, pod information will not be passed on mount. Default is false.  The CSI driver specifies podInfoOnMount as part of driver deployment. If true, Kubelet will pass pod information as VolumeContext in the CSI NodePublishVolume() calls. The CSI driver is responsible for parsing and validating the information passed in as VolumeContext.  The following VolumeContext will be passed if podInfoOnMount is set to true. This list might grow, but the prefix will be used. \"csi.storage.k8s.io/pod.name\": pod.Name \"csi.storage.k8s.io/pod.namespace\": pod.Namespace \"csi.storage.k8s.io/pod.uid\": string(pod.UID) \"csi.storage.k8s.io/ephemeral\": \"true\" if the volume is an ephemeral inline volume                                 defined by a CSIVolumeSource, otherwise \"false\"  \"csi.storage.k8s.io/ephemeral\" is a new feature in Kubernetes 1.16. It is only required for drivers which support both the \"Persistent\" and \"Ephemeral\" VolumeLifecycleMode. Other drivers can leave pod info disabled and/or ignore this field. As Kubernetes 1.15 doesn't support this field, drivers can only support one mode when deployed on such a cluster and the deployment determines which mode that is, for example via a command line parameter of the driver.  This field was immutable in Kubernetes < 1.29 and now is mutable.", alias="podInfoOnMount")
    requires_republish: Optional[StrictBool] = Field(default=None, description="requiresRepublish indicates the CSI driver wants `NodePublishVolume` being periodically called to reflect any possible change in the mounted volume. This field defaults to false.  Note: After a successful initial NodePublishVolume call, subsequent calls to NodePublishVolume should only update the contents of the volume. New mount points will not be seen by a running container.", alias="requiresRepublish")
    se_linux_mount: Optional[StrictBool] = Field(default=None, description="seLinuxMount specifies if the CSI driver supports \"-o context\" mount option.  When \"true\", the CSI driver must ensure that all volumes provided by this CSI driver can be mounted separately with different `-o context` options. This is typical for storage backends that provide volumes as filesystems on block devices or as independent shared volumes. Kubernetes will call NodeStage / NodePublish with \"-o context=xyz\" mount option when mounting a ReadWriteOncePod volume used in Pod that has explicitly set SELinux context. In the future, it may be expanded to other volume AccessModes. In any case, Kubernetes will ensure that the volume is mounted only with a single SELinux context.  When \"false\", Kubernetes won't pass any special SELinux mount options to the driver. This is typical for volumes that represent subdirectories of a bigger shared filesystem.  Default is \"false\".", alias="seLinuxMount")
    storage_capacity: Optional[StrictBool] = Field(default=None, description="storageCapacity indicates that the CSI volume driver wants pod scheduling to consider the storage capacity that the driver deployment will report by creating CSIStorageCapacity objects with capacity information, if set to true.  The check can be enabled immediately when deploying a driver. In that case, provisioning new volumes with late binding will pause until the driver deployment has published some suitable CSIStorageCapacity object.  Alternatively, the driver can be deployed with the field unset or false and it can be flipped later when storage capacity information has been published.  This field was immutable in Kubernetes <= 1.22 and now is mutable.", alias="storageCapacity")
    token_requests: Optional[List[StorageV1TokenRequest]] = Field(default=None, description="tokenRequests indicates the CSI driver needs pods' service account tokens it is mounting volume for to do necessary authentication. Kubelet will pass the tokens in VolumeContext in the CSI NodePublishVolume calls. The CSI driver should parse and validate the following VolumeContext: \"csi.storage.k8s.io/serviceAccount.tokens\": {   \"<audience>\": {     \"token\": <token>,     \"expirationTimestamp\": <expiration timestamp in RFC3339>,   },   ... }  Note: Audience in each TokenRequest should be different and at most one token is empty string. To receive a new token after expiry, RequiresRepublish can be used to trigger NodePublishVolume periodically.", alias="tokenRequests")
    volume_lifecycle_modes: Optional[List[StrictStr]] = Field(default=None, description="volumeLifecycleModes defines what kind of volumes this CSI volume driver supports. The default if the list is empty is \"Persistent\", which is the usage defined by the CSI specification and implemented in Kubernetes via the usual PV/PVC mechanism.  The other mode is \"Ephemeral\". In this mode, volumes are defined inline inside the pod spec with CSIVolumeSource and their lifecycle is tied to the lifecycle of that pod. A driver has to be aware of this because it is only going to get a NodePublishVolume call for such a volume.  For more information about implementing this mode, see https://kubernetes-csi.github.io/docs/ephemeral-local-volumes.html A driver can support one or more of these modes and more modes may be added in the future.  This field is beta. This field is immutable.", alias="volumeLifecycleModes")
    __properties: ClassVar[List[str]] = ["attachRequired", "fsGroupPolicy", "podInfoOnMount", "requiresRepublish", "seLinuxMount", "storageCapacity", "tokenRequests", "volumeLifecycleModes"]

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
        """Create an instance of V1CSIDriverSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in token_requests (list)
        _items = []
        if self.token_requests:
            for _item_token_requests in self.token_requests:
                if _item_token_requests:
                    _items.append(_item_token_requests.to_dict())
            _dict['tokenRequests'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1CSIDriverSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attachRequired": obj.get("attachRequired"),
            "fsGroupPolicy": obj.get("fsGroupPolicy"),
            "podInfoOnMount": obj.get("podInfoOnMount"),
            "requiresRepublish": obj.get("requiresRepublish"),
            "seLinuxMount": obj.get("seLinuxMount"),
            "storageCapacity": obj.get("storageCapacity"),
            "tokenRequests": [StorageV1TokenRequest.from_dict(_item) for _item in obj["tokenRequests"]] if obj.get("tokenRequests") is not None else None,
            "volumeLifecycleModes": obj.get("volumeLifecycleModes")
        })
        return _obj


