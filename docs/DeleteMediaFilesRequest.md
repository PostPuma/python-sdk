# DeleteMediaFilesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[int]** | File IDs | 

## Example

```python
from PostPuma.models.delete_media_files_request import DeleteMediaFilesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMediaFilesRequest from a JSON string
delete_media_files_request_instance = DeleteMediaFilesRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteMediaFilesRequest.to_json())

# convert the object into a dict
delete_media_files_request_dict = delete_media_files_request_instance.to_dict()
# create an instance of DeleteMediaFilesRequest from a dict
delete_media_files_request_from_dict = DeleteMediaFilesRequest.from_dict(delete_media_files_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


