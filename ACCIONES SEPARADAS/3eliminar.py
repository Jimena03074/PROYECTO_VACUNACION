
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

        uic.loadUi("D:/POO/PROYECTO_FINAL/Ventanas/paciente_eliminar.ui", self) 
        self.setWindowTitle("ELIMINAR  PACIENTE")  
        
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","vacunacion")
        self.cursor = self.con.cursor()
 
        #ASIGNA  EVENTOs A BOTONES
        
        #BOTONES DE ELIMINAR-------------------------------------
        self.pbEliminaEl.clicked.connect(self.botEliminar_clicked)
        self.pbConsultaEl.clicked.connect(self.botConsultar_clicked)
        
        
    #ELIMINAR REGISTROS EN LA BD--
    def botEliminar_clicked(self):
        curp = str(self.lineEditCurpEC.text())
        consultar_registro = '''SELECT * from paciente WHERE curp_paciente=%s'''
        self.cursor.execute(consultar_registro,curp)
        row = self.cursor.fetchone()
        if  row != None:
            eliminar_registro = '''DELETE FROM paciente WHERE curp_paciente=%s'''
            self.cursor.execute(eliminar_registro,curp)
            self.con.commit()
            
            self.lineEditCurpEC.setText('')
            self.lineEditNombreE.setText('')
            self.lineEditCurpE.setText('')
            self.lineEditEdadE.setText('')
            self.lineEditDirE.setText('')
            QMessageBox.information(self,"EXITOSO","EL PACIENTE SE ELIMINO CORRECTAMENTE",QMessageBox.Ok)
        else:
            self.lineEditCurpEC.setText('')
            QMessageBox.information(self,"ERROR","EL PACIENTE NO EXISTE",QMessageBox.ok)
            
            
    def botConsultar_clicked(self):
        curp = str(self.lineEditCurpEC.text())
        consultar_registro = '''SELECT * from paciente WHERE curp_paciente=%s'''
        self.cursor.execute(consultar_registro,curp)
        row = self.cursor.fetchone()
        
        if  row != None:
            self.lineEditNombreE.setText(str(row[0]))
            self.lineEditCurpE.setText(str(row[1]))
            self.lineEditEdadE.setText(str(row[2]))
            self.lineEditDirE.setText(str(row[3]))
        else:
            self.lineEditCurpEC.setText('')
            self.lineEditNombreE.setText('')
            self.lineEditCurpE.setText('')
            self.lineEditEdadE.setText('')
            self.lineEditDirE.setText('')
            QMessageBox.information(self,"ERROR","EL PACIENTE NO EXISTE",QMessageBox.Ok)
        
        
if __name__ == '__main__':
    app = QApplication([])
    main = MyWindowClass()
    main.show()
    sys.exit(app.exec())