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

from PostPuma.models.create_tag_request import CreateTagRequest

class TestCreateTagRequest(unittest.TestCase):
    """CreateTagRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateTagRequest:
        """Test CreateTagRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateTagRequest`
        """
        model = CreateTagRequest()
        if include_optional:
            return CreateTagRequest(
                name = '',
                hex_color = ''
            )
        else:
            return CreateTagRequest(
                name = '',
                hex_color = '',
        )
        """

    def testCreateTagRequest(self):
        """Test CreateTagRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()