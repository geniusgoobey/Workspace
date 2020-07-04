from xml.etree import ElementTree

with open('catelog.xml', 'rb') as xml_file:
    tree = ElementTree.parse(xml_file)
    
    for node in tree.iter():
        print(f'{node.tag}', end='')
        if node.text.strip():
            print(f' - {node.text.strip()}', end='')
        if node.attrib:
            print(f' - {node.attrib}', end='')
        print()
        print('-' * 100)