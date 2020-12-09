# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import os 
import subprocess 
import sys 
import tempfile 
from docopt import docopt
#import proyectos.juego_de_la_vida
#


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        Main window
        """
        MainWindow.setObjectName("Proyecto Final")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        """
        Main Panel. Contains everything inside.
        """
        
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 0, 480, 621))
        self.main_frame.setStyleSheet("background-color: rgb(61, 62, 63);")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.label = QtWidgets.QLabel(self.main_frame)
        self.label.setGeometry(QtCore.QRect(115, 80, 250, 50))
        self.label.setMaximumSize(QtCore.QSize(251, 51))
        self.label.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        """
        Push Button. Grafos
        """
        self.pushButton = QtWidgets.QPushButton(self.main_frame)
        self.pushButton.clicked.connect(self._openGrafo)
        self.pushButton.setGeometry(QtCore.QRect(40, 210, 400, 60))
        self.pushButton.setMaximumSize(QtCore.QSize(400, 60))
        self.pushButton.setStyleSheet("background-color: rgb(255, 77, 65);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")

        """
        Push Button. Conjuntos
        """
        self.pushButton_2 = QtWidgets.QPushButton(self.main_frame)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 300, 400, 60))
        self.pushButton_2.setMaximumSize(QtCore.QSize(400, 60))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 125, 0);")
        self.pushButton_2.setObjectName("pushButton_2")

        """
        Puss Button. Juego de la vida
        """
        self.pushButton_3 = QtWidgets.QPushButton(self.main_frame)
        self.pushButton_3.clicked.connect(self._openGameOfLive)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 390, 400, 60))
        self.pushButton_3.setMaximumSize(QtCore.QSize(400, 60))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        """
        Generated code. 
        """
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        All the translation needed for the demo.
        Args:
            MainWindow ([Mainwindow]): [FRAME]
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ABRAHAM EDUARDO HERNÁNDEZ FLORES"))
        self.pushButton.setText(_translate("MainWindow", "GRAFOS"))
        self.pushButton_2.setText(_translate("MainWindow", "CONJUNTOS"))
        self.pushButton_3.setText(_translate("MainWindow", "JUEGO DE LA VIDA"))

    def _openGrafo(self):
        import proyectos.grafo

    def _openConjuntos(self):
        """
        Method implemented to bind the click event of its button to the Conuntos script
        """
        print("SI LLEGO AQUI")
    
    def _openGameOfLive(self):
        """
        Method implemented to bind the click event of its button to the juego_de_la_vida script
        """
        import proyectos.juego_de_la_vida

        print("ABRAHAM EDUARDO HERNANDEZ FLORES - 160079")
        for n in range(3):
            print("."*3)

        rows, cols, per, gen = int(input("Rows-> ")), int(input("Cols-> ")), int(input("Porcentaje(30-60)->")), int(input("Numero de generaciones(10 MIN)->"))
        lives = ((rows*cols)*per)/100
        game = GameOfLife(rows, cols, float(lives), True)
        
        print (lives)

        iterations = 0
        while (game.life > 0 or game.dead > 0) and iterations != gen:
            try:        
                game.test()
                print(game)
                print("Iteración N:"+str(iterations))
                time.sleep(3)
                iterations += 1
            except KeyboardInterrupt:
                break
        print("Total: ", iterations)        

    def _openCLI(self, named_pipe, file_name):
        pass