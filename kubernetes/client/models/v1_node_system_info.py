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

class V1NodeSystemInfo(BaseModel):
    """
    NodeSystemInfo is a set of ids/uuids to uniquely identify the node.
    """ # noqa: E501
    architecture: StrictStr = Field(description="The Architecture reported by the node")
    boot_id: StrictStr = Field(description="Boot ID reported by the node.", alias="bootID")
    container_runtime_version: StrictStr = Field(description="ContainerRuntime Version reported by the node through runtime remote API (e.g. containerd://1.4.2).", alias="containerRuntimeVersion")
    kernel_version: StrictStr = Field(description="Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64).", alias="kernelVersion")
    kube_proxy_version: StrictStr = Field(description="Deprecated: KubeProxy Version reported by the node.", alias="kubeProxyVersion")
    kubelet_version: StrictStr = Field(description="Kubelet Version reported by the node.", alias="kubeletVersion")
    machine_id: StrictStr = Field(description="MachineID reported by the node. For unique machine identification in the cluster this field is preferred. Learn more from man(5) machine-id: http://man7.org/linux/man-pages/man5/machine-id.5.html", alias="machineID")
    operating_system: StrictStr = Field(description="The Operating System reported by the node", alias="operatingSystem")
    os_image: StrictStr = Field(description="OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)).", alias="osImage")
    system_uuid: StrictStr = Field(description="SystemUUID reported by the node. For unique machine identification MachineID is preferred. This field is specific to Red Hat hosts https://access.redhat.com/documentation/en-us/red_hat_subscription_management/1/html/rhsm/uuid", alias="systemUUID")
    __properties: ClassVar[List[str]] = ["architecture", "bootID", "containerRuntimeVersion", "kernelVersion", "kubeProxyVersion", "kubeletVersion", "machineID", "operatingSystem", "osImage", "systemUUID"]

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
        """Create an instance of V1NodeSystemInfo from a JSON string"""
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
        """Create an instance of V1NodeSystemInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "architecture": obj.get("architecture"),
            "bootID": obj.get("bootID"),
            "containerRuntimeVersion": obj.get("containerRuntimeVersion"),
            "kernelVersion": obj.get("kernelVersion"),
            "kubeProxyVersion": obj.get("kubeProxyVersion"),
            "kubeletVersion": obj.get("kubeletVersion"),
            "machineID": obj.get("machineID"),
            "operatingSystem": obj.get("operatingSystem"),
            "osImage": obj.get("osImage"),
            "systemUUID": obj.get("systemUUID")
        })
        return _obj


