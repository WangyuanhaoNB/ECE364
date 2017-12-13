import sys

from PySide.QtGui import *
from BasicUI import *
from xml.etree import ElementTree
from xml.dom import minidom


if __name__ == "__main__":
    root = ElementTree.Element('Content')
    stu_name = ElementTree.Element("StudentName")
    root.append(stu_name)
    stu_name.text="Filsd"
    root.set("grad", "falso")
    tree = ElementTree.ElementTree(root)
    txt = ElementTree.tostring(root)
    print(minidom.parseString(txt).toprettyxml())
    #tree.write("target.xml", encoding="UTF-8", xml_declaration=True)