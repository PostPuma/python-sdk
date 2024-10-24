# VersionContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**media** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from PostPuma.models.version_content import VersionContent

# TODO update the JSON string below
json = "{}"
# create an instance of VersionContent from a JSON string
version_content_instance = VersionContent.from_json(json)
# print the JSON string representation of the object
print(VersionContent.to_json())

# convert the object into a dict
version_content_dict = version_content_instance.to_dict()
# create an instance of VersionContent from a dict
version_content_from_dict = VersionContent.from_dict(version_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


