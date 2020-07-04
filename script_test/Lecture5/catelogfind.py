from xml.etree import ElementTree

with open('catelog.xml', 'rb') as xml_file:
    tree = ElementTree.parse(xml_file)
    
    for node in tree.findall('.//book'):
        _id = node.attrib['id']
        author = node.find('.//author')
        title = node.find('.//title')
        print(f'{_id} - {author.text} - {title.text}')
        