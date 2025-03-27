import unittest

from htmlnode import HTMLNode, LeafNode


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



if __name__ == "__main__":
    unittest.main()
