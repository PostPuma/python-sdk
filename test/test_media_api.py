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

from PostPuma.media_api import MediaApi


class TestMediaApi(unittest.TestCase):
    """MediaApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MediaApi()

    def tearDown(self) -> None:
        pass

    def test_delete_media_files(self) -> None:
        """Test case for delete_media_files

        Delete media files
        """
        pass

    def test_get_media_file(self) -> None:
        """Test case for get_media_file

        Get media file
        """
        pass

    def test_list_media_files(self) -> None:
        """Test case for list_media_files

        List media files
        """
        pass

    def test_upload_media_file(self) -> None:
        """Test case for upload_media_file

        Upload media file
        """
        pass


if __name__ == '__main__':
    unittest.main()
