import unittest

from src.leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_not_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertNotEqual(node.to_html(), "<a>Hello, world!</a>")

    def test_leaf_to_html_a_with_tag(self):
        node = LeafNode("a", "Hello, world!", dict({"href": "https://google.com"}))
        self.assertEqual(node.to_html(), "<a href=\"https://google.com\">Hello, world!</a>")

    def test_not_leaf_to_html_a_with_tag(self):
        node = LeafNode("a", "Hello, world!", dict({"href": "https://google.com"}))
        self.assertNotEqual(node.to_html(), "<a>Hello, world!</a>")

if __name__ == '__main__':
    unittest.main()