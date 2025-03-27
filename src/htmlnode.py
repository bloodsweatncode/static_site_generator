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
        keys = list(self.props.keys())
        values = list(self.props.values())
        for i in range(0, len(keys)):
            html += f" {keys[i]}=\"{values[i]}\"" 
        return html