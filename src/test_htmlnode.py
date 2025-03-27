import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a text node", [], {"a": "la", "b": "lb"})
        self.assertEqual(node.props_to_html(), ' a="la" b="lb"')
        
    def test_eq_false(self):
        node = HTMLNode("div", "This is a text node", [], {"a": "la", "b": "lb"})
        self.assertNotEqual(node.props_to_html(), "\{'a': 'la', 'b': 'lb'\}")
        


if __name__ == "__main__":
    unittest.main()
