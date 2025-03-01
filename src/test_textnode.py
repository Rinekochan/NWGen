import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertEqual(node, TextNode("This is a text node", TextType.BOLD, "https://www.google.com"))

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertNotEqual(node, TextNode("This is a text node, but different!", TextType.ITALIC, "https://www.microsoft.com"))

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertEqual(str(node), "TextNode(This is a text node, BOLD, https://www.google.com)")

    def test_not_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertNotEqual(str(node), "TextNode(This is a text node, but different!, ITALIC, https://www.microsoft.com)")


if __name__ == "__main__":
    unittest.main()