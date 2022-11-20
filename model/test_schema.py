import unittest

import pydantic.error_wrappers

from model import schema


class TestSchema(unittest.TestCase):

    def test_from_json_success(self):
        json_dict = {
            "title": "foo",
            "description": "foo",
            "source": "foo",
            "link": "foo",
            "rating": -1,
            "hash_id": "bar"
        }
        post: schema.Post = schema.Post(**json_dict)

        self.assertEqual(post.title, "foo")
        self.assertEqual(post.description, "foo")
        self.assertEqual(post.source, "foo")
        self.assertEqual(post.link, "foo")
        self.assertEqual(post.rating, -1)
        self.assertEqual(post.hash_id, "bar")

    def test_from_json_failure_missing_field(self):
        json_dict = {
            "title": "foo",
        }

        self.assertRaises(pydantic.error_wrappers.ValidationError, schema.Post, **json_dict)


if __name__ == '__main__':
    unittest.main()
