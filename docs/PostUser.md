# PostUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from PostPuma.models.post_user import PostUser

# TODO update the JSON string below
json = "{}"
# create an instance of PostUser from a JSON string
post_user_instance = PostUser.from_json(json)
# print the JSON string representation of the object
print(PostUser.to_json())

# convert the object into a dict
post_user_dict = post_user_instance.to_dict()
# create an instance of PostUser from a dict
post_user_from_dict = PostUser.from_dict(post_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


