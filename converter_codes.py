from convert_mask2txt import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QIntValidator
import cv2
from glob import glob
import os
from pathlib import Path

class Converter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit_classId.setValidator(QIntValidator(0,10000,self))
        self.ui.pushButton_start.clicked.connect(self.convert_Mask_to_JSON)
        self.ui.pushButton_maskpath.clicked.connect(self.clickbuton_dataMaskPath)
        self.ui.pushButton_outputpath.clicked.connect(self.clickbuton_dataJSONPath)



# ====== When the user clicks the "add" button in the Mask Path section, they will select the page path. ================
    def clickbuton_dataMaskPath(self):
        options = QFileDialog.Options()
        self.fileName = QFileDialog.getExistingDirectory(self, "Select Mask Path", "" ,options=options)
        if self.fileName:
            self.ui.lineEdit_maskpath.setText(self.fileName)

# ====== When the user clicks the "add" button in the output Path section, they will select the page path. ================
    def clickbuton_dataJSONPath(self):
        options = QFileDialog.Options()
        self.fileName = QFileDialog.getExistingDirectory(self, "Select Output Path", "" ,options=options)
        if self.fileName:
            self.ui.lineEdit_outputpath.setText(self.fileName)


# ============== Başlat butonuna basıldığında convert işleminin yapılacığı yer. ==============
    def convert_Mask_to_JSON(self):

        # if mask path empty show error mesage window
        if self.ui.lineEdit_maskpath.displayText() == "":
            QMessageBox.warning(self, "Warning", "Mask Path is empty.")
            return
        
        # if output path empty show error mesage window
        if self.ui.lineEdit_outputpath.displayText() == "":
            QMessageBox.warning(self, "Warning", "Output Path is empty.")
            return
        
        # if class id empty default class id = 0
        if self.ui.lineEdit_classId.displayText() == "":
            class_id = 0
        else:
            class_id = int(self.ui.lineEdit_classId.displayText())


        # Gets the path of all files in mask path.
        img_paths = glob(f"{self.ui.lineEdit_maskpath.displayText()}/*")
        img_paths = [file for file in img_paths if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

        count = 0
        self.ui.progressBar.setMaximum(len(img_paths))

        # for each image in the mask path
        for img_path in img_paths:
            count +=1

            # progress bar
            self.ui.progressBar.setValue(count)
        
            # -------- read image and get width and height ----------------
            img = cv2.imread(img_path)
            width = img.shape[1]
            height = img.shape[0]

            kopya = img.copy()
            kopya = cv2.cvtColor(kopya, cv2.COLOR_RGB2GRAY)

            # -------- get contours ----------------
            blur = cv2.cv2.GaussianBlur(kopya,(5,5),0)
            thresh = cv2.threshold(blur,10,255,cv2.THRESH_BINARY)[1]
            kontur_1 = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

            if len(kontur_1[0]) == 1:

                kontur = kontur_1[0:-1][0][0]

                x_list = [[]]
                y_list = [[]]
                for num, i in enumerate(kontur):
                    x_list[0].append(kontur[num][0][0])
                    y_list[0].append(kontur[num][0][1])

            elif len(kontur_1[0]) > 1:

                kontur = kontur_1[0:-1][0]
                x_list = []
                y_list = []

                for i in range(len(kontur)):
                    kontur_2 = kontur[i]
                    xara_list = []
                    yara_list = []

                    for num, i in enumerate(kontur_2):
                        xara_list.append(kontur_2[num][0][0])
                        yara_list.append(kontur_2[num][0][1])

                    x_list.append(xara_list)
                    y_list.append(yara_list)
            
            # -------- get image name ----------------
            name = img_path.replace("\\","/").split("/")[-1]
            name, extantion = os.path.splitext(name)

            # -------- create txt file ----------------
        
            output_path = os.path.join(self.ui.lineEdit_outputpath.displayText(), "labels")
            output_path = Path(output_path)
            output_path.mkdir(parents=True, exist_ok=True)

            f = open(f"{output_path}/{name}.txt", "w")
            f.close()

            # -------- write coordinates in txt file ----------------
            for i in range(len(x_list)):
                f = open(f"{output_path}/{name}.txt", "a")
                f.write(str(class_id)) # class id
                for j in range(len(x_list[i])):
                    # coordinates
                    f.write(f" {round(x_list[i][j]/width,4)} {round(y_list[i][j]/height,4)} ")
                    
                f.write("\n")   
                f.close()


        self.ui.statusbar.showMessage('Progress Finished',3000)
        self.ui.statusbar.setStyleSheet('color:rgb(0,128,0);font-weight:bold')


