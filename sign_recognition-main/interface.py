from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys
import os
import pygame



class HandTrackingAppInterface(QMainWindow):
    def __init__(self):
        super(HandTrackingAppInterface, self).__init__()

        # Configurar la ventana principal
        self.setWindowTitle("Ajuste Audio")
        self.setGeometry(150, 100, 800, 600)
        self.setFixedWidth(700)
        self.setFixedHeight(500)

        # Agregar un fondo a la ventana
        background_label = QLabel(self)
        pixmap = QPixmap("fondo.png")  
        background_label.setPixmap(pixmap)
        background_label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(background_label)

        # Crea el objeto para el logoo
        image_label = QLabel(self)
         # Establesemos la iamgen
        pixmap = QPixmap("logo.png")
        image_label.setPixmap(pixmap)
        image_label.setGeometry(250,100,200,200)
        
        # Inicializar pygame y cargar la música
        pygame.init()
        pygame.mixer.music.load('music.wav') 

        # Reproducir la música (opcionalmente en bucle)
        pygame.mixer.music.play(-1) 

        # Agregar un botón para ejecutar el script
        self.btnRunScript = QPushButton("Abrir camara", self)
        self.btnRunScript.setGeometry(250, 350, 200, 50)
        self.btnRunScript.clicked.connect(self.run_script)
        self.btnRunScript.setStyleSheet("background-color: #fdbb2d;")

    
  
    def run_script(self):
        # Ocultar la interfaz
        self.hide()

        # Ejecutar el script principal
        os.system("python code.py")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    interface = HandTrackingAppInterface()
    interface.show()
    sys.exit(app.exec_())
