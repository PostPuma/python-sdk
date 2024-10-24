# PostPuma.TagsApi

All URIs are relative to *https://app.postpuma.com/app/5afgg2-1egj4n-7612ng-g313ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag**](TagsApi.md#create_tag) | **POST** /tags | Create tag
[**delete_tag**](TagsApi.md#delete_tag) | **DELETE** /tags/{tagUuid} | Delete tag
[**get_tag**](TagsApi.md#get_tag) | **GET** /tags/{tagUuid} | Get tag
[**list_tags**](TagsApi.md#list_tags) | **GET** /tags | List tags
[**update_tag**](TagsApi.md#update_tag) | **PUT** /tags/{tagUuid} | Update tag


# **create_tag**
> Tag create_tag(create_tag_request=create_tag_request)

Create tag

Create tag

### Example

* Bearer Authentication (bearerAuth):

```python
import PostPuma
from PostPuma.models.create_tag_request import CreateTagRequest
from PostPuma.models.tag import Tag
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
    api_instance = PostPuma.TagsApi(api_client)
    create_tag_request = PostPuma.CreateTagRequest() # CreateTagRequest |  (optional)

    try:
        # Create tag
        api_response = api_instance.create_tag(create_tag_request=create_tag_request)
        print("The response of TagsApi->create_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->create_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tag_request** | [**CreateTagRequest**](CreateTagRequest.md)|  | [optional] 

### Return type

[**Tag**](Tag.md)

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
**422** | Validation errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> DeleteMediaFiles200Response delete_tag(tag_uuid)

Delete tag

Delete tag

### Example

* Bearer Authentication (bearerAuth):

```python
import PostPuma
from PostPuma.models.delete_media_files200_response import DeleteMediaFiles200Response
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
    api_instance = PostPuma.TagsApi(api_client)
    tag_uuid = 'tag_uuid_example' # str | Tag UUID

    try:
        # Delete tag
        api_response = api_instance.delete_tag(tag_uuid)
        print("The response of TagsApi->delete_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->delete_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_uuid** | **str**| Tag UUID | 

### Return type

[**DeleteMediaFiles200Response**](DeleteMediaFiles200Response.md)

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

# **get_tag**
> Tag get_tag(tag_uuid)

Get tag

Get tag

### Example

* Bearer Authentication (bearerAuth):

```python
import PostPuma
from PostPuma.models.tag import Tag
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
    api_instance = PostPuma.TagsApi(api_client)
    tag_uuid = 'tag_uuid_example' # str | Tag UUID

    try:
        # Get tag
        api_response = api_instance.get_tag(tag_uuid)
        print("The response of TagsApi->get_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->get_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_uuid** | **str**| Tag UUID | 

### Return type

[**Tag**](Tag.md)

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

# **list_tags**
> ListTags200Response list_tags()

List tags

List tags

### Example

* Bearer Authentication (bearerAuth):

```python
import PostPuma
from PostPuma.models.list_tags200_response import ListTags200Response
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
    api_instance = PostPuma.TagsApi(api_client)

    try:
        # List tags
        api_response = api_instance.list_tags()
        print("The response of TagsApi->list_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->list_tags: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListTags200Response**](ListTags200Response.md)

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

# **update_tag**
> DeleteMediaFiles200Response update_tag(tag_uuid, update_tag_request=update_tag_request)

Update tag

Update tag

### Example

* Bearer Authentication (bearerAuth):

```python
import PostPuma
from PostPuma.models.delete_media_files200_response import DeleteMediaFiles200Response
from PostPuma.models.update_tag_request import UpdateTagRequest
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
    api_instance = PostPuma.TagsApi(api_client)
    tag_uuid = 'tag_uuid_example' # str | Tag UUID
    update_tag_request = PostPuma.UpdateTagRequest() # UpdateTagRequest |  (optional)

    try:
        # Update tag
        api_response = api_instance.update_tag(tag_uuid, update_tag_request=update_tag_request)
        print("The response of TagsApi->update_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->update_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_uuid** | **str**| Tag UUID | 
 **update_tag_request** | [**UpdateTagRequest**](UpdateTagRequest.md)|  | [optional] 

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
**422** | Validation errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

