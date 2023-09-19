# TagPut200

HTTP 200 success response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | HTTP status code | [optional] 
**message** | **str** | A string detailing specifics of an HTTP operation | [optional] 

## Example

```python
from pytagbase.models.tag_put200 import TagPut200

# TODO update the JSON string below
json = "{}"
# create an instance of TagPut200 from a JSON string
tag_put200_instance = TagPut200.from_json(json)
# print the JSON string representation of the object
print TagPut200.to_json()

# convert the object into a dict
tag_put200_dict = tag_put200_instance.to_dict()
# create an instance of TagPut200 from a dict
tag_put200_form_dict = tag_put200.from_dict(tag_put200_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


