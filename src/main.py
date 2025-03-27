from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode

def main():
    dummy_object = TextNode("Test", TextType.IMAGE, "https://www.sagst.de")
    dummy_html = HTMLNode("", "", "", {"a": "la", "b": "lb"})
    print(dummy_object)
    print(text_node_to_html_node(dummy_object))

if __name__ == "__main__":
    main()
