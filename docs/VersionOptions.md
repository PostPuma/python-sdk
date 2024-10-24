# VersionOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tiktok** | [**VersionOptionsTiktok**](VersionOptionsTiktok.md) |  | [optional] 
**youtube** | [**VersionOptionsYoutube**](VersionOptionsYoutube.md) |  | [optional] 
**linkedin** | [**VersionOptionsLinkedin**](VersionOptionsLinkedin.md) |  | [optional] 
**mastodon** | [**VersionOptionsMastodon**](VersionOptionsMastodon.md) |  | [optional] 
**instagram** | [**VersionOptionsInstagram**](VersionOptionsInstagram.md) |  | [optional] 
**pinterest** | [**VersionOptionsPinterest**](VersionOptionsPinterest.md) |  | [optional] 
**facebook_page** | [**VersionOptionsInstagram**](VersionOptionsInstagram.md) |  | [optional] 

## Example

```python
from PostPuma.models.version_options import VersionOptions

# TODO update the JSON string below
json = "{}"
# create an instance of VersionOptions from a JSON string
version_options_instance = VersionOptions.from_json(json)
# print the JSON string representation of the object
print(VersionOptions.to_json())

# convert the object into a dict
version_options_dict = version_options_instance.to_dict()
# create an instance of VersionOptions from a dict
version_options_from_dict = VersionOptions.from_dict(version_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


