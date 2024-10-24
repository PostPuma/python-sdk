# UpdatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**time** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**accounts** | **List[int]** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**versions** | [**List[Version]**](Version.md) |  | [optional] 

## Example

```python
from PostPuma.models.update_post_request import UpdatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePostRequest from a JSON string
update_post_request_instance = UpdatePostRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePostRequest.to_json())

# convert the object into a dict
update_post_request_dict = update_post_request_instance.to_dict()
# create an instance of UpdatePostRequest from a dict
update_post_request_from_dict = UpdatePostRequest.from_dict(update_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


