import xml.etree.ElementTree as ET
import json


def get_text(element):
    return element.text.encode('utf8') if element.text else ""


def push(dict_, element_tag, element_value):
    if element_tag in dict_ and not isinstance(dict_[element_tag], list):
        first_val = dict_[element_tag]
        dict_[element_tag] = [first_val, element_value]
    elif element_tag not in dict_:
        dict_[element_tag] = element_value
    else:
        dict_[element_tag].append(element_value)


def xml_tree_walk(root, dict_, attributes=[]):
    for element in root:
        if element.tag in attributes and element.tag not in dict_:
            dict_[element.tag] = []

        if len(list(element)):
            push(dict_, element.tag, xml_tree_walk(element, {}, attributes))
        elif element.tag in dict_:
            push(dict_, element.tag, get_text(element))
        else:
            dict_[element.tag] = get_text(element)
    return dict_


def promos_convert(root):
    list_attributes = ['Promotion', 'ItemId', 'ItemType']
    return json.dumps(xml_tree_walk(root, {}, list_attributes), indent=2,
                      sort_keys=True)


def prices_convert(root):
    list_attributes = ['item']
    return json.dumps(xml_tree_walk(root, {}, list_attributes), indent=2,
                      sort_keys=True)


def stores_convert(root):
    list_attributes = ['store']
    return json.dumps(xml_tree_walk(root, {}, list_attributes), indent=2,
                      sort_keys=True)


def get_root(file_path):
    with open(file_path) as xml_handler:
        try:
            root = ET.fromstring(xml_handler.read())
            return root
        except ET.ParseError:
            logger.error("Error parsing the XML file '%s'", file_path)
            raise Exception('XML Parsing error')


if __name__ == '__main__':
    pass
