from xml.etree import ElementTree

with open('classifications.xml', 'rb') as xml_file:
    tree = ElementTree.parse(xml_file)
    
    for node in tree.iter():
        print(f'{node.tag} - {node.text.strip()}')