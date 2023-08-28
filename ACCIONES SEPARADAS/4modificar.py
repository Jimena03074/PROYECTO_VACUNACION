from asyncio.windows_events import NULL
import sys
from PyQt5 import uic
import pandas as pd
from programa.bd import ConexionBD
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class ModificarWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        uic.loadUi("D:/POO/PROYECTO_FINAL/Ventanas/paciente_modificar.ui", self) 
        self.setWindowTitle("MODIFICAR PACIENTE")  
        
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","vacunacion")
        self.cursor = self.con.cursor()
 
        #ASIGNA  EVENTOs A BOTONES********
        #BOTONES DE MODIFICAR-------------------------------------
        self.pbModificarPM.clicked.connect(self.Modificar_clicked)
        self.pbConsultarPM.clicked.connect(self.Consultar2_clicked)
        

    def Modificar_clicked(self):
        try:
            nombre =str(self.lineEditNombreC.text())
            edad = str(self.comboBoxEdadC.currentText())
            dir =str(self.lineEditDirC.text())
            
            curp = str(self.lineEditCurpCon.text())
            consultar_registro = '''SELECT * from paciente WHERE curp_paciente=%s'''
            self.cursor.execute(consultar_registro,curp)
            row = self.cursor.fetchone()
            
            if  row != None:
                respuesta = QMessageBox.information(self,"EXITOSO","¿ESTAS SEGURO DE QUERER MODIFICAR ESTE PACIENTE?",QMessageBox.Yes, QMessageBox.No)
                if respuesta == QMessageBox.Yes:
                    actualizar_registro = '''UPDATE paciente SET nombre_paciente = %s, edad = %s , direccion = %s WHERE curp_paciente = %s''' #%(mod,okd)
                    self.cursor.execute(actualizar_registro,(nombre,edad,dir,curp))
                    self.con.commit()
                    QMessageBox.information(self,"EXITOSOSO","DATOS ACTUALIZADOS",QMessageBox.Ok)
                else: 
                    #Ignore
                    raise ValueError
            else:
                raise ArithmeticError
        except ValueError :
               QMessageBox.information(self,"NO Modificado","CANCELADO",QMessageBox.Ok)
        except ArithmeticError :
               QMessageBox.information(self,"ERROR","EL PACIENTE NO EXISTE, VERIFICA EL CURP",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            #VACIAR lINEEDITS
            self.lineEditCurpCon.setText('')
            self.lineEditNombreC.setText('')
            self.lineEditCurpC.setText('')
            self.comboBoxEdadC.setCurrentIndex(-1)
            self.lineEditDirC.setText('')  
        finally:
            print(" TERMINADO")
            
    def Consultar2_clicked(self):
        try:
            curp = str(self.lineEditCurpCon.text())
            consultar_registro = '''SELECT * from paciente WHERE curp_paciente=%s'''
            self.cursor.execute(consultar_registro,curp)
            row = self.cursor.fetchone()
            
            if  row != None:
                print(" ")
                #QMessageBox.information(self,"EXITOSO","PACIENTE ENCONTRADO",QMessageBox.Ok)   
            else:
                self.lineEditCurpCon.setText('')
                self.lineEditNombreC.setText('')
                self.lineEditCurpC.setText('')
                self.comboBoxEdadC.setCurrentIndex(-1)
                self.lineEditDirC.setText('')  
                raise ValueError
        except ValueError :
            QMessageBox.information(self,"NO Encontrado","EL PACIENTE NO EXISTE, VERIFICA EL CURP",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            self.lineEditNombreC.setText(str(row[0]))
            self.lineEditCurpC.setText(str(row[1]))
            self.comboBoxEdadC.setCurrentText(str(row[2]))
            self.lineEditDirC.setText(str(row[3]))
        finally:
            print(" TERMINADO")

if __name__ == '__main__':
    app = QApplication([])
    main = ModificarWindowClass()
    main.show()
    sys.exit(app.exec())