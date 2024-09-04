# V1alpha3OpaqueDeviceConfiguration

OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver** | **str** | Driver is used to determine which kubelet plugin needs to be passed these configuration parameters.  An admission policy provided by the driver developer could use this to decide whether it needs to validate them.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. | 
**parameters** | **object** | Parameters can contain arbitrary data. It is the responsibility of the driver developer to handle validation and versioning. Typically this includes self-identification and a version (\&quot;kind\&quot; + \&quot;apiVersion\&quot; for Kubernetes types), with conversion between different versions. | 

## Example

```python
from kubernetes.client.models.v1alpha3_opaque_device_configuration import V1alpha3OpaqueDeviceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3OpaqueDeviceConfiguration from a JSON string
v1alpha3_opaque_device_configuration_instance = V1alpha3OpaqueDeviceConfiguration.from_json(json)
# print the JSON string representation of the object
print(V1alpha3OpaqueDeviceConfiguration.to_json())

# convert the object into a dict
v1alpha3_opaque_device_configuration_dict = v1alpha3_opaque_device_configuration_instance.to_dict()
# create an instance of V1alpha3OpaqueDeviceConfiguration from a dict
v1alpha3_opaque_device_configuration_from_dict = V1alpha3OpaqueDeviceConfiguration.from_dict(v1alpha3_opaque_device_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


