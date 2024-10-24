# QueuePost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**scheduled_at** | **str** |  | [optional] 

## Example

```python
from PostPuma.models.queue_post200_response import QueuePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of QueuePost200Response from a JSON string
queue_post200_response_instance = QueuePost200Response.from_json(json)
# print the JSON string representation of the object
print(QueuePost200Response.to_json())

# convert the object into a dict
queue_post200_response_dict = queue_post200_response_instance.to_dict()
# create an instance of QueuePost200Response from a dict
queue_post200_response_from_dict = QueuePost200Response.from_dict(queue_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


