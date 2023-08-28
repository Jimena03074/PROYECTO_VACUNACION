#Autor: Jimena Leon Garcia
#Fecha de creacion: 20/10/2022
#Ultima Fecha de modificacion: 09/11/2022
#Proyecto: Sistema de vacunación
#Modulo del sistema: Modulo Enfermera
#Version: 2.0



from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PyQt5 import QtWidgets, QtCore, QtGui
from asyncio.windows_events import NULL


import sys
from PyQt5 import uic
import pandas as pd
from bd import ConexionBD

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class ReporteWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        #CARGAR EL ARCHIVO .UI====================================================================================================
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/reporte_vacunas.ui", self)
        #self.setWindowTitle("REPORTE")  
        
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","vacunacion2")
        self.cursor = self.con.cursor()
    
        #BOTONES DE REPORTE VACUNAS
        self.pbConsultarReporte.clicked.connect(self.consultarCURP)
        self.pblimpiarREPORTE.clicked.connect(self.Limpiar)
        
        self.pbMenuGr.clicked.connect(self.volverGe)
        
        tablerow = 0
        
        
        
        consulta = '''SELECT * from reporte'''  
        self.cursor.execute(consulta)
        con = self.cursor.fetchone()
        
        

        if con != None:
            
            """print('si entra')
                
            curp1 = con[0]
            CURP1 = str(curp1)

            nomV1 = con[1]
            NOMV1 = str(nomV1)

            dosis1 = con[2]
            DOSIS1 = str(dosis1)"""
            
            
            self.tablePaciente_2.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(con[0])))
            self.tablePaciente_2.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(con[1]))) 
            self.tablePaciente_2.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(con[2])))
            tablerow +=1
        
        
        
    def consultarCURP(self):
        
        tablerow = 0
        
        curp = str(self.lineEditCurpReporte.text())
        consulta = '''SELECT * from reporte WHERE CurpPaciente=%s'''  
        self.cursor.execute(consulta,curp)
        con = self.cursor.fetchone() 
        
        
        
        if con != None:
            print('si entra')
                
            curp = con[0]
            CURP = str(curp)

            nomV = con[1]
            NOMV = str(nomV)

            dosis = con[2]
            DOSIS = str(dosis)
            
            
            self.tablePaciente.setItem(tablerow,0,QtWidgets.QTableWidgetItem(CURP))
            self.tablePaciente.setItem(tablerow,1,QtWidgets.QTableWidgetItem(NOMV)) 
            self.tablePaciente.setItem(tablerow,2,QtWidgets.QTableWidgetItem(DOSIS))
            tablerow +=1
        else:
            QMessageBox.information(self,"NO ENCONTRADO","EL CURP NO EXISTE, VERIFICA LA CEDULA",QMessageBox.Ok)
        
            
    def Limpiar(self):
        #VACIAR lINEEDITS
        self.lineEditCurpReporte.setText('')
        
    
    def volverGe(self):
        respuesta = QMessageBox.information(self,"SALIR","¿ESTAS SEGURO DE QUERER SALIR DE MENÚ",QMessageBox.Yes, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.close() 
        else:
            self.show()
    
    
if __name__ == '__main__':
    app = QApplication([])
    main = ReporteWindowClass()
    main.show()
    sys.exit(app.exec())

