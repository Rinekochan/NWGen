import unittest

from src.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(tag="h1")
        self.assertEqual(repr(node), "HTMLNode(h1, None, None, None)")

    def test_not_repr(self):
        node = HTMLNode(tag="h1")
        self.assertNotEqual(repr(node), "HTMLNode(h2)")

    def test_props_to_html(self):
        node = HTMLNode(tag="h1", props=dict({"href": "https://google.com"}))
        self.assertEqual(node.props_to_html(), " href=\"https://google.com\"")

    def test_not_props_to_html(self):
        node = HTMLNode(tag="h1", props=dict({"href": "https://google.com"}))
        self.assertNotEqual(node.props_to_html(), " href=\"https://microsoft.com\"")

if __name__ == "__main__":
    unittest.main()