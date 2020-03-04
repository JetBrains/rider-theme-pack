import glob
import inspect
import logging
from xml.etree import ElementTree as ET
import argparse
import sys


MIN_PYTHON = (3, 7)
if sys.version_info < MIN_PYTHON:
    sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)


def empty(s: str) -> bool: return not s or not s.strip()


def prettyPrint(elem: ET.Element, newLine: str = '\n', sort: str = None, singleIndent: str = '  ', level: int = 0):
    """
    Sorts and indents the provided ElementTree
    :param elem: the ElementTree to beautify
    :param newLine: the string to create a new line
    :param sort: the name of the attribute which is used to sort sibling XML elements
    :param singleIndent: the string of whitespaces used to create indentation
    :param level: the current depth of recursive prettyPrint() call
    """
    # Based on the code snipped published at http://effbot.org/zone/element-lib.htm#prettyprint

    i = newLine + level * singleIndent

    # since Python 3.7, dict preserves the order of the inserted elements yet it won't allow to reorder them
    # since ElementTree uses a dict for element attributes' storage
    # so we are going to empty that dict and then repopulate it in desired order:
    # first is the 'sort' attribute then the rest in alphabet order
    if sort and sort in elem.attrib.keys():
        sortValue = elem.attrib.pop(sort)       # first extract the sort order defining attribute
        tmp = {sort: sortValue}                 # and add it as the first element
        for key in sorted(iter(elem.attrib)):   # then copy the remaining attributes in alphabetic order
            tmp[key] = elem.attrib[key]
        elem.attrib.clear()                     # now clear...
        for key in iter(tmp):                   # ... and repopulate the dict of attributes
            elem.attrib[key] = tmp[key]         #     in the desired order

    if len(elem) == 0:
        # if has no child elements
        if level > 0 and empty(elem.tail):
            elem.tail = i

    else:
        # if has child elements
        # sort top level elements by tag name in reverse order
        # sort all other levels' elements by the specified attribute's value
        if level == 0:
            if sort:
                # sort by tag name
                # for XML comment nodes child.tag is a function, not a string
                # chr(0x10FFFF) is the last possible char
                elem[:] = sorted(elem, key=lambda child:
                    child.tag if child.tag and not inspect.isfunction(child.tag)
                    else chr(0x10FFFF), reverse=True)
        else:
            if sort:
                # sort by specified attribute's values
                elem[:] = sorted(elem, key=lambda child: child.get(sort) if child.get(sort) else '')

        if empty(elem.text):
            elem.text = i + singleIndent
        if empty(elem.tail):
            elem.tail = i

        # recursively pretty print each child element
        lastChild = None
        for child in elem:
            prettyPrint(child, newLine, sort, singleIndent, level + 1)
            lastChild = child

        if empty(lastChild.tail):
            lastChild.tail = i


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
                                     "Sorts and beautifies an XML file which defines an IDEA editor color scheme. "
                                     "Top-level XML elements are ordered in the reverse alphabetical order. "
                                     "All other XML elements are sorted in the right alphabetical order. "
                                     "Sibling XML elements are sorted by the value of their \"name=\" attribute. "
                                     "For each XML element its attributes are listed in alphabetical order, except "
                                     "the \"name=\" attribute which is listed first.")
    parser.add_argument('input', type=str, nargs='+', help='XML files to beautify; file name masks are accepted')
    parser.add_argument('-o', '--output', type=str, help='resulting XML file if only a single input file is specified; '
                                                         'if not specified, or if there are many input files, '
                                                         'the input files are overwritten')
    args = parser.parse_args()

    numberOfFiles = 0
    for path in args.input:
        logging.info("Handling " + path)
        # each path can be a single file or a mask
        for file in glob.iglob(path):
            logging.info("  opening " + file)
            numberOfFiles += 1
            try:
                tree = ET.parse(file)
                root = tree.getroot()
                root.insert(0, ET.Comment(" This document is auto-generated, do not edit manually."))
                prettyPrint(root, newLine='\n', sort='name')
                if args.output and numberOfFiles == 1:
                    logging.info("  writing to " + args.output)
                    tree.write(args.output, encoding='unicode')
                else:
                    logging.info("  writing to " + file)
                    tree.write(file, encoding='unicode')
            except ET.ParseError:
                logging.warning(file + " is not an XML file, skipping")
