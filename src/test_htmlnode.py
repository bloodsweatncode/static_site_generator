import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a text node", [], {"a": "la", "b": "lb"})
        self.assertEqual(node.props_to_html(), ' a="la" b="lb"')
        
    def test_eq_false(self):
        node = HTMLNode("div", "This is a text node", [], {"a": "la", "b": "lb"})
        self.assertNotEqual(node.props_to_html(), "{'a': 'la', 'b': 'lb'}")
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_i(self):
        node = LeafNode("i", "Hello, world!")
        self.assertEqual(node.to_html(), "<i>Hello, world!</i>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
