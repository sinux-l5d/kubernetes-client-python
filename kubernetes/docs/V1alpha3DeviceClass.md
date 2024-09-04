# V1alpha3DeviceClass

DeviceClass is a vendor- or admin-provided resource that contains device configuration and selectors. It can be referenced in the device requests of a claim to apply these presets. Cluster scoped.  This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1alpha3DeviceClassSpec**](V1alpha3DeviceClassSpec.md) |  | 

## Example

```python
from kubernetes.client.models.v1alpha3_device_class import V1alpha3DeviceClass

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3DeviceClass from a JSON string
v1alpha3_device_class_instance = V1alpha3DeviceClass.from_json(json)
# print the JSON string representation of the object
print(V1alpha3DeviceClass.to_json())

# convert the object into a dict
v1alpha3_device_class_dict = v1alpha3_device_class_instance.to_dict()
# create an instance of V1alpha3DeviceClass from a dict
v1alpha3_device_class_from_dict = V1alpha3DeviceClass.from_dict(v1alpha3_device_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


