from unittest import TestCase
from Part2_Your_first_automated_software_testing.blog.blog import Blog

class BlogTest(TestCase):

    def test_create_Blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)
