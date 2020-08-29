from .tag import Tag

class XMLParser:
    def __init__(self):
        pass

    def load(self, file):
        return self.loads(file.read())

    def loads(self, xml_str):
        self.root = None
        self.working_tags = []
        tag_str = ""
        content = ""
        new_tag = True
        in_str = False

        for char in xml_str:
            if char == '\n' and not in_str:
                continue
            if new_tag:
                if char == '<':
                    if len(content.replace(' ', '').replace('\t', '')) > 0:
                        self.working_tags[-1].content = content.strip(' ').strip('\t')
                    content = ""
                    tag_str += char
                    new_tag = False
                else:
                    content += char
            else:
                tag_str += char
                if char == '"' or char == "'":
                    in_str = not in_str
                elif char == '>' and not in_str:
                    new_tag = True
                    self.create_tag(tag_str)
                    tag_str = ""

        return self.root

    def create_tag(self, tag):
        if tag.startswith('<?'):
            return

        tag_content = tag[1:][:-1]  # remove the <>
        tag_content = tag_content.replace(' =', '=').replace('= ', '=').replace(' = ', '=')  # get the formatting right

        # is the tag self closing? like: <self_closing_tab />
        self_closing = False
        if tag_content.endswith('/'):
            self_closing = True
            tag_content = tag_content[:-1]

        # make a list out of the name and attrs
        in_str = False
        list_tag_content = []
        new_item = ""
        for char in tag_content:
            if char == '"' or char == "'":
                in_str = not in_str
            elif char == ' ' and not in_str:
                list_tag_content.append(new_item)
                new_item = ""
                continue
            new_item += char
        list_tag_content.append(new_item)

        # get tag name
        tag_name = list_tag_content[0]
        if tag_name.startswith('/'):
            if len(self.working_tags) != 0:
                self.working_tags.remove(self.working_tags[-1])  # remove urself bitch
            return

        # get attrs
        attrs = {}
        for item in list_tag_content[1:]:  # without the name
            name = item.split("=")[0]
            value = item[len(name) + 2:][:-1]  # get value and remove " or '
            if name == '':
                continue
            attrs[name] = value

        # construct tag
        tag = Tag(tag_name, self_closing, **attrs)
        if self.root is None:
            self.root = tag
        elif len(self.working_tags) == 0:
            tag.set_parent(self.root)
            if not tag.self_closing:
                self.working_tags.append(tag)
        else:
            tag.set_parent(self.working_tags[-1])
            if not tag.self_closing:
                self.working_tags.append(tag)
