#------------------------------------------------- -----------------------------------------#
"""                                      GUI                                                """
#------------------------------------------------------------------------------------------#

# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Musical_Instruments(object):
    def setupUi(self, Musical_Instruments):
        
        Musical_Instruments.setWindowTitle("Virtual musical instruments")
        Musical_Instruments.setObjectName("Musical_Instruments")
        Musical_Instruments.resize(659, 421)
        self.mw=Musical_Instruments
        self.centralwidget = QtWidgets.QWidget(Musical_Instruments)
        self.centralwidget.setObjectName("centralwidget")
        self.btnArray2=[]
        self.list=["B","A","G","F","E","D","C","E2","C5","D2","c40"
                   ,"f40","g40","d50","c50","a40","C4"]
        i=0
        while i < 17:
                self.btn = QtWidgets.QPushButton(self.centralwidget)
                self.btn.setSizeIncrement(40,20)
                self.btn.setText("")
                self.btn.setObjectName(self.list[i])
                self.btnArray2.append(self.btn)
                i+=1



        
        self.btnArray2[16].setGeometry(QtCore.QRect(20, 30, 41, 181))
        self.btnArray2[16].setStyleSheet("#c4{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#c4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
       
        self.btnArray2[5].setGeometry(QtCore.QRect(60, 30, 41, 181))
        self.btnArray2[5].setStyleSheet("#d4{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#d4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
       
        self.btnArray2[10].setGeometry(QtCore.QRect(40, 30, 31, 111))
        self.btnArray2[10].setStyleSheet("#c40{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#c40:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        
        self.btnArray2[6].setGeometry(QtCore.QRect(80, 30, 31, 111))
        self.btnArray2[6].setStyleSheet("#d40{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#d40:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        
        self.btnArray2[4].setGeometry(QtCore.QRect(100, 30, 41, 181))
        self.btnArray2[4].setStyleSheet("#e4{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#e4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")

        self.btnArray2[3].setGeometry(QtCore.QRect(140, 30, 41, 181))
        self.btnArray2[3].setStyleSheet("#f4{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#f4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        
        self.btnArray2[2].setGeometry(QtCore.QRect(180, 30, 41, 181))
        self.btnArray2[2].setStyleSheet("#g4{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#g4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        
        self.btnArray2[1].setGeometry(QtCore.QRect(220, 30, 41, 181))
        self.btnArray2[1].setStyleSheet("#a4{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#a4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        
        self.btnArray2[0].setGeometry(QtCore.QRect(260, 30, 41, 181))
        self.btnArray2[0].setStyleSheet("#b4{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#b4:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        
        self.btnArray2[8].setGeometry(QtCore.QRect(300, 30, 41, 181))
        self.btnArray2[8].setStyleSheet("#c5{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#c5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
        
        self.btnArray2[9].setGeometry(QtCore.QRect(340, 30, 41, 181))
        self.btnArray2[9].setStyleSheet("#d5{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#d5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
       
        self.btnArray2[7].setGeometry(QtCore.QRect(380, 30, 41, 181))
        self.btnArray2[7].setStyleSheet("#e5{\n"
"background-color: rgb(242, 242, 242);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#e5:pressed{\n"
"background-color: rgb(250, 250, 250);\n"
"\n"
"}")
       
        self.btnArray2[11].setGeometry(QtCore.QRect(160, 30, 31, 111))
        self.btnArray2[11].setStyleSheet("#f40{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#f40:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")

        self.btnArray2[12].setGeometry(QtCore.QRect(200, 30, 31, 111))
        self.btnArray2[12].setStyleSheet("#g40{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#g40:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        
        self.btnArray2[15].setGeometry(QtCore.QRect(240, 30, 31, 111))
        self.btnArray2[15].setStyleSheet("#a40{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#a40:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        
        self.btnArray2[14].setGeometry(QtCore.QRect(320, 30, 31, 111))
        self.btnArray2[14].setStyleSheet("#c50{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#c50:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        
        self.btnArray2[13].setGeometry(QtCore.QRect(360, 30, 31, 111))
        self.btnArray2[13].setStyleSheet("#d50{\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#d50:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        
      
        self.btnArray2[16].raise_()
        self.btnArray2[5].raise_()
        self.btnArray2[10].raise_()
        self.btnArray2[4].raise_()
        self.btnArray2[3].raise_()
        self.btnArray2[6].raise_()
        self.btnArray2[2].raise_()
        self.btnArray2[1].raise_()
        self.btnArray2[0].raise_()
        self.btnArray2[8].raise_()
        self.btnArray2[9].raise_()
        self.btnArray2[7].raise_()
        self.btnArray2[11].raise_()
        self.btnArray2[12].raise_()
        self.btnArray2[15].raise_()
        self.btnArray2[14].raise_()
        self.btnArray2[13].raise_()
       


#**********************************************************************************
        i=0 
        self.btnArray=[]
        list=["noteA","noteB","noteG","noteD","noteE","noteE2","C_major","G_major","A_minor","E_minor"]
        while i < 10 : 
            self.btn = QtWidgets.QPushButton(self.centralwidget)
            self.btn.setSizeIncrement(40,20)
            self.btn.setText(list[i])
            self.btn.setObjectName(list[i])
            self.btn.raise_()
            self.btnArray.append(self.btn)
            i+=1
        self.btnArray[0].raise_()
        
        self.btnArray[0].setGeometry(QtCore.QRect(150, 270, 75, 23))
        self.btnArray[1].setGeometry(QtCore.QRect(150, 300, 75, 23))
        self.btnArray[2].setGeometry(QtCore.QRect(150, 330, 75, 23))
        self.btnArray[3].setGeometry(QtCore.QRect(150, 360, 75, 23))
        self.btnArray[4].setGeometry(QtCore.QRect(290, 270, 75, 23))
        self.btnArray[5].setGeometry(QtCore.QRect(290, 300, 75, 23))
        self.btnArray[6].setGeometry(QtCore.QRect(290, 330, 75, 23))
        self.btnArray[7].setGeometry(QtCore.QRect(400, 270, 75, 23))
        self.btnArray[8].setGeometry(QtCore.QRect(400, 300, 75, 23))
        self.btnArray[9].setGeometry(QtCore.QRect(400, 330, 75, 23))
#******************************************************************************************    
        self.combo = QtWidgets.QComboBox(self.centralwidget)
        self.combo.setGeometry(QtCore.QRect(150, 240, 101, 22))
        list=["select ","1" ,"2" ,"3" , "4","5","6 "]
        self.combo.raise_()
        self.combo.addItems(list)
        self.combo.setObjectName("combo")

        Musical_Instruments.setCentralWidget(self.centralwidget)
       


#***************************************************************************************
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Musical_Instruments = QtWidgets.QMainWindow()
    ui = Ui_Musical_Instruments()
    ui.setupUi(Musical_Instruments)
    Musical_Instruments.show()
    sys.exit(app.exec_())


#------------------------------------------------------------------------------------------------#
"""                                           THE END                                           """
#------------------------------------------------------------------------------------------------#