# PostPuma.AccountsApi

All URIs are relative to *https://app.postpuma.com/app/5afgg2-1egj4n-7612ng-g313ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account**](AccountsApi.md#get_account) | **GET** /accounts/{accountUuid} | Get account
[**list_accounts**](AccountsApi.md#list_accounts) | **GET** /accounts | List accounts


# **get_account**
> Account get_account(account_uuid)

Get account

Get account

### Example

* Bearer Authentication (bearerAuth):

```python
import PostPuma
from PostPuma.models.account import Account
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
    api_instance = PostPuma.AccountsApi(api_client)
    account_uuid = 'account_uuid_example' # str | Account UUID

    try:
        # Get account
        api_response = api_instance.get_account(account_uuid)
        print("The response of AccountsApi->get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_uuid** | **str**| Account UUID | 

### Return type

[**Account**](Account.md)

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

# **list_accounts**
> ListAccounts200Response list_accounts()

List accounts

List accounts

### Example

* Bearer Authentication (bearerAuth):

```python
import PostPuma
from PostPuma.models.list_accounts200_response import ListAccounts200Response
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
    api_instance = PostPuma.AccountsApi(api_client)

    try:
        # List accounts
        api_response = api_instance.list_accounts()
        print("The response of AccountsApi->list_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->list_accounts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListAccounts200Response**](ListAccounts200Response.md)

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

