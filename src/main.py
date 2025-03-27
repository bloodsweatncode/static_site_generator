from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    dummy_object = TextNode("Test", TextType.LINK, "https://www.sagst.de")
    dummy_html = HTMLNode("", "", "", {"a": "la", "b": "lb"})
    print(dummy_object)
    print(dummy_html)

if __name__ == "__main__":
    main()
