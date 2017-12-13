# Import PySide classes
import sys
import re
from PySide.QtCore import *
from PySide.QtGui import *
from SteganographyGUI import *
from Steganography import *

import imageio
import scipy.misc


class Processor(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Processor, self).__init__(parent)
        self.setupUi(self)

        #initialize member variables
        self.payload_1_image = None
        self.payload_1_path = ""
        self.payload_1 = None

        self.carrier_1_path = ""
        self.size_carrier = 0
        self.carrier_1_image = None
        self.carrier_1 = None

        self.carrier_2_path = ""
        self.carrier_2_image = None
        self.carrier_2 = None



        #accept drops for this QWidget
        self.setAcceptDrops(True)

        #views that need drag drop functionality
        views = [self.viewPayload1,
                 self.viewCarrier1,
                 self.viewCarrier2]

        for view in views:
            view.dragEnterEvent = self.accept2
            view.dragMoveEvent = self.accept2
            view.dragLeaveEvent = self.accept2

            if view is self.viewPayload1:
                view.dropEvent = self.payload_drop_1

            elif view is self.viewCarrier1:
                view.dropEvent = self.carrier_drop_1

            elif view is self.viewCarrier2:
                view.dropEvent = self.carrier_drop_2

        self.chkApplyCompression.stateChanged.connect(self.compress_changed)
        self.slideCompression.valueChanged.connect(self.slide_changed)
        self.chkOverride.stateChanged.connect(self.embed_is_gtg)

        #buttons yo
        self.btnSave.clicked.connect(self.save_tab1)
        self.btnExtract.clicked.connect(self.extract_tab2)
        self.btnClean.clicked.connect(self.clean_tab2)

    def extract_tab2(self):

        new_payload = self.carrier_2.extractPayload()
        #y = imageio.imread("payload2.png")
        scipy.misc.toimage(new_payload.rawData).save("test_extract.png")
        #scipy.misc.imsave("test_extract.png", new_payload)

        scene = QGraphicsScene()
        image = QPixmap("test_extract.png")
        image = image.scaled(359, 280, Qt.KeepAspectRatio)
        scene.addPixmap(image)
        self.viewPayload2.setScene(scene)
        self.viewPayload2.show()
        #new_img = new_payload.rawData
        #height, width, channel = new_img.shape
        #bytesPerLine = 3 * width
        #qImg = QImage(new_img.data, width, height, bytesPerLine, QImage.Format_RGB888)

        #scene = QGraphicsScene()
        #image = QPixmap(qImg)
        #image = image.scaled(359, 280, Qt.KeepAspectRatio)
        #scene.addPixmap(image)
        #self.viewPayload2.setScene(scene)
        #self.viewPayload2.show()

    def clean_tab2(self):
        cleaned_carrier = self.carrier_2.clean()
        scipy.misc.imsave(self.carrier_2_path, cleaned_carrier)

        self.carrier_2_image = imageio.imread(self.carrier_2_path)
        #convert numpy array to carrier instance
        self.carrier_2 = Carrier(self.carrier_2_image)


        if (self.carrier_2.payloadExists()):
            self.lblCarrierEmpty.clear()
            self.btnClean.setEnabled(True)
            self.btnExtract.setEnabled(True)
        else:
            self.lblCarrierEmpty.setText(">>>>Carrier Empty<<<<") #?
            self.btnClean.setEnabled(False)
            self.btnExtract.setEnabled(False)

        self.viewPayload2.setScene(None) #clears old payload view

        scene = QGraphicsScene()
        image = QPixmap(self.carrier_2_path)
        image = image.scaled(359, 280, Qt.KeepAspectRatio)
        scene.addPixmap(image)
        self.viewCarrier2.setScene(scene)
        self.viewCarrier2.show()

    def save_tab1(self):
        #get users filename
        filepath, trash = QFileDialog.getSaveFileName(self, caption='Save to Following Location', filter="Png Files (*.png)")
        if filepath:
            new_carrier = self.carrier_1.embedPayload(self.payload_1, True) #always embed at this point
            scipy.misc.imsave(filepath, new_carrier)




    def compress_changed(self):
        if (self.chkApplyCompression.isChecked() ):
            self.lblLevel.setEnabled(True)
            self.slideCompression.setEnabled(True)
            self.txtCompression.setEnabled(True)

            self.txtCompression.setText(str(self.slideCompression.value()))


            #convert numpy array to payload instance
            self.payload_1 = Payload(self.payload_1_image, compressionLevel=self.slideCompression.value())
            #get length json of new payload and set to text box
            self.txtPayloadSize.setText(str(len(self.payload_1.json)))

        else:
            self.lblLevel.setEnabled(False)
            self.slideCompression.setEnabled(False)
            self.txtCompression.setEnabled(False)


            #convert numpy array to payload instance
            self.payload_1 = Payload(self.payload_1_image)
            #get length json of new payload and set to text box
            self.txtPayloadSize.setText(str(len(self.payload_1.json)))

        self.embed_is_gtg()

    def slide_changed(self):

        self.txtCompression.setText(str(self.slideCompression.value()))


        #convert numpy array to payload instance
        self.payload_1 = Payload(self.payload_1_image, compressionLevel=self.slideCompression.value())
        #get length json of new payload and set to text box
        self.txtPayloadSize.setText(str(len(self.payload_1.json)))

        #To do call check save enabled
        self.embed_is_gtg()

    def embed_is_gtg(self):
        if ((self.payload_1 != None) and (self.carrier_1 != None)):
            if (int(self.txtCarrierSize.text()) >= int(self.txtPayloadSize.text())):
                if(self.carrier_1.payloadExists() and self.chkOverride.isChecked()):
                    self.btnSave.setEnabled(True)
                elif( (not self.carrier_1.payloadExists()) ):
                    self.btnSave.setEnabled(True)
                else:
                    self.btnSave.setEnabled(False)
            else:
                self.btnSave.setEnabled(False)
        else:
            self.btnSave.setEnabled(False)



    def accept(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()
    def accept2(self, e):
        e.accept()

    def payload_drop_1(self, e):

        if e.mimeData().hasUrls:
            urllist =  e.mimeData().urls()
            path1 = (urllist[0]).toLocalFile()

            m = re.search(r"^.*?\.png$",path1)

            if not m:
                return

            #save path to var
            self.payload_1_path = path1

            #convert image path to numpy array
            self.payload_1_image = imageio.imread(self.payload_1_path)
            #convert numpy array to payload instance
            self.payload_1 = Payload(self.payload_1_image)
            #get length json of new payload and set to text box
            self.txtPayloadSize.setText(str(len(self.payload_1.json)))

            #uncheck compression box
            self.chkApplyCompression.setChecked(False)
            #disable compression widgets
            self.slideCompression.setValue(0)
            self.slideCompression.setEnabled(False)
            self.txtCompression.setText("0")
            self.txtCompression.setEnabled(False)
            self.lblLevel.setEnabled(False)


            self.embed_is_gtg()

            scene = QGraphicsScene()
            image = QPixmap(path1)
            image = image.scaled(359, 280, Qt.KeepAspectRatio)
            scene.addPixmap(image)
            self.viewPayload1.setScene(scene)
            self.viewPayload1.show()




        else:
            e.ignore()

    def carrier_drop_1(self, e):
        if e.mimeData().hasUrls:
            urllist =  e.mimeData().urls()
            path1 = (urllist[0]).toLocalFile()

            m = re.search(r"^.*?\.png$",path1)

            if not m:
                return

            #save path to var
            self.carrier_1_path = path1

            #convert image path to numpy array
            self.carrier_1_image = imageio.imread(self.carrier_1_path)
            #convert numpy array to carrier instance
            self.carrier_1 = Carrier(self.carrier_1_image)
            row,col,dim = self.carrier_1.img.shape
            self.size_carrier = row*col
            #get length json of new payload and set to text box
            self.txtCarrierSize.setText(str(self.size_carrier))

            if (self.carrier_1.payloadExists()):
                self.lblPayloadFound.setText(">>>>Payload Found<<<<") #?
                self.chkOverride.setEnabled(True)
            else:
                self.chkOverride.setChecked(False)
                self.chkOverride.setEnabled(False)
                self.lblPayloadFound.clear()


            self.embed_is_gtg()

            scene = QGraphicsScene()
            image = QPixmap(path1)
            image = image.scaled(359, 280, Qt.KeepAspectRatio)
            scene.addPixmap(image)
            self.viewCarrier1.setScene(scene)
            self.viewCarrier1.show()




        else:
            e.ignore()

    def carrier_drop_2(self, e):
        if e.mimeData().hasUrls:
            urllist =  e.mimeData().urls()
            path1 = (urllist[0]).toLocalFile()

            m = re.search(r"^.*?\.png$",path1)

            if not m:
                return

            #save path to var
            self.carrier_2_path = path1

            #convert image path to numpy array
            self.carrier_2_image = imageio.imread(self.carrier_2_path)
            #convert numpy array to carrier instance
            self.carrier_2 = Carrier(self.carrier_2_image)


            if (self.carrier_2.payloadExists()):
                self.lblCarrierEmpty.clear()
                self.btnClean.setEnabled(True)
                self.btnExtract.setEnabled(True)
            else:
                self.lblCarrierEmpty.setText(">>>>Carrier Empty<<<<") #?
                self.btnClean.setEnabled(False)
                self.btnExtract.setEnabled(False)

            self.viewPayload2.setScene(None) #clears old payload view

            scene = QGraphicsScene()
            image = QPixmap(path1)
            image = image.scaled(359, 280, Qt.KeepAspectRatio)
            scene.addPixmap(image)
            self.viewCarrier2.setScene(scene)
            self.viewCarrier2.show()




        else:
            e.ignore()








if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Processor()

    currentForm.show()
    currentApp.exec_()
