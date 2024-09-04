# V1alpha3ResourceSliceSpec

ResourceSliceSpec contains the information published by the driver in one ResourceSlice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_nodes** | **bool** | AllNodes indicates that all nodes have access to the resources in the pool.  Exactly one of NodeName, NodeSelector and AllNodes must be set. | [optional] 
**devices** | [**List[V1alpha3Device]**](V1alpha3Device.md) | Devices lists some or all of the devices in this pool.  Must not have more than 128 entries. | [optional] 
**driver** | **str** | Driver identifies the DRA driver providing the capacity information. A field selector can be used to list only ResourceSlice objects with a certain driver name.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. This field is immutable. | 
**node_name** | **str** | NodeName identifies the node which provides the resources in this pool. A field selector can be used to list only ResourceSlice objects belonging to a certain node.  This field can be used to limit access from nodes to ResourceSlices with the same node name. It also indicates to autoscalers that adding new nodes of the same type as some old node might also make new resources available.  Exactly one of NodeName, NodeSelector and AllNodes must be set. This field is immutable. | [optional] 
**node_selector** | [**V1NodeSelector**](V1NodeSelector.md) |  | [optional] 
**pool** | [**V1alpha3ResourcePool**](V1alpha3ResourcePool.md) |  | 

## Example

```python
from kubernetes.client.models.v1alpha3_resource_slice_spec import V1alpha3ResourceSliceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3ResourceSliceSpec from a JSON string
v1alpha3_resource_slice_spec_instance = V1alpha3ResourceSliceSpec.from_json(json)
# print the JSON string representation of the object
print(V1alpha3ResourceSliceSpec.to_json())

# convert the object into a dict
v1alpha3_resource_slice_spec_dict = v1alpha3_resource_slice_spec_instance.to_dict()
# create an instance of V1alpha3ResourceSliceSpec from a dict
v1alpha3_resource_slice_spec_from_dict = V1alpha3ResourceSliceSpec.from_dict(v1alpha3_resource_slice_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


