# pytagbase.IngestApi

All URIs are relative to *https://localhost/tagbase/api/v0.14.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingest_get**](IngestApi.md#ingest_get) | **GET** /ingest | Get network accessible file and execute ingestion
[**ingest_post**](IngestApi.md#ingest_post) | **POST** /ingest | Post a local file and perform a ingest operation


# **ingest_get**
> Ingest200 ingest_get(file, notes=notes, type=type, version=version)

Get network accessible file and execute ingestion

Get network accessible file and execute ingestion

### Example

```python
import time
import os
import pytagbase
from pytagbase.models.ingest200 import Ingest200
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
    api_instance = pytagbase.IngestApi(api_client)
    file = 'file_example' # str | Location of a network accessible (file, ftp, http, https) file e.g. 'file:///usr/src/app/data/eTUFF-sailfish-117259.txt'.
    notes = 'notes_example' # str | Free-form text field where details of submitted eTUFF file for ingest can be provided e.g. submitter name, etuff data contents (tag metadata and measurements + primary position data, or just secondary solution-positional meta/data) (optional)
    type = 'etuff' # str | Type of file to be ingested, defaults to 'etuff' (optional) (default to 'etuff')
    version = 'version_example' # str | Version identifier for the eTUFF tag data file ingested (optional)

    try:
        # Get network accessible file and execute ingestion
        api_response = api_instance.ingest_get(file, notes=notes, type=type, version=version)
        print("The response of IngestApi->ingest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IngestApi->ingest_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**| Location of a network accessible (file, ftp, http, https) file e.g. &#39;file:///usr/src/app/data/eTUFF-sailfish-117259.txt&#39;. | 
 **notes** | **str**| Free-form text field where details of submitted eTUFF file for ingest can be provided e.g. submitter name, etuff data contents (tag metadata and measurements + primary position data, or just secondary solution-positional meta/data) | [optional] 
 **type** | **str**| Type of file to be ingested, defaults to &#39;etuff&#39; | [optional] [default to &#39;etuff&#39;]
 **version** | **str**| Version identifier for the eTUFF tag data file ingested | [optional] 

### Return type

[**Ingest200**](Ingest200.md)

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

# **ingest_post**
> Ingest200 ingest_post(filename, body, notes=notes, type=type, version=version)

Post a local file and perform a ingest operation

Post a local file and perform a ingest operation

### Example

```python
import time
import os
import pytagbase
from pytagbase.models.ingest200 import Ingest200
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
    api_instance = pytagbase.IngestApi(api_client)
    filename = 'filename_example' # str | Free-form text field to explicitly define the name of the file to be persisted
    body = None # bytearray | 
    notes = 'notes_example' # str | Free-form text field where details of submitted eTUFF file for ingest can be provided e.g. submitter name, etuff data contents (tag metadata and measurements + primary position data, or just secondary solution-positional meta/data) (optional)
    type = 'etuff' # str | Type of file to be ingested, defaults to 'etuff' (optional) (default to 'etuff')
    version = 'version_example' # str | Version identifier for the eTUFF tag data file ingested (optional)

    try:
        # Post a local file and perform a ingest operation
        api_response = api_instance.ingest_post(filename, body, notes=notes, type=type, version=version)
        print("The response of IngestApi->ingest_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IngestApi->ingest_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Free-form text field to explicitly define the name of the file to be persisted | 
 **body** | **bytearray**|  | 
 **notes** | **str**| Free-form text field where details of submitted eTUFF file for ingest can be provided e.g. submitter name, etuff data contents (tag metadata and measurements + primary position data, or just secondary solution-positional meta/data) | [optional] 
 **type** | **str**| Type of file to be ingested, defaults to &#39;etuff&#39; | [optional] [default to &#39;etuff&#39;]
 **version** | **str**| Version identifier for the eTUFF tag data file ingested | [optional] 

### Return type

[**Ingest200**](Ingest200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream, text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A success message confirming ingestion. |  -  |
**500** | Internal tagbase-server error. Contact admin detailed in openapi.yaml. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

