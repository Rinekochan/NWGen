from functools import reduce

from src.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None: raise ValueError("parent node needs to have a tag")

        return f"<{self.tag}>{reduce(lambda html_str, node: html_str + node.to_html(), self.children, '')}</{self.tag}>"
