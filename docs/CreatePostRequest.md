# CreatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**time** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**schedule** | **bool** |  | [optional] 
**schedule_now** | **bool** |  | [optional] 
**queue** | **bool** |  | [optional] 
**accounts** | **List[int]** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**versions** | [**List[Version]**](Version.md) |  | [optional] 

## Example

```python
from PostPuma.models.create_post_request import CreatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePostRequest from a JSON string
create_post_request_instance = CreatePostRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePostRequest.to_json())

# convert the object into a dict
create_post_request_dict = create_post_request_instance.to_dict()
# create an instance of CreatePostRequest from a dict
create_post_request_from_dict = CreatePostRequest.from_dict(create_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


