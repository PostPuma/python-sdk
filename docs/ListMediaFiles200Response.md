# ListMediaFiles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MediaFile]**](MediaFile.md) |  | [optional] 

## Example

```python
from PostPuma.models.list_media_files200_response import ListMediaFiles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListMediaFiles200Response from a JSON string
list_media_files200_response_instance = ListMediaFiles200Response.from_json(json)
# print the JSON string representation of the object
print(ListMediaFiles200Response.to_json())

# convert the object into a dict
list_media_files200_response_dict = list_media_files200_response_instance.to_dict()
# create an instance of ListMediaFiles200Response from a dict
list_media_files200_response_from_dict = ListMediaFiles200Response.from_dict(list_media_files200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


