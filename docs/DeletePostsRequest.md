# DeletePostsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posts** | **List[str]** | Post UUIDs | 
**trash** | **bool** |  | [optional] 

## Example

```python
from PostPuma.models.delete_posts_request import DeletePostsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePostsRequest from a JSON string
delete_posts_request_instance = DeletePostsRequest.from_json(json)
# print the JSON string representation of the object
print(DeletePostsRequest.to_json())

# convert the object into a dict
delete_posts_request_dict = delete_posts_request_instance.to_dict()
# create an instance of DeletePostsRequest from a dict
delete_posts_request_from_dict = DeletePostsRequest.from_dict(delete_posts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


