from enum import Enum

from src.htmlnode import HTMLNode
from src.leafnode import LeafNode


class TextType(Enum):
    TEXT = "TEXT"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    CODE = "CODE"
    LINK = "LINK"
    IMAGE = "IMAGE"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text, self.text_type, self.url = text, text_type, url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.url, dict({"href": f"{text_node.url}"}))
        case TextType.IMAGE:
            return LeafNode("img", "", dict({"src": f"{text_node.url}", "alt": f"{text_node.text}"}))
        case _:
            raise Exception(f"Unknown text type: {text_node.text_type}")

