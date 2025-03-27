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
        if not value:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag, value, [], props)

    def to_html(self):
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"