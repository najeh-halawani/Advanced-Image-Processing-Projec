# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFileDialog
from emotionDetection.emotion_recognition import image_emotion
from emotionDetection.video_emotion_recognition import video_emotion
from facemaskdetection.facemaskdetection import *
from adaptivethresholding.adaptiveThreshholding import *
from plateDetection.detectImageVideo import *
from plateDetection.detectImage import *
from textDetection.textDetection import *
from faceDetection.main import *

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Image Processing Project"
        description = "The Swiss Knife of Image Processing"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.btn_exit.clicked.connect(self.buttonClick)
        widgets.pushButton_3.clicked.connect(self.buttonClick)
        widgets.pushButton_2.clicked.connect(self.buttonClick)
        widgets.pushButton_4.clicked.connect(self.buttonClick)
        widgets.pushButton.clicked.connect(self.buttonClick)
        widgets.btn_imgEnhancement.clicked.connect(self.buttonClick)
        widgets.btn_extract.clicked.connect(self.buttonClick)
        widgets.pushButton_13.clicked.connect(self.buttonClick)
        widgets.pushButton_14.clicked.connect(self.buttonClick)
        
        
        # Emotion Detection Functions
        
        widgets.pushButton_10.clicked.connect(self.emotion_openCamera)
        widgets.pushButton_9.clicked.connect(self.emotion_uploadfile)
        
        
        # Mask Detection Functions
        
        widgets.pushButton_12.clicked.connect(self.FaceMaskOpenCamera)
        
        
        # Image Enhancement 
        
        widgets.pushButton_18.clicked.connect(self.enhancement_upload)
        
        
        # License Plate Detection
        
        widgets.pushButton_5.clicked.connect(self.plateDetectionOpenCamera)
        widgets.pushButton_6.clicked.connect(self.plateDetectionUpload)
        
        
        # Text Detection
        
        widgets.pushButton_15.clicked.connect(self.textExtraction)
        
        # Face Recognition
        
        widgets.pushButton_8.clicked.connect(self.faceRecognition)
        
        
        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget_3.setCurrentWidget(widgets.homePage)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "pushButton_3":
            widgets.stackedWidget_3.setCurrentWidget(widgets.FaceRecognition)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        
        if btnName == "pushButton_2":
            widgets.stackedWidget_3.setCurrentWidget(widgets.PlateDetection)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        
        if btnName == "pushButton_4":
            widgets.stackedWidget_3.setCurrentWidget(widgets.EmotionDetection)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "pushButton":
            widgets.stackedWidget_3.setCurrentWidget(widgets.MaskDetection)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        
        if btnName == "pushButton_14":
            widgets.stackedWidget_3.setCurrentWidget(widgets.texttoImgPage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))


        if btnName == "pushButton_13":
            widgets.stackedWidget_3.setCurrentWidget(widgets.ImageEnhancement)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))



        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget_3.setCurrentWidget(widgets.homePage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget_3.setCurrentWidget(widgets.FaceRecognition)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget_3.setCurrentWidget(widgets.PlateDetection) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_save":
            widgets.stackedWidget_3.setCurrentWidget(widgets.EmotionDetection) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
            
        if btnName == "btn_exit":
            widgets.stackedWidget_3.setCurrentWidget(widgets.MaskDetection) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
            
                 
        if btnName == "btn_extract":
            widgets.stackedWidget_3.setCurrentWidget(widgets.texttoImgPage) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
        
        if btnName == "btn_imgEnhancement":
            widgets.stackedWidget_3.setCurrentWidget(widgets.ImageEnhancement) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
            
    def emotion_openCamera(self):
        video_emotion()

    def emotion_uploadfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'c\\', 'Image files (*.jpg *.png *jpeg)')
        imagePath = fname[0]
        image_emotion(imgPath=imagePath)

    def FaceMaskOpenCamera(self):
        MaskDetection()
        
    def enhancement_upload(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'c\\', 'Image files (*.jpg *.png *jpeg)')
        imagePath = fname[0]
        adaptveThreshholding(imagePath)
    
    def plateDetectionOpenCamera(self):
        PlateDetection()
        
    def plateDetectionUpload(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'c\\', 'Image files (*.jpg *.png *jpeg)')
        imagePath = fname[0]
        detectPlate(imagePath)
        
    def textExtraction(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'c\\', 'Image files (*.jpg *.png *jpeg)')
        imagePath = fname[0]
        res = textDetection(imagePath)
        widgets.label_15.setText("Extracted Text: "+ res)
        
    def faceRecognition(self):
        run()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
