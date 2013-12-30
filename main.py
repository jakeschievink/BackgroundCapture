import sys, time
import pygame, pygame.camera
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class SetupWindow(QDialog):
    def __init__(self):
        super(SetupWindow, self).__init__()
        container = QVBoxLayout()
        delayContainer = QHBoxLayout()
        numberOfPicturesContainer = QHBoxLayout()
        self.inputTimeDelay = QSpinBox();
        self.inputNumberOfPictures = QSpinBox()
        self.submitButton = QPushButton('Set Variables')
        delayContainer.addWidget(QLabel("Input Delay:"))
        delayContainer.addWidget(self.inputTimeDelay)
        numberOfPicturesContainer.addWidget(QLabel("Number Of Pictures to Take:"))
        numberOfPicturesContainer.addWidget(self.inputNumberOfPictures)
        container.addLayout(delayContainer)
        container.addLayout(numberOfPicturesContainer)
        container.addWidget(self.submitButton)
        self.setWindowTitle("Setup")
        self.setLayout(container)
        self.submitButton.clicked.connect(self.submitValues)
        self.show()
    def submitValues(self):
        numOfPictures = self.inputNumberOfPictures.value()
        delay = self.inputTimeDelay.value()
        pictureInst = PictureDameon(delay, numOfPictures)
        self.hide()
        pictureInst.start()

class PictureDameon:
    def __init__(self, delay, numOfPictures):
        self.delay = delay
        self.numOfPictures = numOfPictures
        self.camera = CameraPicture()
    def start(self):
        print "starting sleep"
        time.sleep(float(self.delay))
        self.takePicture()
    def takePicture(self):
        for i in range(0, self.numOfPictures):
            print "taking picture"
            self.camera.takePicture()
            self.camera.savePicture()
            time.sleep(1)
        self.start()

class CameraPicture:
    def  __init__(self):
        pygame.camera.init()
        self.cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
    def takePicture(self):
        self.cam.start()
        self.img = self.cam.get_image()
    def savePicture(self):
        ctime = time.localtime()
        pygame.image.save(self.img, str(ctime.tm_mon)+":"+str(ctime.tm_mday)+":"+str(ctime.tm_hour)+":"+str(ctime.tm_min)+":"+str(ctime.tm_sec)+"picture.jpg")
        self.cam.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    setup = SetupWindow()
    app.exec_()







