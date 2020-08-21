class Tag:
    """ A XML tag """
    def __init__(self, _name, _self_closing, **kwargs):
        self.name = _name  # tag name <root> tag.name would be 'root'
        self.attrs = kwargs  # all the arrgs <root x="test"> would become -> kwargs: {"x": "test"}
        self.self_closing = _self_closing  # self_closing tag: <self_closing_tag />
        self.children = []
        self.parent = None
        self.content = None

    def set_parent(self, parent):
        """ Called when setting the parent """
        self.parent = parent
        self.parent.children.append(self)

    def replace(self, new_tag):
        """ Replace this tag with a new tag """
        new_tag.parent = self.parent
        new_tag.children += self.children
        for child in self.children:
            child.parent = new_tag
        self.parent.children.append(new_tag)
        self.parent.children.remove(self)

    def __repr__(self):
        return str(self)  # call self.__str__()

    def __str__(self):
        """ When converted to string """
        attrs_str = ""
        for item in self.attrs:
            attrs_str += f"{item}=\"{self.attrs[item]}\" "
        if len(attrs_str) > 0:
            return f"<{self.name} {attrs_str[:-1]}{' /' if self.self_closing else ''}>"
        else:
            return f"<{self.name}{' /' if self.self_closing else ''}>"
