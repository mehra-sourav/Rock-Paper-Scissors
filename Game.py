import sys,random,cv2,io
from PyQt5.QtCore import QBuffer, QTimer, QCoreApplication
from PyQt5.QtGui import QPixmap, QImage,QColor
from PyQt5.QtWidgets import QApplication,QDialog,QLabel
from PyQt5.uic import loadUi
import numpy as np
from PIL import Image
from Predict import Prediction

Stone='CPU Hand Images/New Stone.jpg'
Paper='CPU Hand Images/New Paper.jpg'
Scissors='CPU Hand Images/New Scissors.jpg'

class Game(QDialog):
    CPUScore=0
    PlayerScore=0
    def __init__(self):
        super(Game,self).__init__()
        loadUi('Game.ui',self)
        self.image=None
        self.start_webcam()
        self.Start.clicked.connect(self.stop_webcam)

        # QUITING GAME
        self.Quit.clicked.connect(self.close)
        #CPUScore = 0
        #PlayerScore = 0
        #self.CPUScore.setText("CPU Score:{}".format(CPUScore))
        #self.PlayerScore.setText("CPU Score:{}".format(PlayerScore))

    #class CPU:
     #   CPUScore=0

    #class Player:
        #PlayerScore=0

    #STARTING WEBCAM
    def start_webcam(self):
        self.capture=cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,300)


        self.timer=QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)

    #UPDATING FRAMES
    def update_frame(self,i=0):
        ret,self.image=self.capture.read()
        #self.image=cv2.flip(self.image,1)
        if i==0:
         self.displayLive(self.image,1)
        elif i==1:
         self.displayPlayer(self.image,1)

    def stop_webcam(self):
        self.update_frame(1)
        qformat = QImage.Format_Indexed8
        ret,img=self.capture.read()
        if len(img.shape) == 3:  # 3 is number of channels
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        Playerinput = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        # BGR>>RGB
        #Playerinput = Playerinput.rgbSwapped()
        #img=img.rgbSwapped()
        self.CPUGame(img)

    #LIVE DISPLAY
    def displayLive(self,img,window=1):
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
            self.Liveview.setPixmap(QPixmap.fromImage(outImage1))
            self.Liveview.setScaledContents(True)

    #PLAYER INPUT DISPLAY
    def displayPlayer(self,img,window=1):
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

    #GAME START
    def CPUGame(self,Playerinput): #Playerinput is image of player input
        num=random.randint(1,3)
        CPUinput=None

        typea=type(Playerinput)

        np.save('INPUTARRAY.npy',Playerinput)


        result=None
        self.CPUScore.setText("CPU Score:{}".format(Game.CPUScore))
        self.PlayerScore.setText("CPU Score:{}".format(Game.PlayerScore))
        #self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 440)
        #self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 360)
        if num==1:
            CPUinput="Stone"
            self.CPUview.setPixmap(QPixmap(Stone))
            self.CPUoutput.setText("CPU Output:Stone")
            #self.CPUoutput.setText(str(typea))
            self.CPUview.setScaledContents(True)
            #self.CPUview.setGeometry()
        if num==2:
            CPUinput="Paper"
            self.CPUview.setPixmap(QPixmap(Paper))
            self.CPUoutput.setText("CPU Output:Paper")
            self.CPUview.setScaledContents(True)
        if num==3:
            CPUinput="Scissors"
            self.CPUview.setPixmap(QPixmap(Scissors))
            self.CPUoutput.setText("CPU Output:Scissors")#CPU Output:{CPUinput}".format(CPUinput))
            self.CPUview.setScaledContents(True)

        Playerinput=Prediction()#Playerinput)
        self.Playeroutput.setText("Player Output: {}".format(Playerinput))
        #GAME CONDITIONS
        if CPUinput=='Stone' and Playerinput=='Scissors':
            self.Result.setText("Result:CPU WINS")
            Game.CPUScore+=1
            self.CPUScore.setText("CPU Score: {}".format(Game.CPUScore))
        elif CPUinput=='Stone' and Playerinput=='Paper':
            #result="Player Wins"
            self.Result.setText("Result:PLAYER WINS")
            Game.PlayerScore+=1
            self.PlayerScore.setText("Player Score: {}".format(Game.PlayerScore))
        elif CPUinput=='Paper' and Playerinput=='Stone':
            #result="CPU Wins"
            self.Result.setText("Result:CPU WINS")
            Game.CPUScore+=1
            self.CPUScore.setText("CPU Score: {}".format(Game.CPUScore))
        elif CPUinput=='Paper' and Playerinput=='Scissors':
            #result="Player Wins"
            self.Result.setText("Result:PLAYER WINS")
            Game.PlayerScore+=1
            self.PlayerScore.setText("Player Score: {}".format(Game.PlayerScore))
        elif CPUinput=='Scissors' and Playerinput=='Paper':
            #result="CPU Wins"
            self.Result.setText("Result:CPU WINS")
            Game.CPUScore+=1
            self.CPUScore.setText("CPU Score: {}".format(Game.CPUScore))
        elif CPUinput=='Scissors' and Playerinput=='Stone':
            #result="Player Wins"
            self.Result.setText("Result:PLAYER WINS")
            Game.PlayerScore+=1
            self.PlayerScore.setText("Player Score: {}".format(Game.PlayerScore))
        elif CPUinput==Playerinput:
            self.Result.setText("Result:DRAW")
        elif Playerinput==None:
            self.Result.setText("Result:Player Input not Available")

    #QUITING GAME
    #def Quit(self):
        #self.Quit.clicked.connect(self.QCoreApplication.instance().quit)



if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Game()
    window.setWindowTitle("Rock Paper Scissor Game")
    window.show()
    sys.exit(app.exec_())



