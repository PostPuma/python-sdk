# coding: utf-8

"""
    PostPuma - OpenAPI 3.0

    PostPuma API specifications

    The version of the OpenAPI document: 1.0.0
    Contact: support@postpuma.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from PostPuma.models.queue_post200_response import QueuePost200Response

class TestQueuePost200Response(unittest.TestCase):
    """QueuePost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueuePost200Response:
        """Test QueuePost200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueuePost200Response`
        """
        model = QueuePost200Response()
        if include_optional:
            return QueuePost200Response(
                success = True,
                scheduled_at = ''
            )
        else:
            return QueuePost200Response(
        )
        """

    def testQueuePost200Response(self):
        """Test QueuePost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
