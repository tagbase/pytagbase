# Tags200

Response detailing all available unique tags and associated filename

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total count of unique tags | [optional] 
**tags** | [**List[Tag]**](Tag.md) | List of unique numeric Tag IDs and associated filename | [optional] 

## Example

```python
from pytagbase.models.tags200 import Tags200

# TODO update the JSON string below
json = "{}"
# create an instance of Tags200 from a JSON string
tags200_instance = Tags200.from_json(json)
# print the JSON string representation of the object
print Tags200.to_json()

# convert the object into a dict
tags200_dict = tags200_instance.to_dict()
# create an instance of Tags200 from a dict
tags200_form_dict = tags200.from_dict(tags200_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


