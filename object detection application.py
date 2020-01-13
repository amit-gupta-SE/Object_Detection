from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon,QPixmap,QImage,QPalette,QBrush
import socket
import sys
import os
import webcam
import detect_video
import detect_image
from PIL import Image
from resizeimage import resizeimage

objectDetectionApplication = QtWidgets.QApplication([])
homeScreen = uic.loadUi("first_window.ui")
imageScreen = uic.loadUi("image_window.ui")
imageScreen.back_button.setStyleSheet("background-image: url(back_image.jpeg); background-attachment: fixed")
imageScreen.convert.setPixmap(QPixmap("convertImage.png"))
homeScreen.label.setStyleSheet("background-color: rgb(238, 238, 236)")
homeScreen.label_2.setStyleSheet("background-color: rgb(238, 238, 236)")
homeScreen.centralwidget.setStyleSheet("background-image: url(bg.jpg); background-attachment: fixed")

def webcam_realtime_detection():
    homeScreen.setWindowOpacity(0.8)
    webcam.main(0.5,0.5,0)
    return

def image_detection_window():
    homeScreen.hide()
    imageScreen.original_image.setPixmap(QPixmap("empty_image.jpeg"))
    imageScreen.new_image.setPixmap(QPixmap("empty_image.jpeg"))
    imageScreen.path.setText("")
    imageScreen.show()

def image_detection():
    path = imageScreen.path.text()
    if os.path.exists(path):
       lis = path.split("/")
       name = lis[1].split(".")
       na = lis[0] + "/a" + lis[1]
       command = "convert " + path + " -resize 450x500 " + na 
       os.system(command)
       imageScreen.original_image.setPixmap(QPixmap(na))
       detect_image.main(0.5,0.5,path)
       des = "detections/a" + name[0] + "._yolo.jpg"
       imageScreen.new_image.setPixmap(QPixmap(des))
    else :
       QMessageBox.information(None, "ERROR!", "No such path exists.")

imageScreen.path.returnPressed.connect(image_detection)

def homeScreen_window():
    imageScreen.hide()
    homeScreen.show()

imageScreen.back_button.clicked.connect(homeScreen_window)

homeScreen.webcam_button.clicked.connect(webcam_realtime_detection)
homeScreen.image_button.clicked.connect(image_detection_window)

if __name__=="__main__":
    homeScreen.show()
    sys.exit(objectDetectionApplication.exec())
