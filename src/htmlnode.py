class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"<HTMLNode tag={self.tag} value={self.value} children={self.children} props={self.props}>"

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        html = ""
        if self.props == None:
            return html
        keys = list(self.props.keys())
        values = list(self.props.values())
        for i in range(0, len(keys)):
            html += f" {keys[i]}=\"{values[i]}\""
        return html


class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("invalid HTML:no value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag = None, children = None, props = None):
        if not children or children == []:
            raise ValueError("ParentNode must have children")
        if not tag:
            raise ValueError("ParentNode must have a tag")
        super().__init__(tag, None, children, props)

    def to_html(self):
        children_html = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

