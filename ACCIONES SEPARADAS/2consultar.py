
from asyncio.windows_events import NULL
import sys
from PyQt5 import uic
import pandas as pd
from programa.bd import ConexionBD
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class MyWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


#AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","vacunacion")
        self.cursor = self.con.cursor()
        
        
        #CARGAR EL ARCHIVO .UI
        uic.loadUi("D:/POO/PROYECTO_FINAL/Ventanas/paciente_consultar.ui", self)
        self.setWindowTitle("CONSULTAR PACIENTE")  
        
        #ASIGNA  EVENTOS A BOTONES
    
        #BOTONES DE AGREGAR--------------------------------------
        self.pbConsultar.clicked.connect(self.botConsultar_clicked)

    def botConsultar_clicked(self):
            curp = str(self.lineEditCurpCon.text())
            consultar_registro = '''SELECT * from paciente WHERE curp_paciente=%s'''
            self.cursor.execute(consultar_registro,curp)
            row = self.cursor.fetchone()
            
            #self.lineEditCurpCon.setText(str(row[0]))
            self.lineEditNombreC.setText(str(row[0]))
            self.lineEditCurpC.setText(str(row[1]))
            self.lineEditEdadC.setText(str(row[2]))
            self.lineEditDirC.setText(str(row[3]))
            
if __name__ == '__main__':
    app = QApplication([])
    main = MyWindowClass()
    main.show()
    sys.exit(app.exec())