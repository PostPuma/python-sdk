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

from PostPuma.models.delete_posts200_response_one_of import DeletePosts200ResponseOneOf

class TestDeletePosts200ResponseOneOf(unittest.TestCase):
    """DeletePosts200ResponseOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeletePosts200ResponseOneOf:
        """Test DeletePosts200ResponseOneOf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeletePosts200ResponseOneOf`
        """
        model = DeletePosts200ResponseOneOf()
        if include_optional:
            return DeletePosts200ResponseOneOf(
                deleted = True
            )
        else:
            return DeletePosts200ResponseOneOf(
        )
        """

    def testDeletePosts200ResponseOneOf(self):
        """Test DeletePosts200ResponseOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
