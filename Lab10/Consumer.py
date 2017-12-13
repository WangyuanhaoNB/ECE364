import sys

from PySide.QtGui import *
from BasicUI import *
from xml.etree import ElementTree
from xml.dom import minidom


class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        #init widgets
        self.clearAll()



        #connect clear button
        self.btnClear.clicked.connect(self.clearAll)
        self.btnSave.clicked.connect(self.Save)
        self.btnLoad.clicked.connect(self.loadData)
        #if widget changed enable save btn
        self.txtStudentName.textChanged.connect(self.setSave)
        self.txtStudentID.textChanged.connect(self.setSave)

        self.txtComponentCount_1.textChanged.connect(self.setSave)
        self.txtComponentCount_2.textChanged.connect(self.setSave)
        self.txtComponentCount_3.textChanged.connect(self.setSave)
        self.txtComponentCount_4.textChanged.connect(self.setSave)
        self.txtComponentCount_5.textChanged.connect(self.setSave)
        self.txtComponentCount_6.textChanged.connect(self.setSave)
        self.txtComponentCount_7.textChanged.connect(self.setSave)
        self.txtComponentCount_8.textChanged.connect(self.setSave)
        self.txtComponentCount_9.textChanged.connect(self.setSave)
        self.txtComponentCount_10.textChanged.connect(self.setSave)
        self.txtComponentCount_11.textChanged.connect(self.setSave)
        self.txtComponentCount_12.textChanged.connect(self.setSave)
        self.txtComponentCount_13.textChanged.connect(self.setSave)
        self.txtComponentCount_14.textChanged.connect(self.setSave)
        self.txtComponentCount_15.textChanged.connect(self.setSave)
        self.txtComponentCount_16.textChanged.connect(self.setSave)
        self.txtComponentCount_17.textChanged.connect(self.setSave)
        self.txtComponentCount_18.textChanged.connect(self.setSave)
        self.txtComponentCount_19.textChanged.connect(self.setSave)
        self.txtComponentCount_20.textChanged.connect(self.setSave)

        self.txtComponentName_1.textChanged.connect(self.setSave)
        self.txtComponentName_2.textChanged.connect(self.setSave)
        self.txtComponentName_3.textChanged.connect(self.setSave)
        self.txtComponentName_4.textChanged.connect(self.setSave)
        self.txtComponentName_5.textChanged.connect(self.setSave)
        self.txtComponentName_6.textChanged.connect(self.setSave)
        self.txtComponentName_7.textChanged.connect(self.setSave)
        self.txtComponentName_8.textChanged.connect(self.setSave)
        self.txtComponentName_9.textChanged.connect(self.setSave)
        self.txtComponentName_10.textChanged.connect(self.setSave)
        self.txtComponentName_11.textChanged.connect(self.setSave)
        self.txtComponentName_12.textChanged.connect(self.setSave)
        self.txtComponentName_13.textChanged.connect(self.setSave)
        self.txtComponentName_14.textChanged.connect(self.setSave)
        self.txtComponentName_15.textChanged.connect(self.setSave)
        self.txtComponentName_16.textChanged.connect(self.setSave)
        self.txtComponentName_17.textChanged.connect(self.setSave)
        self.txtComponentName_18.textChanged.connect(self.setSave)
        self.txtComponentName_19.textChanged.connect(self.setSave)
        self.txtComponentName_20.textChanged.connect(self.setSave)

        self.chkGraduate.stateChanged.connect(self.setSave)

        self.cboCollege.currentIndexChanged.connect(self.setSave)

    def Save(self): #broken
        boxes = [
        self.txtComponentName_1,
        self.txtComponentName_2,
        self.txtComponentName_3,
        self.txtComponentName_4,
        self.txtComponentName_5,
        self.txtComponentName_6,
        self.txtComponentName_7,
        self.txtComponentName_8,
        self.txtComponentName_9,
        self.txtComponentName_10,
        self.txtComponentName_11,
        self.txtComponentName_12,
        self.txtComponentName_13,
        self.txtComponentName_14,
        self.txtComponentName_15,
        self.txtComponentName_16,
        self.txtComponentName_17,
        self.txtComponentName_18,
        self.txtComponentName_19,
        self.txtComponentName_20
        ]
        countboxes = [
        self.txtComponentCount_1,
        self.txtComponentCount_2,
        self.txtComponentCount_3,
        self.txtComponentCount_4,
        self.txtComponentCount_5,
        self.txtComponentCount_6,
        self.txtComponentCount_7,
        self.txtComponentCount_8,
        self.txtComponentCount_9,
        self.txtComponentCount_10,
        self.txtComponentCount_11,
        self.txtComponentCount_12,
        self.txtComponentCount_13,
        self.txtComponentCount_14,
        self.txtComponentCount_15,
        self.txtComponentCount_16,
        self.txtComponentCount_17,
        self.txtComponentCount_18,
        self.txtComponentCount_19,
        self.txtComponentCount_20
        ]
        with open("target.xml","w") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write("<Content>\n")
            if self.chkGraduate.isChecked():
                test = "true"
            else:
                test = "false"
            f.write('    <StudentName graduate="{}">{}</StudentName>\n'.format(test,self.txtStudentName.text()))
            f.write('    <StudentID>{}</StudentID>\n'.format(self.txtStudentID.text()))
            f.write('    <College>{}</College>\n'.format(self.cboCollege.currentText()))
            f.write('    <Components>\n')


            for index in range(len(boxes)):
                if boxes[index].text():
                    f.write('        <Component name="{}" count="{}" />\n'.format(boxes[index].text(),countboxes[index].text()))

            f.write('    </Components>\n')
            f.write('</Content>')






        # #root = ElementTree.Element('Content')
        #
        # #stu_name = ElementTree.Element("StudentName")
        # root.append(stu_name)
        # stu_name.text = self.txtStudentName.text()
        #
        # if self.chkGraduate.isChecked():
        #     stu_name.set("graduate", "true")
        # else:
        #     stu_name.set("graduate", "false")
        #
        # stu_id = ElementTree.Element("StudentID")
        # root.append(stu_id)
        # stu_id.text = self.txtStudentID.text()
        #
        # college = ElementTree.Element("College")
        # root.append(college)
        # college.text = self.cboCollege.currentText()
        #
        # comp = ElementTree.Element("Components")
        # root.append(comp)
        #
        # boxes = [
        # self.txtComponentName_1,
        # self.txtComponentName_2,
        # self.txtComponentName_3,
        # self.txtComponentName_4,
        # self.txtComponentName_5,
        # self.txtComponentName_6,
        # self.txtComponentName_7,
        # self.txtComponentName_8,
        # self.txtComponentName_9,
        # self.txtComponentName_10,
        # self.txtComponentName_11,
        # self.txtComponentName_12,
        # self.txtComponentName_13,
        # self.txtComponentName_14,
        # self.txtComponentName_15,
        # self.txtComponentName_16,
        # self.txtComponentName_17,
        # self.txtComponentName_18,
        # self.txtComponentName_19,
        # self.txtComponentName_20
        # ]
        # countboxes = [
        # self.txtComponentCount_1,
        # self.txtComponentCount_2,
        # self.txtComponentCount_3,
        # self.txtComponentCount_4,
        # self.txtComponentCount_5,
        # self.txtComponentCount_6,
        # self.txtComponentCount_7,
        # self.txtComponentCount_8,
        # self.txtComponentCount_9,
        # self.txtComponentCount_10,
        # self.txtComponentCount_11,
        # self.txtComponentCount_12,
        # self.txtComponentCount_13,
        # self.txtComponentCount_14,
        # self.txtComponentCount_15,
        # self.txtComponentCount_16,
        # self.txtComponentCount_17,
        # self.txtComponentCount_18,
        # self.txtComponentCount_19,
        # self.txtComponentCount_20
        # ]
        #
        # for index in range(len(boxes)):
        #     if boxes[index].text():
        #         temp = ElementTree.Element("Component")
        #         comp.append(temp)
        #         temp.set("count", countboxes[index].text())
        #         temp.set("name", boxes[index].text())
        #
        #
        #
        #
        #
        #
        # tree = ElementTree.ElementTree(root)
        # txt = ElementTree.tostring(root)
        #
        # #xmlstr = bytes.decode(minidom.parseString(txt).toprettyxml(encoding="UTF-8"))
        #
        # tree.write("target.xml", encoding="UTF-8", xml_declaration=True)
        # #with open("target.xml","w") as f:
        # #    f.write(xmlstr)

    def setSave(self):
        self.btnSave.setDisabled(False)
        self.btnLoad.setDisabled(True)


    def clearAll(self):
        self.txtStudentName.clear()
        self.txtStudentID.clear()

        self.txtComponentCount_1.clear()
        self.txtComponentCount_2.clear()
        self.txtComponentCount_3.clear()
        self.txtComponentCount_4.clear()
        self.txtComponentCount_5.clear()
        self.txtComponentCount_6.clear()
        self.txtComponentCount_7.clear()
        self.txtComponentCount_8.clear()
        self.txtComponentCount_9.clear()
        self.txtComponentCount_10.clear()
        self.txtComponentCount_11.clear()
        self.txtComponentCount_12.clear()
        self.txtComponentCount_13.clear()
        self.txtComponentCount_14.clear()
        self.txtComponentCount_15.clear()
        self.txtComponentCount_16.clear()
        self.txtComponentCount_17.clear()
        self.txtComponentCount_18.clear()
        self.txtComponentCount_19.clear()
        self.txtComponentCount_20.clear()

        self.txtComponentName_1.clear()
        self.txtComponentName_2.clear()
        self.txtComponentName_3.clear()
        self.txtComponentName_4.clear()
        self.txtComponentName_5.clear()
        self.txtComponentName_6.clear()
        self.txtComponentName_7.clear()
        self.txtComponentName_8.clear()
        self.txtComponentName_9.clear()
        self.txtComponentName_10.clear()
        self.txtComponentName_11.clear()
        self.txtComponentName_12.clear()
        self.txtComponentName_13.clear()
        self.txtComponentName_14.clear()
        self.txtComponentName_15.clear()
        self.txtComponentName_16.clear()
        self.txtComponentName_17.clear()
        self.txtComponentName_18.clear()
        self.txtComponentName_19.clear()
        self.txtComponentName_20.clear()

        self.chkGraduate.setChecked(False)

        self.cboCollege.setCurrentIndex(0)
        self.btnSave.setDisabled(True)
        self.btnLoad.setDisabled(False)

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.
        
        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***
        *** This method is required for unit tests! ***
        """

        boxes = [
        self.txtComponentName_1,
        self.txtComponentName_2,
        self.txtComponentName_3,
        self.txtComponentName_4,
        self.txtComponentName_5,
        self.txtComponentName_6,
        self.txtComponentName_7,
        self.txtComponentName_8,
        self.txtComponentName_9,
        self.txtComponentName_10,
        self.txtComponentName_11,
        self.txtComponentName_12,
        self.txtComponentName_13,
        self.txtComponentName_14,
        self.txtComponentName_15,
        self.txtComponentName_16,
        self.txtComponentName_17,
        self.txtComponentName_18,
        self.txtComponentName_19,
        self.txtComponentName_20
        ]
        countboxes = [
        self.txtComponentCount_1,
        self.txtComponentCount_2,
        self.txtComponentCount_3,
        self.txtComponentCount_4,
        self.txtComponentCount_5,
        self.txtComponentCount_6,
        self.txtComponentCount_7,
        self.txtComponentCount_8,
        self.txtComponentCount_9,
        self.txtComponentCount_10,
        self.txtComponentCount_11,
        self.txtComponentCount_12,
        self.txtComponentCount_13,
        self.txtComponentCount_14,
        self.txtComponentCount_15,
        self.txtComponentCount_16,
        self.txtComponentCount_17,
        self.txtComponentCount_18,
        self.txtComponentCount_19,
        self.txtComponentCount_20
        ]

        tree=ElementTree.parse(filePath)
        root=tree.getroot()

        self.txtStudentName.setText(root.find("StudentName").text)

        if (root.find("StudentName").get("graduate")) == "true":
            self.chkGraduate.setChecked(True)
        else:
            self.chkGraduate.setChecked(False)


        self.txtStudentID.setText(root.find("StudentID").text)


        index = self.cboCollege.findText(root.find("College").text, QtCore.Qt.MatchFixedString)
        self.cboCollege.setCurrentIndex(index)

        x = list((root.find("Components")).iter("Component"))

        if len(x) > len(range(20)):
            y = 20
        else:
            y = len(x)
        for index in range(y):
            boxes[index].setText(x[index].get("name"))
            countboxes[index].setText(x[index].get("count"))

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
