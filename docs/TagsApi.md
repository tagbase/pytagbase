# pytagbase.TagsApi

All URIs are relative to *https://localhost/tagbase/api/v0.14.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sub**](TagsApi.md#delete_sub) | **DELETE** /tags/{tag_id}/subs/{sub_id} | Delete a tag submission
[**delete_tag**](TagsApi.md#delete_tag) | **DELETE** /tags/{tag_id} | Delete an individual tag
[**delete_tags**](TagsApi.md#delete_tags) | **DELETE** /tags | Delete all tags
[**get_tag**](TagsApi.md#get_tag) | **GET** /tags/{tag_id} | Get information about an individual tag
[**list_tags**](TagsApi.md#list_tags) | **GET** /tags | Get information about all tags
[**replace_tag**](TagsApi.md#replace_tag) | **PUT** /tags/{tag_id}/subs/{sub_id} | Update the &#39;notes&#39; and/or &#39;version&#39; associated with a tag submission


# **delete_sub**
> delete_sub(sub_id, tag_id)

Delete a tag submission

Delete a tag submission

### Example

```python
import time
import os
import pytagbase
from pytagbase.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/tagbase/api/v0.14.0
# See configuration.py for a list of all supported configuration parameters.
configuration = pytagbase.Configuration(
    host = "https://localhost/tagbase/api/v0.14.0"
)


# Enter a context with an instance of the API client
with pytagbase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pytagbase.TagsApi(api_client)
    sub_id = 56 # int | Existing submission id for an existing tag
    tag_id = 56 # int | Existing tag id

    try:
        # Delete a tag submission
        api_instance.delete_sub(sub_id, tag_id)
    except Exception as e:
        print("Exception when calling TagsApi->delete_sub: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **int**| Existing submission id for an existing tag | 
 **tag_id** | **int**| Existing tag id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful delete operation. |  -  |
**500** | Internal tagbase-server error. Contact admin detailed in openapi.yaml. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(tag_id)

Delete an individual tag

Delete an individual tag

### Example

```python
import time
import os
import pytagbase
from pytagbase.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/tagbase/api/v0.14.0
# See configuration.py for a list of all supported configuration parameters.
configuration = pytagbase.Configuration(
    host = "https://localhost/tagbase/api/v0.14.0"
)


# Enter a context with an instance of the API client
with pytagbase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pytagbase.TagsApi(api_client)
    tag_id = 56 # int | Existing tag id

    try:
        # Delete an individual tag
        api_instance.delete_tag(tag_id)
    except Exception as e:
        print("Exception when calling TagsApi->delete_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **int**| Existing tag id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful delete operation. |  -  |
**500** | Internal tagbase-server error. Contact admin detailed in openapi.yaml. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tags**
> delete_tags()

Delete all tags

Delete all tags

### Example

```python
import time
import os
import pytagbase
from pytagbase.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/tagbase/api/v0.14.0
# See configuration.py for a list of all supported configuration parameters.
configuration = pytagbase.Configuration(
    host = "https://localhost/tagbase/api/v0.14.0"
)


# Enter a context with an instance of the API client
with pytagbase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pytagbase.TagsApi(api_client)

    try:
        # Delete all tags
        api_instance.delete_tags()
    except Exception as e:
        print("Exception when calling TagsApi->delete_tags: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful delete operation. |  -  |
**500** | Internal tagbase-server error. Contact admin detailed in openapi.yaml. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag**
> Tag200 get_tag(tag_id)

Get information about an individual tag

Get information about an individual tag

### Example

```python
import time
import os
import pytagbase
from pytagbase.models.tag200 import Tag200
from pytagbase.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/tagbase/api/v0.14.0
# See configuration.py for a list of all supported configuration parameters.
configuration = pytagbase.Configuration(
    host = "https://localhost/tagbase/api/v0.14.0"
)


# Enter a context with an instance of the API client
with pytagbase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pytagbase.TagsApi(api_client)
    tag_id = 56 # int | Existing tag id

    try:
        # Get information about an individual tag
        api_response = api_instance.get_tag(tag_id)
        print("The response of TagsApi->get_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->get_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **int**| Existing tag id | 

### Return type

[**Tag200**](Tag200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A success message confirming ingestion. |  -  |
**500** | Internal tagbase-server error. Contact admin detailed in openapi.yaml. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags**
> Tags200 list_tags()

Get information about all tags

Get information about all tags

### Example

```python
import time
import os
import pytagbase
from pytagbase.models.tags200 import Tags200
from pytagbase.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/tagbase/api/v0.14.0
# See configuration.py for a list of all supported configuration parameters.
configuration = pytagbase.Configuration(
    host = "https://localhost/tagbase/api/v0.14.0"
)


# Enter a context with an instance of the API client
with pytagbase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pytagbase.TagsApi(api_client)

    try:
        # Get information about all tags
        api_response = api_instance.list_tags()
        print("The response of TagsApi->list_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->list_tags: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Tags200**](Tags200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A success message confirming ingestion. |  -  |
**500** | Internal tagbase-server error. Contact admin detailed in openapi.yaml. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_tag**
> TagPut200 replace_tag(sub_id, tag_id, notes=notes, version=version)

Update the 'notes' and/or 'version' associated with a tag submission

Update a tag submission

### Example

```python
import time
import os
import pytagbase
from pytagbase.models.tag_put200 import TagPut200
from pytagbase.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/tagbase/api/v0.14.0
# See configuration.py for a list of all supported configuration parameters.
configuration = pytagbase.Configuration(
    host = "https://localhost/tagbase/api/v0.14.0"
)


# Enter a context with an instance of the API client
with pytagbase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pytagbase.TagsApi(api_client)
    sub_id = 56 # int | Existing submission id for an existing tag
    tag_id = 56 # int | Existing tag id
    notes = 'notes_example' # str | Free-form text field where details of submitted eTUFF file for ingest can be provided e.g. submitter name, etuff data contents (tag metadata and measurements + primary position data, or just secondary solution-positional meta/data) (optional)
    version = 'version_example' # str | Version identifier for the eTUFF tag data file ingested (optional)

    try:
        # Update the 'notes' and/or 'version' associated with a tag submission
        api_response = api_instance.replace_tag(sub_id, tag_id, notes=notes, version=version)
        print("The response of TagsApi->replace_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->replace_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **int**| Existing submission id for an existing tag | 
 **tag_id** | **int**| Existing tag id | 
 **notes** | **str**| Free-form text field where details of submitted eTUFF file for ingest can be provided e.g. submitter name, etuff data contents (tag metadata and measurements + primary position data, or just secondary solution-positional meta/data) | [optional] 
 **version** | **str**| Version identifier for the eTUFF tag data file ingested | [optional] 

### Return type

[**TagPut200**](TagPut200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A success message confirming ingestion. |  -  |
**500** | Internal tagbase-server error. Contact admin detailed in openapi.yaml. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

