from asyncio.windows_events import NULL
import sys
from PyQt5 import uic
import pandas as pd
from programa.bd import ConexionBD
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
  

class VacunaMWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

#CARGAR EL ARCHIVO .UI==================================================================================================
        
        uic.loadUi("D:/POO/PROYECTO_FINAL/Ventanas/vacuna_modificar.ui", self)
       
         
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","vacunacion")
        self.cursor = self.con.cursor()
 
#ASIGNAR  EVENTOs A BOTONES==============================================================================================
        #BOTONES DE MENU
       
       
        #MODIFICAR        
         #BOTONES DE MODIFICAR-------------------------------------
        self.pbConsultarLC.clicked.connect(self.ConsultarV2_clicked)
        self.pbModificarVA.clicked.connect(self.ModificarV_clicked)
        
        """ self.pbMenuVM.clicked.connect(self.botVolverMenuV_clicked)#IR A MENU (VOLVER MENU)
        self.pbAgregarVM.clicked.connect(self.botAgregarV_clicked)
        self.pbConsultarVM.clicked.connect(self.botModificarV_clicked)
        self.pbEliminarVM.clicked.connect(self.botConsultarV_clicked)"""
#FUNCION CONSULTAR*********************************************************************************
    def ConsultarV2_clicked(self):
        try:
            loteC = str(self.lineEditLoteMC.text())
            consultar_registro = '''SELECT * from vacuna WHERE lote_vacuna=%s'''
            self.cursor.execute(consultar_registro,loteC)
            row = self.cursor.fetchone()
            if  row != None:
                print(" ")
                #QMessageBox.information(self,"EXITOSO","PACIENTE ENCONTRADO",QMessageBox.Ok)   
            else:
                self.comboBoxVacunaM.setCurrentIndex(-1)
                self.lineEditDosisM.setText('')
                self.comboBoxViaAM.setCurrentIndex(-1)
                self.lineEditDispoM.setText('')
                self.lineEditLoteMC.setText('') 
                raise ValueError
        except ValueError :
            QMessageBox.information(self,"NO Encontrado","EL PACIENTE NO EXISTE, VERIFICA EL CURP",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            self.comboBoxVacunaM.setCurrentText(str(row[0]))
            self.lineEditDosisM.setText((row[2]))
            self.comboBoxViaAM.setCurrentText(str(row[3]))
            self.lineEditDispoM.setText((row[4]))
        finally:
            print(" TERMINADO")
            
    #FUNCION MODIFICAR*********************************************************************************
    def ModificarV_clicked(self):
        try:
            loteC= str(self.lineEditLoteMC.text())  #curp de consulta
            vacuna = str(self.comboBoxVacunaM.currentText())
            dosis = str(self.lineEditDosisM.text())
            via = str(self.comboBoxViaAM.currentText())
            disp = str(self.lineEditDispoM.text())
    
            #consultar
            loteC = str(self.lineEditLoteMC.text())
            consultar_registro = '''SELECT * from vacuna WHERE lote_vacuna=%s'''
            self.cursor.execute(consultar_registro,loteC)
            row = self.cursor.fetchone()
                  
            if  row != None:
                respuesta = QMessageBox.information(self,"EXITOSO","¿ESTAS SEGURO DE QUERER MODIFICAR ESTA VACUNA?",QMessageBox.Yes, QMessageBox.No)
                if respuesta == QMessageBox.Yes:
                    actualizar_registro = '''UPDATE vacuna SET nombre_vacuna = %s,dosis = %s ,via = %s , disponibilidad = %s WHERE lote_vacuna = %s''' #%(mod,okd)
                    self.cursor.execute(actualizar_registro,(vacuna,dosis,via,disp,loteC))
                    self.con.commit()
                    QMessageBox.information(self,"EXITOSO","VACUNA ACTUALIZADA",QMessageBox.Ok)
                else: 
                    #Ignore
                    raise ValueError
            else:
                raise ArithmeticError
        except ValueError :
               QMessageBox.information(self,"NO ELIMINADO","CANCELADO",QMessageBox.Ok)
        except ArithmeticError :
               QMessageBox.information(self,"ERROR","NO EXISTE, VERIFICA EL LOTE",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            #VACIAR lINEEDITS
            self.comboBoxVacunaM.setCurrentIndex(-1)
            self.lineEditDosisM.setText('')
            self.comboBoxViaAM.setCurrentIndex(-1)
            self.lineEditDispoM.setText('')
            self.lineEditLoteMC.setText('') 
        finally:
            print(" TERMINADO")
if __name__ == '__main__':
    app = QApplication([])
    main = VacunaMWindowClass()
    main.show()
    sys.exit(app.exec())