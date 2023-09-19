# TagSubmission


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **int** | The primary key from the Dataset relation | [optional] 
**date_time** | **str** | Local datetime stamp at the time of eTUFF tag data file ingestion | [optional] 
**filename** | **str** | Full name and extension of the ingested eTUFF tag data file | [optional] 
**hash_sha256** | **str** | SHA256 hash representing the contents of the submission eTUFF file | [optional] 
**metadata** | **Dict[str, str]** | Contains the ingested tag metadata consistent with the eTUFF specification | [optional] 
**notes** | **str** | Free-form text field where details of submitted eTUFF file for ingest can be provided e.g. submitter name, etuff data contents (tag metadata and measurements + primary position data, or just secondary solutionpositional meta/data) | [optional] 
**submission_id** | **int** | Unique numeric ID assigned upon submission of a tag eTUFF data file for ingest/importation into Tagbase | [optional] 
**tag_id** | **int** | Unique numeric Tag ID associated with the ingested tag eTUFF data file | [optional] 
**version** | **str** | Version identifier for the eTUFF tag data file ingested | [optional] 

## Example

```python
from pytagbase.models.tag_submission import TagSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of TagSubmission from a JSON string
tag_submission_instance = TagSubmission.from_json(json)
# print the JSON string representation of the object
print TagSubmission.to_json()

# convert the object into a dict
tag_submission_dict = tag_submission_instance.to_dict()
# create an instance of TagSubmission from a dict
tag_submission_form_dict = tag_submission.from_dict(tag_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


