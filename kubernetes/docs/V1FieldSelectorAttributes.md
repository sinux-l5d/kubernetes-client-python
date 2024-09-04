# V1FieldSelectorAttributes

FieldSelectorAttributes indicates a field limited access. Webhook authors are encouraged to * ensure rawSelector and requirements are not both set * consider the requirements field if set * not try to parse or consider the rawSelector field if set. This is to avoid another CVE-2022-2880 (i.e. getting different systems to agree on how exactly to parse a query is not something we want), see https://www.oxeye.io/resources/golang-parameter-smuggling-attack for more details. For the *SubjectAccessReview endpoints of the kube-apiserver: * If rawSelector is empty and requirements are empty, the request is not limited. * If rawSelector is present and requirements are empty, the rawSelector will be parsed and limited if the parsing succeeds. * If rawSelector is empty and requirements are present, the requirements should be honored * If rawSelector is present and requirements are present, the request is invalid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_selector** | **str** | rawSelector is the serialization of a field selector that would be included in a query parameter. Webhook implementations are encouraged to ignore rawSelector. The kube-apiserver&#39;s *SubjectAccessReview will parse the rawSelector as long as the requirements are not present. | [optional] 
**requirements** | [**List[V1FieldSelectorRequirement]**](V1FieldSelectorRequirement.md) | requirements is the parsed interpretation of a field selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood. | [optional] 

## Example

```python
from kubernetes.client.models.v1_field_selector_attributes import V1FieldSelectorAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of V1FieldSelectorAttributes from a JSON string
v1_field_selector_attributes_instance = V1FieldSelectorAttributes.from_json(json)
# print the JSON string representation of the object
print(V1FieldSelectorAttributes.to_json())

# convert the object into a dict
v1_field_selector_attributes_dict = v1_field_selector_attributes_instance.to_dict()
# create an instance of V1FieldSelectorAttributes from a dict
v1_field_selector_attributes_from_dict = V1FieldSelectorAttributes.from_dict(v1_field_selector_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


