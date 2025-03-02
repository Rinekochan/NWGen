from functools import reduce


class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag, self.value, self.children, self.props = tag, value, children, props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None: return ""
        return reduce(lambda html_str, kv: html_str + f" {kv[0]}=\"{kv[1]}\"", self.props.items(), "")

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
