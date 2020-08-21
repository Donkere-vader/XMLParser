from XMLParser import XMLParser

xmlparser = XMLParser()

xml_root = xmlparser.loads(open('XMLParser/test.xml', 'r').read())

print(xml_root)  # represents the root object
