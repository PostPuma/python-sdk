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

from PostPuma.posts_api import PostsApi


class TestPostsApi(unittest.TestCase):
    """PostsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PostsApi()

    def tearDown(self) -> None:
        pass

    def test_create_post(self) -> None:
        """Test case for create_post

        Create post
        """
        pass

    def test_delete_post(self) -> None:
        """Test case for delete_post

        Delete post
        """
        pass

    def test_delete_posts(self) -> None:
        """Test case for delete_posts

        Delete posts
        """
        pass

    def test_get_post(self) -> None:
        """Test case for get_post

        Get post
        """
        pass

    def test_list_posts(self) -> None:
        """Test case for list_posts

        List posts
        """
        pass

    def test_queue_post(self) -> None:
        """Test case for queue_post

        Queue post
        """
        pass

    def test_schedule_post(self) -> None:
        """Test case for schedule_post

        Schedule post
        """
        pass

    def test_update_post(self) -> None:
        """Test case for update_post

        Update post
        """
        pass


if __name__ == '__main__':
    unittest.main()
