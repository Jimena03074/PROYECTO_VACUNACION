#Autor: Jimena Leon Garcia
#Fecha de creacion: 20/10/2022
#Ultima Fecha de modificacion: 13/11/2022
#Proyecto: Sistema de vacunacion
#Modulo del sistema: Modulo de Paciente
#Version: 2.0

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from bd import ConexionBD
from PyQt5.QtCore import QDate


class ComprobanteWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #CARGAR EL ARCHIVO .UI
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/comprobante.ui", self)
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Consultar_Comprobante.ui", self)
        self.setWindowTitle("APLICAR VACUNA")

       
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","vacunacion2")
        self.cursor = self.con.cursor()
        
             
        
        #---------------------------VENTANA COMPROBANTE-----------------------------------
        self.pbInfo_apli.clicked.connect(self.Comprobante_clicked)
        
        self.pbImprimir_apli.clicked.connect(self.Imprimir_clicked)
        self.pbLimpiar.clicked.connect(self.Limpiar_clicked)
        self.pbMENU_paci2.clicked.connect(self.volverGe)
        
        
        
        self.pbRegresa.clicked.connect(self.volver_clicked)
    
    
    def Limpiar_clicked(self):    
        #VACIAR lINEEDITS
        self.lineEdit_Folio_apli.setText('')
        self.lineEdit_Nombre_p.setText('')
        self.lineEdit_edadp.setText('')
        self.lineEdit_vacunaN.setText('')
        self.lineEdit_dosis_p.setText('')
        self.lineEdit_fechaA.setText('')
    
            
    def Comprobante_clicked(self):
        try:
            consulta = str(self.lineEdit_Folio_apli.text())
            self.cursor.execute("SELECT * from comprobante WHERE folio=%s ",consulta)
            row = self.cursor.fetchone()
            
            if  row != None:
                print(" ")
                #QMessageBox.information(self,"EXITOSO","LOTE ENCONTRADO",QMessageBox.Ok)   
            else:
                self.lineEdit_Folio_apli.setText('')
                self.lineEdit_Nombre_p.setText('')
                self.lineEdit_edadp.setText('')
                self.lineEdit_vacunaN.setText('')
                self.lineEdit_dosis_p.setText('')
                self.lineEdit_fechaA.setText('')
                raise ValueError
            
        except ValueError :
            QMessageBox.information(self,"NO ENCONTRADO","EL FOLIO NO EXISTE, VERIFICA EL FOLIO",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            self.lineEdit_Folio_apli.setText(str(row[0]))
            self.lineEdit_Nombre_p.setText(str(row[3]))
            self.lineEdit_edadp.setText(str(row[4]))
            self.lineEdit_vacunaN.setText(str(row[5]))
            self.lineEdit_dosis_p.setText(str(row[6]))
            self.lineEdit_fechaA.setText(str(row[7]))
        
        finally:
            print(" TERMINADO")
            
            
            
            
    def Imprimir_clicked(self):
        
        try:
            uic.loadUi("D:/PROYECTO_FINAL/Ventanas/comprobante.ui", self)
        
            va = str(self.lineEdit_Folio_apli.text())
            #compro=self.cursor.execute("SELECT MAX(folio) FROM comprobante")
            self.cursor.execute("SELECT * from comprobante WHERE folio =%s",va)
            row = self.cursor.fetchone()
            print(row)
            
            if  row != None and va!=0:
                print(" ")
                #QMessageBox.information(self,"EXITOSO","LOTE ENCONTRADO",QMessageBox.Ok)   
            else:
                self.lineEdit_Folio_apli.setText('')
                self.lineEdit_Nombre_p.setText('')
                self.lineEdit_edadp.setText('')
                self.lineEdit_vacunaN.setText('')
                self.lineEdit_dosis_p.setText('')
                self.lineEdit_fechaA.setText('')
                
                ComprobanteWindowClass()
                self.pbRegresa.clicked.connect(self.volver_clicked)
                
                raise ValueError
            
        except ValueError :
            QMessageBox.information(self,"NO ENCONTRADO","EL FOLIO NO EXISTE, VERIFICA EL FOLIO",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            self.lineEdit_Folio.setText(str(row[0]))
            self.lineEdit_CurpPaciente.setText(str(row[1]))
            self.lineEdit_CurpTutor.setText(str(row[2]))
            self.lineEdit_Nombre_p.setText(str(row[3]))
            self.lineEdit_edad.setText(str(row[4]))
            self.lineEdit_Vacuna.setText(str(row[5]))
            self.lineEdit_Dosis.setText(str(row[6]))
            self.lineEdit_FechaA.setText(str(row[7]))  
            
            ComprobanteWindowClass()
            self.pbRegresa.clicked.connect(self.volver_clicked)
        
        finally:
            print('')
        
             
    def BotVolverC_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/comprobante.ui", self)
        self.setWindowTitle("COMPROBANTE DE VACUNACION")  
        
        ComprobanteWindowClass()
        self.pbRegresa.clicked.connect(self.volver_clicked)
        
        
    def volver_clicked(self):
        #CARGAR EL ARCHIVO .UI
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Consultar_Comprobante.ui", self)
        self.setWindowTitle("COMPROBANTE")
        
        ComprobanteWindowClass()
        #---------------------------VENTANA COMPROBANTE-----------------------------------
        self.pbInfo_apli.clicked.connect(self.Comprobante_clicked)
        self.pbImprimir_apli.clicked.connect(self.Imprimir_clicked)
        self.pbLimpiar.clicked.connect(self.Limpiar_clicked)
        self.pbMENU_paci2.clicked.connect(self.volverGe)
        
    def volverGe(self):
        respuesta = QMessageBox.information(self,"SALIR","¿ESTAS SEGURO DE QUERER SALIR DE COMPROBANTE?",QMessageBox.Yes, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.close() 
        else:
            self.show()
        

if __name__ == '__main__':
    app = QApplication([])
    MyWindow = ComprobanteWindowClass()
    MyWindow.show()
    sys.exit(app.exec())