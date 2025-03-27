from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    pass


node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)