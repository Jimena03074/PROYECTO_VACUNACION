from asyncio.windows_events import NULL
import sys
from PyQt5 import uic
import pandas as pd
from programa.bd import ConexionBD
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
  

class TutorMWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

#CARGAR EL ARCHIVO .UI==================================================================================================
        uic.loadUi("D:/POO/PROYECTO_FINAL/Ventanas/tutor_consultar.ui", self)
        #self.setWindowTitle("CONSULTAR PACIENTE")  
        
        uic.loadUi("D:/POO/PROYECTO_FINAL/Ventanas/tutor_modificar.ui", self)
       
         
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","vacunacion")
        self.cursor = self.con.cursor()
 
#ASIGNAR  EVENTOs A BOTONES==============================================================================================
        #BOTONES DE MENU
       
       #BOTONES DE CONSULTAR--------------------------------------
        
        self.pbConsultaCT.clicked.connect(self.ConsultarT_clicked) #ACCION CONSULTAR

        #MODIFICAR        
        self.pbConsultaMT.clicked.connect(self.ConsultarT2_clicked) 
        self.pbModificarMT.clicked.connect(self.ModificarT_clicked) 

#FUNCION CONSULTAR*********************************************************************************
    def ConsultarT2_clicked(self):
        try:
            curp = str(self.lineEditCurpConTE.text())
            consultar_registro = '''SELECT * from tutor WHERE curp_tutor=%s'''
            self.cursor.execute(consultar_registro,curp)
            row = self.cursor.fetchone()
            if  row != None:
                print(" ")
                #QMessageBox.information(self,"EXITOSO","PACIENTE ENCONTRADO",QMessageBox.Ok)   
            else:
                self.lineEditNomTE.setText('')
                self.lineEditCurpTE.setText('')
                self.lineEditEdadTE.setText('')
                self.lineEditTelefonoTE.setText('')
                self.lineEditDireccionTE.setText('') 
                raise ValueError
        except ValueError :
            QMessageBox.information(self,"NO Encontrado","EL PACIENTE NO EXISTE, VERIFICA EL CURP",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            self.lineEditNomTE.setText((row[0]))
            self.lineEditCurpTE.setText((row[1]))
            self.lineEditTelefonoTE.setText((row[2]))
            self.lineEditEdadTE.setText((row[3]))
            self.lineEditDireccionTE.setText((row[4]))
        finally:
            print(" TERMINADO")
            
    #FUNCION MODIFICAR*********************************************************************************
    def ModificarT_clicked(self):
        try:
            curp1 = str(self.lineEditCurpConTE.text())  #curp de consulta
            nom = str(self.lineEditNomTE.text())
            #curp = str(self.lineEditCurpTE.text())
            edad = str(self.lineEditEdadTE.text())
            telefono = str(self.lineEditTelefonoTE.text())
            direc = str(self.lineEditDireccionTE.text())
    
            #consultar
            curp = str(self.lineEditCurpConTE.text())
            consultar_registro = '''SELECT * from tutor WHERE curp_tutor=%s'''
            self.cursor.execute(consultar_registro,curp)
            row = self.cursor.fetchone()
                  
            if  row != None:
                respuesta = QMessageBox.information(self,"EXITOSO","¿ESTAS SEGURO DE QUERER MODIFICAR ESTE TUTOR?",QMessageBox.Yes, QMessageBox.No)
                if respuesta == QMessageBox.Yes:
                    actualizar_registro = '''UPDATE tutor SET nombre_tutor = %s,telefono_tutor = %s ,edad = %s , direccion_tutor = %s WHERE curp_tutor = %s''' #%(mod,okd)
                    self.cursor.execute(actualizar_registro,(nom,telefono,edad,direc,curp1))
                    self.con.commit()
                    QMessageBox.information(self,"EXITOSO","TUTOR ACTUALIZADO",QMessageBox.Ok)
                else: 
                    #Ignore
                    raise ValueError
            else:
                raise ArithmeticError
        except ValueError :
               QMessageBox.information(self,"NO ELIMINADO","CANCELADO",QMessageBox.Ok)
        except ArithmeticError :
               QMessageBox.information(self,"ERROR","EL TUTOR NO EXISTE, VERIFICA EL CURP",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            #VACIAR lINEEDITS
            self.lineEditNomTE.setText('')
            self.lineEditCurpConTE.setText('')
            self.lineEditEdadTE.setText('')
            self.lineEditTelefonoTE.setText('')
            self.lineEditDireccionTE.setText('') 
        finally:
            print(" TERMINADO")
if __name__ == '__main__':
    app = QApplication([])
    main = TutorMWindowClass()
    main.show()
    sys.exit(app.exec())