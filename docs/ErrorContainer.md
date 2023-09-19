# ErrorContainer

An error response for an operation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[Error]**](Error.md) | The array of error entries associated with the error response | [optional] 
**trace** | **str** | The error trace information. | [optional] 

## Example

```python
from pytagbase.models.error_container import ErrorContainer

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorContainer from a JSON string
error_container_instance = ErrorContainer.from_json(json)
# print the JSON string representation of the object
print ErrorContainer.to_json()

# convert the object into a dict
error_container_dict = error_container_instance.to_dict()
# create an instance of ErrorContainer from a dict
error_container_form_dict = error_container.from_dict(error_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


