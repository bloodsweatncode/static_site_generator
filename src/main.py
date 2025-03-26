from textnode import TextNode, TextType

def main():
    dummy_object = TextNode("Test", TextType.LINK, "https://www.sagst.de")
    print(dummy_object)

if __name__ == "__main__":
    main()
