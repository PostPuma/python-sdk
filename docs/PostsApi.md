# PostPuma.PostsApi

All URIs are relative to *https://app.postpuma.com/app/5afgg2-1egj4n-7612ng-g313ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_post**](PostsApi.md#create_post) | **POST** /posts | Create post
[**delete_post**](PostsApi.md#delete_post) | **DELETE** /posts/{postUuid} | Delete post
[**delete_posts**](PostsApi.md#delete_posts) | **DELETE** /posts | Delete posts
[**get_post**](PostsApi.md#get_post) | **GET** /posts/{postUuid} | Get post
[**list_posts**](PostsApi.md#list_posts) | **GET** /posts | List posts
[**queue_post**](PostsApi.md#queue_post) | **POST** /posts/add-to-queue/{postUuid} | Queue post
[**schedule_post**](PostsApi.md#schedule_post) | **POST** /posts/schedule/{postUuid} | Schedule post
[**update_post**](PostsApi.md#update_post) | **PUT** /posts/{postUuid} | Update post


# **create_post**
> Post create_post(create_post_request=create_post_request)

Create post

Create post

### Example

* Bearer Authentication (bearerAuth):

```python
import PostPuma
from PostPuma.models.create_post_request import CreatePostRequest
from PostPuma.models.post import Post
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
    api_instance = PostPuma.PostsApi(api_client)
    create_post_request = PostPuma.CreatePostRequest() # CreatePostRequest |  (optional)

    try:
        # Create post
        api_response = api_instance.create_post(create_post_request=create_post_request)
        print("The response of PostsApi->create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_post_request** | [**CreatePostRequest**](CreatePostRequest.md)|  | [optional] 

### Return type

[**Post**](Post.md)

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

# **delete_post**
> DeletePosts200Response delete_post(post_uuid, delete_post_request=delete_post_request)

Delete post

Delete post

### Example

* Bearer Authentication (bearerAuth):

```python
import PostPuma
from PostPuma.models.delete_post_request import DeletePostRequest
from PostPuma.models.delete_posts200_response import DeletePosts200Response
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
    api_instance = PostPuma.PostsApi(api_client)
    post_uuid = 'post_uuid_example' # str | Post UUID
    delete_post_request = PostPuma.DeletePostRequest() # DeletePostRequest |  (optional)

    try:
        # Delete post
        api_response = api_instance.delete_post(post_uuid, delete_post_request=delete_post_request)
        print("The response of PostsApi->delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_uuid** | **str**| Post UUID | 
 **delete_post_request** | [**DeletePostRequest**](DeletePostRequest.md)|  | [optional] 

### Return type

[**DeletePosts200Response**](DeletePosts200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_posts**
> DeletePosts200Response delete_posts(delete_posts_request=delete_posts_request)

Delete posts

Delete posts

### Example

* Bearer Authentication (bearerAuth):

```python
import PostPuma
from PostPuma.models.delete_posts200_response import DeletePosts200Response
from PostPuma.models.delete_posts_request import DeletePostsRequest
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
    api_instance = PostPuma.PostsApi(api_client)
    delete_posts_request = PostPuma.DeletePostsRequest() # DeletePostsRequest |  (optional)

    try:
        # Delete posts
        api_response = api_instance.delete_posts(delete_posts_request=delete_posts_request)
        print("The response of PostsApi->delete_posts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->delete_posts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_posts_request** | [**DeletePostsRequest**](DeletePostsRequest.md)|  | [optional] 

### Return type

[**DeletePosts200Response**](DeletePosts200Response.md)

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

# **get_post**
> Post get_post(post_uuid)

Get post

Get post

### Example

* Bearer Authentication (bearerAuth):

```python
import PostPuma
from PostPuma.models.post import Post
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
    api_instance = PostPuma.PostsApi(api_client)
    post_uuid = 'post_uuid_example' # str | Post UUID

    try:
        # Get post
        api_response = api_instance.get_post(post_uuid)
        print("The response of PostsApi->get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_uuid** | **str**| Post UUID | 

### Return type

[**Post**](Post.md)

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

# **list_posts**
> ListPosts200Response list_posts(page=page)

List posts

List posts

### Example

* Bearer Authentication (bearerAuth):

```python
import PostPuma
from PostPuma.models.list_posts200_response import ListPosts200Response
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
    api_instance = PostPuma.PostsApi(api_client)
    page = 56 # int | Page (optional)

    try:
        # List posts
        api_response = api_instance.list_posts(page=page)
        print("The response of PostsApi->list_posts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->list_posts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page | [optional] 

### Return type

[**ListPosts200Response**](ListPosts200Response.md)

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

# **queue_post**
> QueuePost200Response queue_post(post_uuid)

Queue post

Queue post

### Example

* Bearer Authentication (bearerAuth):

```python
import PostPuma
from PostPuma.models.queue_post200_response import QueuePost200Response
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
    api_instance = PostPuma.PostsApi(api_client)
    post_uuid = 'post_uuid_example' # str | Post UUID

    try:
        # Queue post
        api_response = api_instance.queue_post(post_uuid)
        print("The response of PostsApi->queue_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->queue_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_uuid** | **str**| Post UUID | 

### Return type

[**QueuePost200Response**](QueuePost200Response.md)

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
**422** | Validation errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_post**
> QueuePost200Response schedule_post(post_uuid, schedule_post_request=schedule_post_request)

Schedule post

Schedule post

### Example

* Bearer Authentication (bearerAuth):

```python
import PostPuma
from PostPuma.models.queue_post200_response import QueuePost200Response
from PostPuma.models.schedule_post_request import SchedulePostRequest
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
    api_instance = PostPuma.PostsApi(api_client)
    post_uuid = 'post_uuid_example' # str | Post UUID
    schedule_post_request = PostPuma.SchedulePostRequest() # SchedulePostRequest |  (optional)

    try:
        # Schedule post
        api_response = api_instance.schedule_post(post_uuid, schedule_post_request=schedule_post_request)
        print("The response of PostsApi->schedule_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->schedule_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_uuid** | **str**| Post UUID | 
 **schedule_post_request** | [**SchedulePostRequest**](SchedulePostRequest.md)|  | [optional] 

### Return type

[**QueuePost200Response**](QueuePost200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_post**
> DeleteMediaFiles200Response update_post(post_uuid, update_post_request=update_post_request)

Update post

Update post

### Example

* Bearer Authentication (bearerAuth):

```python
import PostPuma
from PostPuma.models.delete_media_files200_response import DeleteMediaFiles200Response
from PostPuma.models.update_post_request import UpdatePostRequest
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
    api_instance = PostPuma.PostsApi(api_client)
    post_uuid = 'post_uuid_example' # str | Post UUID
    update_post_request = PostPuma.UpdatePostRequest() # UpdatePostRequest |  (optional)

    try:
        # Update post
        api_response = api_instance.update_post(post_uuid, update_post_request=update_post_request)
        print("The response of PostsApi->update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_uuid** | **str**| Post UUID | 
 **update_post_request** | [**UpdatePostRequest**](UpdatePostRequest.md)|  | [optional] 

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

