# V1TypeChecking

TypeChecking contains results of type checking the expressions in the ValidatingAdmissionPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression_warnings** | [**List[V1ExpressionWarning]**](V1ExpressionWarning.md) | The type checking warnings for each expression. | [optional] 

## Example

```python
from kubernetes.client.models.v1_type_checking import V1TypeChecking

# TODO update the JSON string below
json = "{}"
# create an instance of V1TypeChecking from a JSON string
v1_type_checking_instance = V1TypeChecking.from_json(json)
# print the JSON string representation of the object
print(V1TypeChecking.to_json())

# convert the object into a dict
v1_type_checking_dict = v1_type_checking_instance.to_dict()
# create an instance of V1TypeChecking from a dict
v1_type_checking_from_dict = V1TypeChecking.from_dict(v1_type_checking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


