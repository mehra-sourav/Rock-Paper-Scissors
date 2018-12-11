import sys,random,cv2
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication,QDialog,QLabel
from PyQt5.uic import loadUi

Stone='CPU Hand Images/Stone.jpg'
Paper='CPU Hand Images/Paper.jpg'
Scissors='CPU Hand Images/Scissors.jpg'

class Game(QDialog):
    def __init__(self):
        super(Game,self).__init__()
        loadUi('Game.ui',self)
        self.image=None
        self.start_webcam()
        self.Start.clicked.connect(self.stop_webcam)


    def start_webcam(self):
        self.capture=cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,440)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,360)


        self.timer=QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)

    def update_frame(self):
        ret,self.image=self.capture.read()
        self.image=cv2.flip(self.image,1)
        self.displayImage(self.image,1)

    def stop_webcam(self):
        self.update_frame()
        self.timer.stop()
        self.CPUGame()

    def displayImage(self,img,window=1):
        qformat=QImage.Format_Indexed8
        if len(img.shape)==3: #3 is number of channels
            if img.shape[2]==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888

        outImage=QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
        #BGR>>RGB
        outImage1=outImage.rgbSwapped()

        if window==1:
            self.Playerview.setPixmap(QPixmap.fromImage(outImage1))
            self.Playerview.setScaledContents(True)

    def CPUGame(self):
        num=random.randint(1,3)
        input=None

        #self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 440)
        #self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 360)
        if num==1:
            input='Stone'
            self.CPUview.setPixmap(QPixmap(Stone))

            #self.CPUview.setGeometry()
        if num==2:
            input='Paper'
            #self.displayImage(Paper,2)
            self.CPUview.setPixmap(QPixmap(Paper))
        if num==3:
            input='Scissors'
            #self.displayImage(Scissors,2)
            self.CPUview.setPixmap(QPixmap(Scissors))




if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Game()
    window.setWindowTitle("Rock Paper Scissor Game")
    window.show()
    sys.exit(app.exec_())



