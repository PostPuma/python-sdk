# VersionOptionsPinterest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**boards** | [**VersionOptionsPinterestBoards**](VersionOptionsPinterestBoards.md) |  | [optional] 

## Example

```python
from PostPuma.models.version_options_pinterest import VersionOptionsPinterest

# TODO update the JSON string below
json = "{}"
# create an instance of VersionOptionsPinterest from a JSON string
version_options_pinterest_instance = VersionOptionsPinterest.from_json(json)
# print the JSON string representation of the object
print(VersionOptionsPinterest.to_json())

# convert the object into a dict
version_options_pinterest_dict = version_options_pinterest_instance.to_dict()
# create an instance of VersionOptionsPinterest from a dict
version_options_pinterest_from_dict = VersionOptionsPinterest.from_dict(version_options_pinterest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


