#Autor: Jimena Leon Garcia
#Fecha de creacion: 20/10/2022
#Ultima Fecha de modificacion: 016/11/2022
#Proyecto: Sistema de vacunación
#Modulo del sistema: Modulo Enfermera
#Version: 2.0


import sys
from PyQt5 import uic
import pandas as pd
from bd import ConexionBD

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class EnfermeraWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        
        
        #CARGAR EL ARCHIVO .UI====================================================================================================
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/enfermera_consultar.ui", self)
        #self.setWindowTitle("CONSULTAR VACUNA")  
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/enfermera_eliminar.ui", self) 
        #self.setWindowTitle("ELIMINAR VACUNA")  
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/enfermera_modificar.ui", self)
        #self.setWindowTitle("MODIFICAR VACUNA") 
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/enfermera_agregar.ui", self)
        
        
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Enfermera_menu.ui", self)
        self.setWindowTitle("MENU")  
        
    
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","vacunacion2")
        self.cursor = self.con.cursor()
        
        
        #ASIGNAR  EVENTOs A BOTONES=================================================================================================
        #BOTONES DE MENU
        self.pbAgregarEMenu.clicked.connect(self.botAgregarE_clicked) #ACCION IR A TUTOR (AGREGA) 
        self.pbEliminarEMenu.clicked.connect(self.botEliminarE_clicked)
        self.pbActualizarEMenu.clicked.connect(self.botModificarE_clicked) 
        self.pbConsultarEMenu.clicked.connect(self.botConsultarE_clicked)
        
        #BOTONES DE AGREGAR--------------------------------------
        self.pbAgregarEn.clicked.connect(self.AgregarE_clicked) #ACCION AGREGAR
        self.pblimpiarAE.clicked.connect(self.LimpiarAE_clicked) #ACCION LIMPIAR
        
        
        self.pbMenuE.clicked.connect(self.botVolverMenuE_clicked)#IR A MENU (VOLVER MENU)
        self.pbEliminarE.clicked.connect(self.botEliminarE_clicked)
        self.pbModificarE.clicked.connect(self.botModificarE_clicked)
        self.pbConsultarE.clicked.connect(self.botConsultarE_clicked)
        
        #BOTONES DE ELIMINAR-------------------------------------
        self.pbEliminarEn.clicked.connect(self.EliminarE_clicked) #ACCION ELIMINAR
        self.pbConsultaEn.clicked.connect(self.ConsultarE_clicked)#ACCION CONSULTAR
        self.pblimpiarEE.clicked.connect(self.LimpiarEE_clicked) #ACCION LIMPIAR
        
        
        self.pbMenuEE.clicked.connect(self.botVolverMenuE_clicked)#IR A MENU (VOLVER MENU)
        self.pbAgregarEE.clicked.connect(self.botAgregarE_clicked)
        self.pbModificarEE.clicked.connect(self.botModificarE_clicked)
        self.pbConsultarEE.clicked.connect(self.botConsultarE_clicked)
        
        #BOTONES DE CONSULTAR-------------------------------------
        self.pbConsultaCE.clicked.connect(self.ConsultarE_clicked)
        self.pblimpiarCE.clicked.connect(self.LimpiarEE_clicked) #ACCION LIMPIAR
        
        self.pbMenuEC.clicked.connect(self.botVolverMenuE_clicked)#IR A MENU (VOLVER MENU)
        self.pbAgregarEC.clicked.connect(self.botAgregarE_clicked)
        self.pbModificarEC.clicked.connect(self.botModificarE_clicked)
        self.pbEliminarEC.clicked.connect(self.botConsultarE_clicked)
        
        #BOTONES DE MODIFICAR-------------------------------------
        self.pbConsultarCo.clicked.connect(self.ConsultarEV2_clicked)
        self.pbModificarMo.clicked.connect(self.ModificarE_clicked)
        self.pblimpiarME.clicked.connect(self.LimpiarME_clicked) #ACCION LIMPIAR
        
        self.pbMenuEM.clicked.connect(self.botVolverMenuE_clicked)#IR A MENU (VOLVER MENU)
        self.pbAgregarEM.clicked.connect(self.botAgregarE_clicked)
        self.pbConsultarEM.clicked.connect(self.botConsultarE_clicked)
        self.pbEliminarEM.clicked.connect(self.botConsultarE_clicked)
        
    
    def LimpiarAE_clicked(self):
        #VACIAR lINEEDITS
        self.lineEditCedulaEA.setText('')
        self.lineEditNomEA.setText('')
        self.comboBoxTurnoEA.setCurrentIndex(-1)
        
    def LimpiarEE_clicked(self):
        #VACIAR lINEEDITS
        self.lineEditCedulaEn.setText('')
        self.lineEditNombreEn.setText('')
        self.lineEditTurnoEn.setText('')
        self.lineEditCedulaConEn.setText('')
        
    def LimpiarME_clicked(self):
        #VACIAR lINEEDITS
        self.comboBoxTurnoE.setCurrentIndex(-1)
        self.lineEditCedulaCE.setText('')
        self.lineEditCedulaE.setText('')
        self.lineEditNombreEn.setText('') 
        
    
    def AgregarE_clicked(self):
            #INSERTAR REGISTROS EN LA BD--
            try:
                #ASIGNAR VALORES DE ENTRADA 
                cedula = str(self.lineEditCedulaEA.text())
                cedula1 = len(cedula)                   
                consulta = '''SELECT * from enfermera WHERE cedula=%s'''  
                self.cursor.execute(consulta,cedula)
                con = self.cursor.fetchone()
                
                nomEnfermera = str(self.lineEditNomEA.text())
                Nom1 = len(nomEnfermera)
                turno = str(self.comboBoxTurnoEA.currentText())
                Nom2 = len(turno) 
                
                
                if cedula1 == 8 and con == None:
                    if Nom1 !=0 and Nom2 !=0 :
                        insertar_registros = '''insert into enfermera(cedula,nombre_enfermera, turno) 
                        values (%s,%s,%s)'''
                        datos = (cedula,nomEnfermera,turno)
                        self.cursor.execute(insertar_registros,datos)
                        self.con.commit()
                        '''#VACIAR lINEEDITS  #Tambien funciona
                        self.lineEditCedulaEA.setText('')
                        self.lineEditNomEA.setText('')
                        self.comboBoxTurnoEA.setCurrentIndex(-1)
                        
                        QMessageBox.information(self,"EXITOSO","GUARDADO CON EXITO",QMessageBox.Ok)'''
                    else: 
                        raise ValueError
                else:
                    raise ArithmeticError
                
            except ArithmeticError:
                    QMessageBox.information(self,"NO GUARDADO","VERIFICA LA CEDULA",QMessageBox.Ok)
            
            except  ValueError :
                    QMessageBox.information(self,"NO GUARDADO","POR FAVOR LLENA TODOS LOS CAMPOS",QMessageBox.Ok)
            
            else: # es la operacion que se va a realizar
                #VACIAR lINEEDITS
                self.lineEditCedulaEA.setText('')
                self.lineEditNomEA.setText('')
                self.comboBoxTurnoEA.setCurrentIndex(-1)
                
                QMessageBox.information(self,"EXITOSO","GUARDADO CON EXITO",QMessageBox.Ok)
            finally:
                print(" TERMINADO")
    #FUNCION ELIMINAR*********************************************************************************
    def EliminarE_clicked(self):
        try:
            cedula = str(self.lineEditCedulaConEn.text())
            consulta = '''SELECT * from enfermera WHERE cedula=%s'''  
            self.cursor.execute(consulta,cedula)
            con = self.cursor.fetchone() 
            if  con != None:
                respuesta = QMessageBox.information(self,"EXITOSO","¿ESTAS SEGURO DE QUERER ELIMINAR A ESTA ENFERMERA?",QMessageBox.Yes, QMessageBox.No)
                if respuesta == QMessageBox.Yes:
                    eliminar_registro = '''DELETE FROM enfermera WHERE cedula=%s'''
                    self.cursor.execute(eliminar_registro,cedula)
                    self.con.commit()
                    QMessageBox.information(self,"EXITOSO","ENFERMERA ELIMINADA",QMessageBox.Ok)
                else: 
                    #Ignore
                    raise ValueError
            else:
                raise ArithmeticError
        except ValueError :
            QMessageBox.information(self,"NO ELIMINADO","CANCELADO",QMessageBox.Ok)
        except ArithmeticError :
            QMessageBox.information(self,"ERROR","LA CEDULA NO EXISTE",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            #VACIAR lINEEDITS
            self.lineEditCedulaEn.setText('')
            self.lineEditNombreEn.setText('')
            self.lineEditTurnoEn.setText('')
            self.lineEditCedulaConEn.setText('')
        finally:
            print(" TERMINADO")
            
    #FUNCION CONSULTAR*********************************************************************************
    def ConsultarE_clicked(self):
        try:
            cedula = str(self.lineEditCedulaConEn.text())
            consulta = '''SELECT * from enfermera WHERE cedula=%s'''  
            self.cursor.execute(consulta,cedula)
            con = self.cursor.fetchone() 
            if  con != None:
                print(" ")
                #QMessageBox.information(self,"EXITOSO","PACIENTE ENCONTRADO",QMessageBox.Ok)   
            else:
                self.lineEditCedulaEn.setText('')
                self.lineEditNombreEn.setText('')
                self.lineEditTurnoEn.setText('')
                raise ValueError
        except ValueError :
            QMessageBox.information(self,"NO ENCONTRADO","LA ENFERMERA NO EXISTE, VERIFICA LA CEDULA",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            self.lineEditCedulaEn.setText((con[0]))
            self.lineEditNombreEn.setText((con[1]))
            self.lineEditTurnoEn.setText((con[2]))
        finally:
            print(" TERMINADO")
    #FUNCION MODIFICAR*********************************************************************************
    def ConsultarEV2_clicked(self):
        try:
            cedulaC = str(self.lineEditCedulaCE.text())
            consultar_registro = '''SELECT * from enfermera WHERE cedula=%s'''
            self.cursor.execute(consultar_registro,cedulaC)
            row = self.cursor.fetchone()
            if  row != None:
                print(" ")
                #QMessageBox.information(self,"EXITOSO","PACIENTE ENCONTRADO",QMessageBox.Ok)   
            else:
                self.lineEditCedulaE.setText('')
                self.lineEditNombreEn.setText('') 
                self.comboBoxTurnoE.setCurrentIndex(-1)
                
                
                raise ValueError
        except ValueError :
            QMessageBox.information(self,"NO ENCONTRADO","LA ENFERMERA NO EXISTE, VERIFICA EL CURP",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            self.lineEditCedulaE.setText((row[0]))
            self.lineEditNombreEn.setText((row[1]))
            self.comboBoxTurnoE.setCurrentText(str(row[2]))
            
        finally:
            print(" TERMINADO")
            
    #FUNCION MODIFICAR*********************************************************************************
    def ModificarE_clicked(self):
        try:
            #consultar
            cedulaC= str(self.lineEditCedulaCE.text())  #curp de consulta
            consultar_registro = '''SELECT * from enfermera WHERE cedula=%s'''
            self.cursor.execute(consultar_registro,cedulaC)
            row = self.cursor.fetchone()
            
            nombreEn = str(self.lineEditNombreEn.text())
            Nom1 = len(nombreEn)
            turno = str(self.comboBoxTurnoE.currentText())
            Nom2 = len(turno)
            
            
                    
            if  row != None:
                if Nom1 !=0 and Nom2 !=0 and row != None:
                    respuesta = QMessageBox.information(self,"EXITOSO","¿ESTAS SEGURO DE QUERER MODIFICAR ESTA ENFERMERA?",QMessageBox.Yes, QMessageBox.No)
                    if respuesta == QMessageBox.Yes:
                        actualizar_registro = '''UPDATE enfermera SET nombre_enfermera = %s , turno = %s WHERE cedula = %s''' #%(mod,okd)
                        self.cursor.execute(actualizar_registro,(nombreEn,turno,cedulaC))
                        self.con.commit()
                        QMessageBox.information(self,"EXITOSO","ENFERMERA ACTUALIZADA",QMessageBox.Ok)
                    else: 
                        #Ignore
                        raise ValueError
                else:
                    raise TypeError
            else:
                raise ArithmeticError
        
        except ValueError:
               QMessageBox.information(self,"NO ELIMINADO","CANCELADO",QMessageBox.Ok)
               
        except TypeError :
               QMessageBox.information(self,"NO ELIMINADO","POR FAVOR LLENA TODOS LOS CAMPOS",QMessageBox.Ok)
               
        except ArithmeticError :
               QMessageBox.information(self,"ERROR","NO EXISTE, VERIFICA LA CEDULA",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            #VACIAR lINEEDITS
            self.comboBoxTurnoE.setCurrentIndex(-1)
            self.lineEditCedulaCE.setText('')
            self.lineEditCedulaE.setText('')
            self.lineEditNombreEn.setText('') 
        finally:
            print(" TERMINADO")
                
    
    

                
    #>>>IR A MENU GENERAL
    def botVolverMenuE_clicked(self):    
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Enfermera_menu.ui", self)
        self.setWindowTitle("MENU")  
        
        EnfermeraWindowClass()#ACCION AGREGAR
        
        #BOTONES DE MENU
        self.pbAgregarEMenu.clicked.connect(self.botAgregarE_clicked) #ACCION IR A enfermera (AGREGA) 
        self.pbEliminarEMenu.clicked.connect(self.botEliminarE_clicked)
        self.pbActualizarEMenu.clicked.connect(self.botModificarE_clicked) 
        self.pbConsultarEMenu.clicked.connect(self.botConsultarE_clicked)
    
        self.pbRegresarEMenuMG.clicked.connect(self.volverG)
        
        
    def volverG(self):
        respuesta = QMessageBox.information(self,"SALIR","¿ESTAS SEGURO DE QUERER SALIR DE MENÚ ENFERMERA?",QMessageBox.Yes, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.close() 
        else:
            self.show() 
            
            
    
    #>>>IR A AGREGAR
    def botAgregarE_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/enfermera_agregar.ui", self)
        self.setWindowTitle("AGREGAR ENFERMERA")

        EnfermeraWindowClass()#ACCION AGREGAR 
        
        #BOTONES DE AGREGAR--------------------------------------
        self.pbAgregarEn.clicked.connect(self.AgregarE_clicked) #ACCION AGREGAR
        self.pblimpiarAE.clicked.connect(self.LimpiarAE_clicked) #ACCION LIMPIAR
        
        self.pbMenuE.clicked.connect(self.botVolverMenuE_clicked)#IR A MENU (VOLVER MENU)
        self.pbEliminarE.clicked.connect(self.botEliminarE_clicked)
        self.pbModificarE.clicked.connect(self.botModificarE_clicked)
        self.pbConsultarE.clicked.connect(self.botConsultarE_clicked)
        
    #>>>IR A ELIMINAR 
    def botEliminarE_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/enfermera_eliminar.ui", self)
        self.setWindowTitle("ELIMINAR ENFERMERA") 
        
        EnfermeraWindowClass()#ACCION AGREGAR 
        
        
        #BOTONES DE ELIMINAR-------------------------------------
        self.pbEliminarEn.clicked.connect(self.EliminarE_clicked) #ACCION ELIMINAR
        self.pbConsultaEn.clicked.connect(self.ConsultarE_clicked)
        self.pblimpiarEE.clicked.connect(self.LimpiarEE_clicked) #ACCION LIMPIAR
        
        
        self.pbMenuEE.clicked.connect(self.botVolverMenuE_clicked)#IR A MENU (VOLVER MENU)
        self.pbAgregarEE.clicked.connect(self.botAgregarE_clicked)
        self.pbModificarEE.clicked.connect(self.botModificarE_clicked)
        self.pbConsultarEE.clicked.connect(self.botConsultarE_clicked)
    
    #>>>IR A CONSULTAR
    def botConsultarE_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/enfermera_consultar.ui", self)
        self.setWindowTitle("CONSULTAR VENFERMERA")  
        
        EnfermeraWindowClass()#ACCION AGREGAR 
        
        self.pbConsultaCE.clicked.connect(self.ConsultarE_clicked)
        self.pblimpiarCE.clicked.connect(self.LimpiarEE_clicked) #ACCION LIMPIAR
        
        self.pbMenuEC.clicked.connect(self.botVolverMenuE_clicked)#IR A MENU (VOLVER MENU)
        self.pbAgregarEC.clicked.connect(self.botAgregarE_clicked)
        self.pbModificarEC.clicked.connect(self.botModificarE_clicked)
        self.pbEliminarEC.clicked.connect(self.botEliminarE_clicked)
    
    #>>>IR A MODIFICAR
    def botModificarE_clicked(self):    
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/enfermera_modificar.ui", self)
        self.setWindowTitle("MODIFICAR ENFERMERA")  
        
        self.pbConsultarCo.clicked.connect(self.ConsultarEV2_clicked)
        self.pbModificarMo.clicked.connect(self.ModificarE_clicked)
        self.pblimpiarME.clicked.connect(self.LimpiarME_clicked) #ACCION LIMPIAR
        
        self.pbMenuEM.clicked.connect(self.botVolverMenuE_clicked)#IR A MENU (VOLVER MENU)
        self.pbAgregarEM.clicked.connect(self.botAgregarE_clicked)
        self.pbConsultarEM.clicked.connect(self.botConsultarE_clicked)
        self.pbEliminarEM.clicked.connect(self.botConsultarE_clicked)
    
if __name__ == '__main__':
    app = QApplication([])
    main = EnfermeraWindowClass()
    main.show()
    sys.exit(app.exec())

