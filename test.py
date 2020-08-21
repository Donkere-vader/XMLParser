from XMLParser import XMLParser

xmlparser = XMLParser()

root = xmlparser.load(open('XMLParser/test.xml', 'r'))

print(root.children[0].children)
