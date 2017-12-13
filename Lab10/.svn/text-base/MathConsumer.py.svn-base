# Import PySide classes
import sys
import re
from PySide.QtCore import *
from PySide.QtGui import *
from calculator import *

class MathConsumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MathConsumer, self).__init__(parent)
        self.setupUi(self)

        self.btnCalculate.clicked.connect(self.performOperation)

    def performOperation(self):
        m = re.search(r"^([-+]?([0-9]+\.[0-9]*)|(\.[0-9]+))$", self.edtNumber1.text())

        if m:
            k = re.search(r"^([-+]?([0-9]+\.[0-9]*)|(\.[0-9]+))$", self.edtNumber2.text())

            if k:
                op1 = float(self.edtNumber1.text())
                op2 = float(self.edtNumber2.text())
                if(self.cboOperation.currentText() == "+"):
                    res = op1 + op2
                elif (self.cboOperation.currentText() == "-"):
                    res = op1 - op2
                elif (self.cboOperation.currentText() == "*"):
                    res = op1 * op2
                else:
                    res = op1 / op2

                self.edtResult.setText(str(res))
            else:
                k1 = re.search(r"^([-+]?[0-9]+)$", self.edtNumber2.text())

                if k1:
                    op1 = float(self.edtNumber1.text())
                    op2 = int(self.edtNumber2.text())
                    if(self.cboOperation.currentText() == "+"):
                        res = op1 + op2
                    elif (self.cboOperation.currentText() == "-"):
                        res = op1 - op2
                    elif (self.cboOperation.currentText() == "*"):
                        res = op1 * op2
                    else:
                        res = op1 / op2

                    self.edtResult.setText(str(res))
                else:
                    self.edtResult.setText("E")
        else:
            m1 = re.search(r"^([-+]?[0-9]+)$", self.edtNumber1.text())

            if m1:
                k = re.search(r"^([-+]?([0-9]+\.[0-9]*)|(\.[0-9]+))$", self.edtNumber2.text())

                if k:
                    op1 = int(self.edtNumber1.text())
                    op2 = float(self.edtNumber2.text())
                    if(self.cboOperation.currentText() == "+"):
                        res = op1 + op2
                    elif (self.cboOperation.currentText() == "-"):
                        res = op1 - op2
                    elif (self.cboOperation.currentText() == "*"):
                        res = op1 * op2
                    else:
                        res = op1 / op2

                    self.edtResult.setText(str(res))
                else:
                    k1 = re.search(r"^([-+]?[0-9]+)$", self.edtNumber2.text())

                    if k1:
                        op1 = int(self.edtNumber1.text())
                        op2 = int(self.edtNumber2.text())
                        if(self.cboOperation.currentText() == "+"):
                            res = op1 + op2
                        elif (self.cboOperation.currentText() == "-"):
                            res = op1 - op2
                        elif (self.cboOperation.currentText() == "*"):
                            res = op1 * op2
                        else:
                            res = op1 / op2

                        self.edtResult.setText(str(res))
                    else:
                        self.edtResult.setText("E")
            else:
                self.edtResult.setText("E")



if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = MathConsumer()

    currentForm.show()
    currentApp.exec_()

