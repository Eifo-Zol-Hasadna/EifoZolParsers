#!/usr/bin/python


import libs.commonparser as cparser
import libs.commonxml as cxml
import sys


def main():
    xmls = ['prices.xml', 'stores.xml', 'promos.xml']
    jsons = ['prices.json', 'stores.json', 'promos.json']
    convert_funcs = [cxml.prices_convert, cxml.stores_convert,
                    cxml.promos_convert]

    for convert_fun, files_tuple in zip(convert_funcs, zip(xmls, jsons)):
        xml_file, json_file = files_tuple
        with open(json_file, 'w') as file_handler:
            logger.debug("writing json to '%s' from '%s' xml",
                         json_file, xml_file)
            file_handler.write(
                    convert_fun(
                        cxml.get_root(
                            cparser.get_file_path(sys.argv[0], xml_file))))


if __name__ == '__main__':
    logger = cparser.setup_logger()
    main()
