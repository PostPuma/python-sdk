# AccountData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**union_id** | **str** |  | [optional] 
**is_private** | **bool** |  | [optional] 
**duet_disabled** | **bool** |  | [optional] 
**privacy_levels** | **List[str]** |  | [optional] 
**stitch_disabled** | **bool** |  | [optional] 
**comment_disabled** | **bool** |  | [optional] 
**max_video_post_duration_sec** | **int** |  | [optional] 

## Example

```python
from PostPuma.models.account_data import AccountData

# TODO update the JSON string below
json = "{}"
# create an instance of AccountData from a JSON string
account_data_instance = AccountData.from_json(json)
# print the JSON string representation of the object
print(AccountData.to_json())

# convert the object into a dict
account_data_dict = account_data_instance.to_dict()
# create an instance of AccountData from a dict
account_data_from_dict = AccountData.from_dict(account_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


