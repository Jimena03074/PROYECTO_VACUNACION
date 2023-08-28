
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

        #CARGAR EL ARCHIVO .UI
        uic.loadUi("D:/POO/PROYECTO_FINAL/Ventanas/paciente_agregar.ui", self)
        self.setWindowTitle("AGREGAR PACIENTE")  
        
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","vacunacion")
        self.cursor = self.con.cursor()
 
        #ASIGNA  EVENTOS A BOTONES
        #BOTONES DE AGREGAR--------------------------------------
        self.pbAgregar.clicked.connect(self.botAgregar_clicked)

    #INSERTAR REGISTROS EN LA BD--
    def botAgregar_clicked(self):
        try:
            #ASIGNAR VALORES DE ENTRADA 
            curp = str(self.lineEditCurp.text())
            curp1 = len(curp)
            consulta = '''SELECT * from paciente WHERE curp_paciente=%s'''  
            self.cursor.execute(consulta,curp)
            con = self.cursor.fetchone()          

            if curp1 == 18 and con == None:
                    nom = str(self.lineEditNomP.text())
                    edad = str(self.comboBoxEdad.currentText())
                    direc = str(self.lineEditDir.text())
                    insertar_registros = '''insert into paciente (nombre_paciente,curp_paciente,edad,direccion) 
                    values (%s,%s,%s,%s)'''
                    datos = (nom,curp,edad,direc)
                    self.cursor.execute(insertar_registros,datos)
                    self.con.commit()
            else:
                raise ArithmeticError
        except ArithmeticError :
            QMessageBox.information(self,"NO GUARDADO","VERIFICA EL CURP",QMessageBox.Ok)
            
        else: # es la operacion que se va a realizar
            #VACIAR lINEEDITS
            self.lineEditCurp.setText('')
            self.lineEditNomP.setText('')
            self.comboBoxEdad.setCurrentIndex(-1)
            self.lineEditDir.setText('')
            QMessageBox.information(self,"EXITOSO","Guardado con éxito",QMessageBox.Ok)
        finally:
            print(" TERMINADO")
        
if __name__ == '__main__':
    app = QApplication([])
    main = MyWindowClass()
    main.show()
    sys.exit(app.exec())
