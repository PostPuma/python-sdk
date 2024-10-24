# PostPuma.MediaApi

All URIs are relative to *https://app.postpuma.com/app/5afgg2-1egj4n-7612ng-g313ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_media_files**](MediaApi.md#delete_media_files) | **DELETE** /media | Delete media files
[**get_media_file**](MediaApi.md#get_media_file) | **GET** /media/{mediaUuid} | Get media file
[**list_media_files**](MediaApi.md#list_media_files) | **GET** /media | List media files
[**upload_media_file**](MediaApi.md#upload_media_file) | **POST** /media | Upload media file


# **delete_media_files**
> DeleteMediaFiles200Response delete_media_files(delete_media_files_request=delete_media_files_request)

Delete media files

Delete media files

### Example

* Bearer Authentication (bearerAuth):

```python
import PostPuma
from PostPuma.models.delete_media_files200_response import DeleteMediaFiles200Response
from PostPuma.models.delete_media_files_request import DeleteMediaFilesRequest
from PostPuma.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.postpuma.com/app/5afgg2-1egj4n-7612ng-g313ie
# See configuration.py for a list of all supported configuration parameters.
configuration = PostPuma.Configuration(
    host = "https://app.postpuma.com/app/5afgg2-1egj4n-7612ng-g313ie"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = PostPuma.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PostPuma.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PostPuma.MediaApi(api_client)
    delete_media_files_request = PostPuma.DeleteMediaFilesRequest() # DeleteMediaFilesRequest |  (optional)

    try:
        # Delete media files
        api_response = api_instance.delete_media_files(delete_media_files_request=delete_media_files_request)
        print("The response of MediaApi->delete_media_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->delete_media_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_media_files_request** | [**DeleteMediaFilesRequest**](DeleteMediaFilesRequest.md)|  | [optional] 

### Return type

[**DeleteMediaFiles200Response**](DeleteMediaFiles200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthenticated. |  -  |
**403** | Access forbidden. |  -  |
**404** | Workspace not found. |  -  |
**422** | Validation errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_file**
> MediaFile get_media_file(media_uuid)

Get media file

Get media file

### Example

* Bearer Authentication (bearerAuth):

```python
import PostPuma
from PostPuma.models.media_file import MediaFile
from PostPuma.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.postpuma.com/app/5afgg2-1egj4n-7612ng-g313ie
# See configuration.py for a list of all supported configuration parameters.
configuration = PostPuma.Configuration(
    host = "https://app.postpuma.com/app/5afgg2-1egj4n-7612ng-g313ie"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = PostPuma.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PostPuma.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PostPuma.MediaApi(api_client)
    media_uuid = 'media_uuid_example' # str | Media UUID

    try:
        # Get media file
        api_response = api_instance.get_media_file(media_uuid)
        print("The response of MediaApi->get_media_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->get_media_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_uuid** | **str**| Media UUID | 

### Return type

[**MediaFile**](MediaFile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthenticated. |  -  |
**403** | Access forbidden. |  -  |
**404** | Workspace not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_media_files**
> ListMediaFiles200Response list_media_files(page=page)

List media files

List media files

### Example

* Bearer Authentication (bearerAuth):

```python
import PostPuma
from PostPuma.models.list_media_files200_response import ListMediaFiles200Response
from PostPuma.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.postpuma.com/app/5afgg2-1egj4n-7612ng-g313ie
# See configuration.py for a list of all supported configuration parameters.
configuration = PostPuma.Configuration(
    host = "https://app.postpuma.com/app/5afgg2-1egj4n-7612ng-g313ie"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = PostPuma.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PostPuma.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PostPuma.MediaApi(api_client)
    page = 56 # int | Page number (optional)

    try:
        # List media files
        api_response = api_instance.list_media_files(page=page)
        print("The response of MediaApi->list_media_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->list_media_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 

### Return type

[**ListMediaFiles200Response**](ListMediaFiles200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthenticated. |  -  |
**403** | Access forbidden. |  -  |
**404** | Workspace not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_media_file**
> MediaFile upload_media_file(file=file)

Upload media file

Upload media file

### Example

* Bearer Authentication (bearerAuth):

```python
import PostPuma
from PostPuma.models.media_file import MediaFile
from PostPuma.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.postpuma.com/app/5afgg2-1egj4n-7612ng-g313ie
# See configuration.py for a list of all supported configuration parameters.
configuration = PostPuma.Configuration(
    host = "https://app.postpuma.com/app/5afgg2-1egj4n-7612ng-g313ie"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = PostPuma.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PostPuma.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PostPuma.MediaApi(api_client)
    file = None # bytearray |  (optional)

    try:
        # Upload media file
        api_response = api_instance.upload_media_file(file=file)
        print("The response of MediaApi->upload_media_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->upload_media_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | [optional] 

### Return type

[**MediaFile**](MediaFile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthenticated. |  -  |
**403** | Access forbidden. |  -  |
**404** | Workspace not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

