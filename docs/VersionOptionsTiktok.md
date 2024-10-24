# VersionOptionsTiktok


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privacy_level** | [**VersionOptionsTiktokPrivacyLevel**](VersionOptionsTiktokPrivacyLevel.md) |  | [optional] 
**allow_comments** | [**VersionOptionsTiktokPrivacyLevel**](VersionOptionsTiktokPrivacyLevel.md) |  | [optional] 
**allow_duet** | [**VersionOptionsTiktokPrivacyLevel**](VersionOptionsTiktokPrivacyLevel.md) |  | [optional] 
**allow_stitch** | [**VersionOptionsTiktokPrivacyLevel**](VersionOptionsTiktokPrivacyLevel.md) |  | [optional] 
**content_disclosure** | [**VersionOptionsTiktokPrivacyLevel**](VersionOptionsTiktokPrivacyLevel.md) |  | [optional] 
**brand_organic_toggle** | [**VersionOptionsTiktokPrivacyLevel**](VersionOptionsTiktokPrivacyLevel.md) |  | [optional] 
**brand_content_toggle** | [**VersionOptionsTiktokPrivacyLevel**](VersionOptionsTiktokPrivacyLevel.md) |  | [optional] 

## Example

```python
from PostPuma.models.version_options_tiktok import VersionOptionsTiktok

# TODO update the JSON string below
json = "{}"
# create an instance of VersionOptionsTiktok from a JSON string
version_options_tiktok_instance = VersionOptionsTiktok.from_json(json)
# print the JSON string representation of the object
print(VersionOptionsTiktok.to_json())

# convert the object into a dict
version_options_tiktok_dict = version_options_tiktok_instance.to_dict()
# create an instance of VersionOptionsTiktok from a dict
version_options_tiktok_from_dict = VersionOptionsTiktok.from_dict(version_options_tiktok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


