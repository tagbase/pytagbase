# Ingest200

HTTP 200 success response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | HTTP status code | [optional] 
**elapsed** | **str** | Elapsed time for the operation | [optional] 
**message** | **str** | A string detailing specifics of an HTTP operation | [optional] 

## Example

```python
from pytagbase.models.ingest200 import Ingest200

# TODO update the JSON string below
json = "{}"
# create an instance of Ingest200 from a JSON string
ingest200_instance = Ingest200.from_json(json)
# print the JSON string representation of the object
print Ingest200.to_json()

# convert the object into a dict
ingest200_dict = ingest200_instance.to_dict()
# create an instance of Ingest200 from a dict
ingest200_form_dict = ingest200.from_dict(ingest200_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


