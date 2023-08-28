#Autor: Jimena Leon Garcia
#Fecha de creacion: 20/10/2022
#Ultima Fecha de modificacion: 13/11/2022
#Proyecto: Sistema de vacunación
#Modulo del sistema: Modulo de Paciente
#Version: 2.0

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from bd import ConexionBD
from PyQt5.QtCore import QDate



class AplicarWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #CARGAR EL ARCHIVO .UI
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/comprobante.ui", self)
       
       
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","vacunacion2")
        self.cursor = self.con.cursor()
        
        
        self.pbRegresa.clicked.connect(self.Imprimir_clicked)
        
        
    #----------------CONSULTAR INFORMACION
    
   
    #declaracion de la funcion para el boton consultar    
    def Imprimir_clicked(self):
        
        self.cursor.execute("SELECT MAX(folio) FROM comprobante")
        self.con.commit()
        va = self.cursor.fetchone()
        print(va)
        
        #compro=self.cursor.execute("SELECT MAX(folio) FROM comprobante")
        self.cursor.execute("SELECT * from comprobante WHERE folio =%s",va)
        row = self.cursor.fetchone()
        print(row)
        
        self.lineEdit_Folio.setText(str(row[0]))
        self.lineEdit_CurpPaciente.setText(str(row[1]))
        self.lineEdit_CurpTutor.setText(str(row[2]))
        self.lineEdit_Nombre_p.setText(str(row[3]))
        self.lineEdit_edad.setText(str(row[4]))
        self.lineEdit_Vacuna.setText(str(row[5]))
        self.lineEdit_Dosis.setText(str(row[6]))
        self.lineEdit_FechaA.setText(str(row[7]))

    

if __name__ == '__main__':
    app = QApplication([])
    MyWindow = AplicarWindowClass()
    MyWindow.show()
    sys.exit(app.exec())