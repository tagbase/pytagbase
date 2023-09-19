# Tag

Unique numeric Tag ID associated with the ingested tag eTUFF data file

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_id** | **int** | Unique numeric Tag ID associated with the ingested tag eTUFF data file | [optional] 
**filename** | **str** | Full name and extension of the ingested eTUFF tag data file | [optional] 

## Example

```python
from pytagbase.models.tag import Tag

# TODO update the JSON string below
json = "{}"
# create an instance of Tag from a JSON string
tag_instance = Tag.from_json(json)
# print the JSON string representation of the object
print Tag.to_json()

# convert the object into a dict
tag_dict = tag_instance.to_dict()
# create an instance of Tag from a dict
tag_form_dict = tag.from_dict(tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


