# V1beta1ParentReference

ParentReference describes a reference to a parent object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | Group is the group of the object being referenced. | [optional] 
**name** | **str** | Name is the name of the object being referenced. | 
**namespace** | **str** | Namespace is the namespace of the object being referenced. | [optional] 
**resource** | **str** | Resource is the resource of the object being referenced. | 

## Example

```python
from kubernetes.client.models.v1beta1_parent_reference import V1beta1ParentReference

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ParentReference from a JSON string
v1beta1_parent_reference_instance = V1beta1ParentReference.from_json(json)
# print the JSON string representation of the object
print(V1beta1ParentReference.to_json())

# convert the object into a dict
v1beta1_parent_reference_dict = v1beta1_parent_reference_instance.to_dict()
# create an instance of V1beta1ParentReference from a dict
v1beta1_parent_reference_from_dict = V1beta1ParentReference.from_dict(v1beta1_parent_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


