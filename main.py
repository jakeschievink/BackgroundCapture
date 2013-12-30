import sys, time
import pygame, pygame.camera
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class SetupWindow(QDialog):
    def __init__(self):
        super(SetupWindow, self).__init__()
        container = QVBoxLayout()
        hcontainer = QHBoxLayout()
        self.inputTimeDelay = QLineEdit("Delay");
        self.inputNumberOfPictures = QLineEdit("Number of Pictures");
        self.submitButton = QPushButton('Set Variables')
        hcontainer.addWidget(QLabel("Input Delay:"))
        hcontainer.addWidget(self.inputTimeDelay)
        container.addLayout(hcontainer)
        container.addWidget(self.inputNumberOfPictures)
        container.addWidget(self.submitButton)
        self.setLayout(container)
        self.show()


class CameraPicture():
    def  __init__(self):
        pygame.camera.init()
        self.cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
    def takePicture():
        cam.start()
        img = self.cam.get_image()
    def savePicture():
        ctime = time.localtime()
        pygame.image.save(img, str(ctime.tm_mon)+":"+str(ctime.tm_day)+":"+str(ctime.tm_hour)+":"+str(ctime.tm_min)+":"+str(ctime.tm_sec)+"picture.jpg")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    setup = SetupWindow()
    app.exec_()







