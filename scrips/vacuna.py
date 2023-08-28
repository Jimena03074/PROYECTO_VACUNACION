#Autor: Jimena Leon Garcia
#Matricula: 181803074
#Fecha de creacion: 20/10/2022
#Ultima Fecha de modificacion: 16/11/2022
#Profesora: Rebeca Rodríguez Huesca
#Proyecto: Sistema de vacunacion
#Modulo del sistema: Modulo de Vacuna
#Version: 2.0



from asyncio.windows_events import NULL
import sys
from PyQt5 import uic
import pandas as pd
from bd import ConexionBD
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
  

class VacunaWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
#CARGAR EL ARCHIVO .UI====================================================================================================
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/vacuna_consultar.ui", self)
        #self.setWindowTitle("CONSULTAR VACUNA")  
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/vacuna_eliminar.ui", self) 
        #self.setWindowTitle("ELIMINAR VACUNA")  
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/vacuna_modificar.ui", self)
        #self.setWindowTitle("MODIFICAR VACUNA") 
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/vacuna_agregar.ui", self)
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/vacuna_menu.ui", self)
        
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","vacunacion2")
        self.cursor = self.con.cursor()
        
#ASIGNAR  EVENTOs A BOTONES=================================================================================================
        #BOTONES DE MENU
        self.pbAgregarVMenu.clicked.connect(self.botAgregarV_clicked) #ACCION IR A TUTOR (AGREGA) 
        self.pbEliminarVMenu.clicked.connect(self.botEliminarV_clicked)
        self.pbActualizarVMenu.clicked.connect(self.botModificarV_clicked) 
        self.pbConsultarVMenu.clicked.connect(self.botConsultarV_clicked)
       
       
       
       
        #BOTONES DE AGREGAR--------------------------------------
        self.pbAgregarVa.clicked.connect(self.AgregarV_clicked) #ACCION AGREGAR
        self.pblimpiarAV.clicked.connect(self.LimpiarAV_clicked) #ACCION LIMPIAR
        
        self.pbMenuV.clicked.connect(self.botVolverMenuV_clicked)#IR A MENU (VOLVER MENU)
        self.pbEliminarV.clicked.connect(self.botEliminarV_clicked)
        self.pbModificarV.clicked.connect(self.botModificarV_clicked)
        self.pbConsultarV.clicked.connect(self.botConsultarV_clicked)
        
        #BOTONES DE ELIMINAR-------------------------------------
        self.pbEliminarVA.clicked.connect(self.EliminarV_clicked) #ACCION ELIMINAR
        self.pbConsultarL.clicked.connect(self.ConsultarV_clicked)
        self.pblimpiarEV.clicked.connect(self.LimpiarEV_clicked) #ACCION LIMPIAR
        
        
        self.pbMenuVE.clicked.connect(self.botVolverMenuV_clicked)#IR A MENU (VOLVER MENU)
        self.pbAgregarVE.clicked.connect(self.botAgregarV_clicked)
        self.pbModificarVE.clicked.connect(self.botModificarV_clicked)
        self.pbConsultarVE.clicked.connect(self.botConsultarV_clicked)
        
        #BOTONES DE CONSULTAR-------------------------------------
        self.pbConsultarCV.clicked.connect(self.ConsultarV_clicked)
        self.pblimpiarEV.clicked.connect(self.LimpiarEV_clicked) #ACCION LIMPIAR
        
        self.pbMenuVC.clicked.connect(self.botVolverMenuV_clicked)#IR A MENU (VOLVER MENU)
        self.pbAgregarVC.clicked.connect(self.botAgregarV_clicked)
        self.pbModificarVC.clicked.connect(self.botModificarV_clicked)
        self.pbEliminarVC.clicked.connect(self.botConsultarV_clicked)
        
        #BOTONES DE MODIFICAR-------------------------------------
        self.pbConsultarLC.clicked.connect(self.ConsultarV2_clicked)
        self.pbModificarVA.clicked.connect(self.ModificarV_clicked)
        self.pblimpiarAV.clicked.connect(self.LimpiarMV_clicked) #ACCION LIMPIAR
        
        
        self.pbMenuVM.clicked.connect(self.botVolverMenuV_clicked)#IR A MENU (VOLVER MENU)
        self.pbAgregarVM.clicked.connect(self.botAgregarV_clicked)
        self.pbConsultarVM.clicked.connect(self.botConsultarV_clicked)
        self.pbEliminarVM.clicked.connect(self.botConsultarV_clicked)
        
        
    def LimpiarAV_clicked(self):    
        #VACIAR lINEEDITS
        self.comboBoxVacuna.setCurrentIndex(-1)
        self.lineEditLote.setText('')
        self.comboBoxViaA.setCurrentIndex(-1)
        self.lineEditDispo.setText('')

    def LimpiarEV_clicked(self):    
        #VACIAR lINEEDITS
        self.lineEditLoteEC.setText('')
        self.lineEditNomVE.setText('')
        self.lineEditLoteE.setText('')
        self.lineEditViaAE.setText('')
        self.lineEditDispoE.setText('')
    
    def LimpiarMV_clicked(self): 
        #VACIAR lINEEDITS
        self.comboBoxVacunaM.setCurrentIndex(-1)
        self.comboBoxViaAM.setCurrentIndex(-1)
        self.lineEditDispoM.setText('')
        self.lineEditLoteMC.setText('') 

        
    def AgregarV_clicked(self):
            #INSERTAR REGISTROS EN LA BD--
            try:
                #ASIGNAR VALORES DE ENTRADA 
                lote = str(self.lineEditLote.text())
                lote1 = len(lote)
                
                consulta = '''SELECT * from vacuna WHERE lote_vacuna=%s'''  
                self.cursor.execute(consulta,lote)
                con = self.cursor.fetchone()          
                
                nomVacuna = str(self.comboBoxVacuna.currentText())
                via = str(self.comboBoxViaA.currentText())
                disponibilidad = int(self.lineEditDispo.text())
                

                if lote1 == 6 and con == None:
                    if disponibilidad >= 0:
                        insertar_registros = '''insert into vacuna(nombre_vacuna,lote_vacuna,via,disponibilidad) 
                        values (%s,%s,%s,%s)'''
                        datos = (nomVacuna,lote,via,disponibilidad)
                        self.cursor.execute(insertar_registros,datos)
                        self.con.commit()
                    else:
                        raise ArithmeticError
                else:
                    raise ValueError
                
            except ValueError :
                QMessageBox.information(self,"NO GUARDADO","VERIFICA LOS DATOS",QMessageBox.Ok)#falta arreglar
                   
            except ArithmeticError :
                QMessageBox.information(self,"NO GUARDADO","VERIFICA LA DISPONIBILIDAD",QMessageBox.Ok)
            
            else: # es la operacion que se va a realizar
                #VACIAR lINEEDITS
                self.comboBoxVacuna.setCurrentIndex(-1)
                self.lineEditLote.setText('')
                self.comboBoxViaA.setCurrentIndex(-1)
                self.lineEditDispo.setText('')
                QMessageBox.information(self,"EXITOSO","GUARDADO CON EXITO",QMessageBox.Ok)
            finally:
                print(" TERMINADO")
                
    #FUNCION ELIMINAR*********************************************************************************
    def EliminarV_clicked(self):
        try:
            lote = str(self.lineEditLoteEC.text())
            lote1 = len(lote)
            consulta = '''SELECT * from vacuna WHERE lote_vacuna=%s'''  
            self.cursor.execute(consulta,lote)
            con = self.cursor.fetchone() 
            
            if lote1 == 6 and con != None:
                respuesta = QMessageBox.information(self,"EXITOSO","¿ESTAS SEGURO DE QUERER ELIMINAR ESTA VACUNA?",QMessageBox.Yes, QMessageBox.No)
                if respuesta == QMessageBox.Yes:
                    eliminar_registro = '''DELETE FROM vacuna WHERE lote_vacuna=%s'''
                    self.cursor.execute(eliminar_registro,lote)
                    self.con.commit()
                    QMessageBox.information(self,"EXITOSO","VACUNA ELIMINADA",QMessageBox.Ok)
                else: 
                    #Ignore
                    raise ValueError
            else:
                raise ArithmeticError
        except ValueError :
            QMessageBox.information(self,"NO ELIMINADO","CANCELADO",QMessageBox.Ok)
        except ArithmeticError :
            QMessageBox.information(self,"ERROR","LA VACUNA NO EXISTE",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            #VACIAR lINEEDITS
            self.lineEditLoteEC.setText('')
            self.lineEditNomVE.setText('')
            self.lineEditLoteE.setText('')
            self.lineEditViaAE.setText('')
            self.lineEditDispoE.setText('')
        finally:
            print(" TERMINADO")
    #FUNCION CONSULTAR*********************************************************************************
    def ConsultarV_clicked(self):
        try:
            lote = str(self.lineEditLoteEC.text())
            lote1 = len(lote)
            consulta = '''SELECT * from vacuna WHERE lote_vacuna=%s'''  
            self.cursor.execute(consulta,lote)
            con = self.cursor.fetchone() 
            
            if  con != None and lote1==6:
                print(" ")
                #QMessageBox.information(self,"EXITOSO","LOTE ENCONTRADO",QMessageBox.Ok)   
            else:
                #self.lineEditLoteEC.setText('')
                self.lineEditNomVE.setText('')
                self.lineEditLoteE.setText('')
                self.lineEditViaAE.setText('')
                self.lineEditDispoE.setText('')
                raise ValueError
        except ValueError :
            QMessageBox.information(self,"NO ENCONTRADO","LA VACUNA NO EXISTE, VERIFICA EL LOTE",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            self.lineEditNomVE.setText((con[0]))
            self.lineEditLoteE.setText((con[1]))
            self.lineEditViaAE.setText((con[2]))
            self.lineEditDispoE.setText((con[3]))
        
        finally:
            print(" TERMINADO")
            
    #FUNCION MODIFICAR*********************************************************************************
    def ConsultarV2_clicked(self):
        try:
            loteC = str(self.lineEditLoteMC.text())
            lote1 = len(loteC)
            consultar_registro = '''SELECT * from vacuna WHERE lote_vacuna=%s'''
            self.cursor.execute(consultar_registro,loteC)
            row = self.cursor.fetchone()
            
            if lote1 == 6 and row != None:
                print(" ")
                #QMessageBox.information(self,"EXITOSO","ENFERMERA ENCONTRADO",QMessageBox.Ok)   
            else:
                self.lineEditVacunaM.setText('')
                self.comboBoxViaAM.setCurrentIndex(-1)
                self.lineEditDispoM.setText('')
                #self.lineEditLoteMC.setText('') 
                raise ValueError
        except ValueError :
            QMessageBox.information(self,"NO ENCONTRADO","LA VACUNA NO EXISTE, VERIFICA EL LOTE",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            self.lineEditVacunaM.setText(str(row[0]))
            self.comboBoxViaAM.setCurrentText(str(row[2]))
            self.lineEditDispoM.setText((row[3]))
        finally:
            print(" TERMINADO")
            
    #FUNCION MODIFICAR*********************************************************************************
    def ModificarV_clicked(self):
        try:
            loteC= str(self.lineEditLoteMC.text())  #curp de consulta
            lote1 = len(loteC)
            
            vacuna = str(self.lineEditVacunaM.text())
            via = str(self.comboBoxViaAM.currentText())
            disp = str(self.lineEditDispoM.text())
    
            #consultar
            loteC = str(self.lineEditLoteMC.text())
            consultar_registro = '''SELECT * from vacuna WHERE lote_vacuna=%s'''
            self.cursor.execute(consultar_registro,loteC)
            row = self.cursor.fetchone()
                  
            if  row != None and lote1==6:
                respuesta = QMessageBox.information(self,"EXITOSO","¿ESTAS SEGURO DE QUERER MODIFICAR ESTA VACUNA?",QMessageBox.Yes, QMessageBox.No)
                if respuesta == QMessageBox.Yes:
                    actualizar_registro = '''UPDATE vacuna SET nombre_vacuna = %s ,via = %s , disponibilidad = %s WHERE lote_vacuna = %s''' #%(mod,okd)
                    self.cursor.execute(actualizar_registro,(vacuna,via,disp,loteC))
                    self.con.commit()
                    QMessageBox.information(self,"EXITOSO","VACUNA ACTUALIZADA",QMessageBox.Ok)
                else: 
                    #Ignore
                    raise ValueError
            else:
                raise ArithmeticError
        except ValueError :
               QMessageBox.information(self,"NO ACTUALIZADO","CANCELADO",QMessageBox.Ok)
        except ArithmeticError :
               QMessageBox.information(self,"ERROR","NO EXISTE, VERIFICA EL LOTE",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            #VACIAR lINEEDITS
            self.lineEditVacunaM.setText('')
            self.comboBoxViaAM.setCurrentIndex(-1)
            self.lineEditDispoM.setText('')
            self.lineEditLoteMC.setText('') 
        finally:
            print(" TERMINADO")

#>>>IR A MENU GENERAL
    def botVolverMenuV_clicked(self):    
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Vacuna_menu.ui", self)
        self.setWindowTitle("MENU VACUNAS")  
        
        VacunaWindowClass()#ACCION AGREGAR
        
        #BOTONES DE MENU
        self.pbAgregarVMenu.clicked.connect(self.botAgregarV_clicked) #ACCION IR A TUTOR (AGREGA) 
        self.pbEliminarVMenu.clicked.connect(self.botEliminarV_clicked)
        self.pbActualizarVMenu.clicked.connect(self.botModificarV_clicked) 
        self.pbConsultarVMenu.clicked.connect(self.botConsultarV_clicked)
        
        self.pbRegresarVMenuMG.clicked.connect(self.volverGe)
        
    
    def volverGe(self):
        respuesta = QMessageBox.information(self,"SALIR","¿ESTAS SEGURO DE QUERER SALIR DE MENÚ VACUNA?",QMessageBox.Yes, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.close() 
        else:
            self.show()
        
#>>>IR A AGREGAR
    def botAgregarV_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/vacuna_agregar.ui", self)
        self.setWindowTitle("AGREGAR VACUNA")

        VacunaWindowClass()#ACCION AGREGAR 
         #BOTONES DE AGREGAR--------------------------------------
        self.pbAgregarVa.clicked.connect(self.AgregarV_clicked) #ACCION AGREGAR
        self.pblimpiarAV.clicked.connect(self.LimpiarAV_clicked) #ACCION LIMPIAR
        
        self.pbMenuV.clicked.connect(self.botVolverMenuV_clicked)#IR A MENU (VOLVER MENU)
        self.pbEliminarV.clicked.connect(self.botEliminarV_clicked)
        self.pbModificarV.clicked.connect(self.botModificarV_clicked)
        self.pbConsultarV.clicked.connect(self.botConsultarV_clicked)
        
        
#>>>IR A ELIMINAR 
    def botEliminarV_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/vacuna_eliminar.ui", self)
        self.setWindowTitle("ELIMINAR VACUNA") 
        
        VacunaWindowClass()#ACCION AGREGAR 
        
        #ACCION ELIMINAR
        self.pbConsultarL.clicked.connect(self.ConsultarV_clicked)
        self.pbEliminarVA.clicked.connect(self.EliminarV_clicked)
        self.pblimpiarEV.clicked.connect(self.LimpiarEV_clicked) #ACCION LIMPIAR 
        
        self.pbMenuVE.clicked.connect(self.botVolverMenuV_clicked)#IR A MENU (VOLVER MENU)
        self.pbAgregarVE.clicked.connect(self.botAgregarV_clicked)
        self.pbModificarVE.clicked.connect(self.botModificarV_clicked)
        self.pbConsultarVE.clicked.connect(self.botConsultarV_clicked)
        
        
    
#>>>IR A CONSULTAR
    def botConsultarV_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/vacuna_consultar.ui", self)
        self.setWindowTitle("CONSULTAR VACUNA")  
        
        VacunaWindowClass()#ACCION AGREGAR 
        self.pbConsultarCV.clicked.connect(self.ConsultarV_clicked)
        self.pblimpiarCV.clicked.connect(self.LimpiarEV_clicked) #ACCION LIMPIAR
        
        self.pbMenuVC.clicked.connect(self.botVolverMenuV_clicked)#IR A MENU (VOLVER MENU)
        self.pbAgregarVC.clicked.connect(self.botAgregarV_clicked)
        self.pbModificarVC.clicked.connect(self.botModificarV_clicked)
        self.pbEliminarVC.clicked.connect(self.botEliminarV_clicked)
        
        
#>>>IR A MODIFICAR
    def botModificarV_clicked(self):    
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/vacuna_modificar.ui", self)
        self.setWindowTitle("MODIFICAR VACUNA")  
        
        self.pbConsultarLC.clicked.connect(self.ConsultarV2_clicked)
        self.pbModificarVA.clicked.connect(self.ModificarV_clicked)
        self.pblimpiarAV.clicked.connect(self.LimpiarMV_clicked) #ACCION LIMPIAR
        
        self.pbMenuVM.clicked.connect(self.botVolverMenuV_clicked)#IR A MENU (VOLVER MENU)
        self.pbAgregarVM.clicked.connect(self.botAgregarV_clicked)
        self.pbConsultarVM.clicked.connect(self.botConsultarV_clicked)
        self.pbEliminarVM.clicked.connect(self.botEliminarV_clicked)
        
                    
if __name__ == '__main__':
    app = QApplication([])
    main = VacunaWindowClass()
    main.show()
    sys.exit(app.exec())


