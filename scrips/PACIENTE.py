#Autor: Luis Alberto Sanchez Salazar
#Matricula: 181803050
#Fecha de creacion: 20/10/2022
#Ultima Fecha de modificacion: 13/11/2022
#Profesora: Rebeca Rodríguez Huesca
#Proyecto: Sistema de vacunacion
#Modulo del sistema: Modulo de Paciente
#Version: 2.0

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from bd import ConexionBD

class PacienteWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Paciente.ui", self)
        #CARGAR EL ARCHIVO .UI
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Agregar_Paciente.ui", self)
        #self.setWindowTitle("Agregar Paciente")
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Actualizar_Paciente.ui", self)
        #self.setWindowTitle("Modificar Paciente")
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Eliminar_Paciente.ui", self)
        #self.setWindowTitle("Eliminar Paciente")
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Consultar_Paciente.ui", self)
        #self.setWindowTitle("Consultar Paciente")
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Paciente.ui", self)
       
       
        
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","vacunacion2")
        self.cursor = self.con.cursor()
        
        #ASIGNAR  EVENTOs A BOTONES=================================================================================================
       
        #BOTONES DE MENU
        self.pbAgregar_paci.clicked.connect(self.BotonAgregar_paci_clicked)
        self.pbModificar_paci.clicked.connect(self.BotonModificar_paci_clicked)
        self.pbConsultar_paci.clicked.connect(self.BotonConsultar_paci_clicked)
        self.pbEliminar_paci.clicked.connect(self.BotonEliminar_paci_clicked)
        self.pbMenuP.clicked.connect(self.volverG)
        
        
        #BOTONES DE AGREGAR--------------------------------------
        self.pbGuardar_paci.clicked.connect(self.AgregarPaciente_clicked)
        
        
        self.pbCancelar_paci.clicked.connect(self.BotonCancelar_paci_clicked)
        self.pbMENU_paci.clicked.connect(self.BotonVolverMenu_paci_clicked)
        self.pbEliminar_paci.clicked.connect(self.BotonEliminar_paci_clicked)
        self.pbModificar_paci.clicked.connect(self.BotonModificar_paci_clicked)
        self.pbConsultar_paci.clicked.connect(self.BotonConsultar_paci_clicked)
        
        #BOTONES DE ELIMINAR-------------------------------------
        self.pbDelete_paci.clicked.connect(self.EliminarPaciente_clicked)
        self.pbInfo_paci.clicked.connect(self.Consultar2_clicked)
        
        self.pbConsultar_paci.clicked.connect(self.BotonConsultar_paci_clicked)
        self.pbMENU_paci.clicked.connect(self.BotonVolverMenu_paci_clicked)
        self.pbAgregar_paci.clicked.connect(self.BotonAgregar_paci_clicked)
        self.pbModificar_paci.clicked.connect(self.BotonModificar_paci_clicked)
        self.pbCancelar_paci.clicked.connect(self.BotonCancelar_paci1_clicked)
        
        
        #BOTONES DE CONSULTAR-------------------------------------
        self.pbInfo_paci.clicked.connect(self.Consultar2_clicked)
        
        self.pbAgregar_paci.clicked.connect(self.BotonAgregar_paci_clicked)
        self.pbMENU_paci.clicked.connect(self.BotonVolverMenu_paci_clicked)
        self.pbEliminar_paci.clicked.connect(self.BotonEliminar_paci_clicked)
        self.pbModificar_paci.clicked.connect(self.BotonModificar_paci_clicked)
        self.pbCancelar_paci.clicked.connect(self.BotonCancelar_paci1_clicked)
        
        
        #BOTONES DE ACTUALIZAR-------------------------------------
        self.pbGuardar_paci.clicked.connect(self.Modificar_clicked)
        self.pbInfo_paci.clicked.connect(self.Consultar_clicked)
        
        
        self.pbConsultar_paci.clicked.connect(self.BotonConsultar_paci_clicked)
        self.pbAgregar_paci.clicked.connect(self.BotonAgregar_paci_clicked)
        self.pbMENU_paci.clicked.connect(self.BotonVolverMenu_paci_clicked)
        self.pbEliminar_paci.clicked.connect(self.BotonEliminar_paci_clicked)
        self.pbCancelar_paci.clicked.connect(self.BotonCancelar_paci_clicked)
    
    
    
    
    #Boton para limpieza del formulario
    def BotonCancelar_paci1_clicked(self):
        self.lineEdit_CurpT.setText('')
        self.lineEdit_CURP_p.setText('')
        self.lineEdit_Nombre_p.setText('')
        self.lineEdit_Edad_p.setText('')
        self.lineEdit_Direccion_p.setText('')
        self.con.commit()
    
    #Boton para limpieza del formulario
    def BotonCancelar_paci_clicked(self):
        self.lineEdit_CurpT.setText('')
        self.lineEdit_CURP_p.setText('')
        self.lineEdit_Nombre_p.setText('')
        self.comboBoxEdad_p.setCurrentIndex(-1)
        self.lineEdit_Direccion_p.setText('')
        self.con.commit()
    
    
    #--------AGREGAR PACIENTE-------------------------------------------------------------------
    #declaracion de la funcion para el boton guardar        
    def AgregarPaciente_clicked(self):
        try:
            
            #ASIGNAR VALORES DE ENTRADA PARA CONSULTAR
            curp_p = str(self.lineEdit_CURP_p.text())
            curp1 = len(curp_p)
            
            consulta = '''SELECT curp_p from paciente WHERE curp_p=%s'''  
            self.cursor.execute(consulta,curp_p)
            row = self.cursor.fetchone()
            
            
            if curp1 == 18 and row == None: #Corrobora que no exista el datos a ingresar
                
                #se declaran variables para las entradas de datos
                curp_t = str(self.lineEdit_CURP_T.text())
                curp2 = len(curp_t)
                
                consulta1 = '''SELECT curp_t from tutor WHERE curp_t=%s'''  
                self.cursor.execute(consulta1,curp_t)
                row2 = self.cursor.fetchone()
                
                if curp2 == 18 and row2 != None: #Corrobora que no exista el datos a ingresar
                    nombre_p=str(self.lineEdit_Nombre_p.text())
                    edad_p = str(self.comboBoxEdad_p.currentText())
                    direc_p=str(self.lineEdit_Direccion_p.text())
                    inserta_registros = '''insert into paciente(curp_p, curp_t, nombre_p, edad_p, direccion_p)
                    values(%s,%s,%s,%s,%s)'''
                    datos=(curp_p, curp_t, nombre_p, edad_p, direc_p)
                    self.cursor.execute(inserta_registros,datos)
                    self.con.commit()
                else:
                    raise ArithmeticError
            else:
                raise ValueError
            
        except ValueError :
            QMessageBox.information(self,"NO GUARDADO","VERIFICA EL CURP DE PACIENTE",QMessageBox.Ok)#falta arreglar
                
        except ArithmeticError :
            QMessageBox.information(self,"NO GUARDADO","VERIFICA EL CURP DE TUTOR",QMessageBox.Ok)
        
        else:
            #Limpia por completo el formulario
            self.lineEdit_CURP_T.setText('')
            self.lineEdit_CURP_p.setText('')
            self.lineEdit_Nombre_p.setText('')
            self.comboBoxEdad_p.setCurrentIndex(-1)
            self.lineEdit_Direccion_p.setText('')
            QMessageBox.information(self, "EXITOSO","GUARDADO CON EXITO", QMessageBox.Ok)
        finally:
            print(" TERMINADO")
        
    #----------------ELIMINAR PACIENTE-----------------------------------------------------------
    #funcion para eliminar datos    
    def EliminarPaciente_clicked(self):
        try:
            ELI=str(self.lineEdit_CURP_p.text())
            consulta  ='''SELECT * from paciente WHERE curp_p=%s''' #% ELI
            self.cursor.execute(consulta,ELI)
            row = self.cursor.fetchone()
            
            if row != None:
                reply = QMessageBox.information(self,"EXITOSO","¿ESTAS SEGURO DE QUERER ELIMINAR EL PACIENTE?",
                        QMessageBox.Yes, QMessageBox.No)
                
                if reply == QMessageBox.Yes:
                    eliminar_registro = '''DELETE FROM paciente WHERE curp_p=%s'''
                    self.cursor.execute(eliminar_registro,ELI)
                    self.con.commit()
                    QMessageBox.information(self, "EXITOSO","PACIENTE ELIMINADO", QMessageBox.Ok)
                else:
                    raise ValueError
            else:
                raise ArithmeticError
        except ValueError :
            QMessageBox.information(self,"NO ELIMINADO","CANCELADO",QMessageBox.Ok)
        except ArithmeticError :
            QMessageBox.information(self,"ERROR","EL PACIENTE NO EXISTE",QMessageBox.Ok)
        else:
            self.lineEdit_CURP_p.setText('')
            self.lineEdit_Nombre_p.setText('')
            self.lineEdit_Edad_p.setText('')
            self.lineEdit_Direccion_p.setText('')
        finally:
            print(" TERMINADO")
    
    
    
    #----------------CONSULTAR PACIENTE---------------------------------------------------------------------------
    #FUNCION MODIFICAR*********************************************************************************
    def Modificar_clicked(self):
        try:
            nombre =str(self.lineEdit_Nombre_p.text())
            edad = str(self.comboBoxEdad_p.currentText())
            dir =str(self.lineEdit_Direccion_p.text())
            
            curp = str(self.lineEdit_CURP_p.text())
            consultar_registro = '''SELECT * from paciente WHERE curp_p=%s'''
            self.cursor.execute(consultar_registro,curp)
            row = self.cursor.fetchone()
            
            if  row != None:
                respuesta = QMessageBox.information(self,"EXITOSO","¿ESTAS SEGURO DE QUERER MODIFICAR ESTE PACIENTE?",QMessageBox.Yes, QMessageBox.No)
                if respuesta == QMessageBox.Yes:
                    actualizar_registro = '''UPDATE paciente SET nombre_p= %s, edad_p = %s , direccion_p = %s WHERE curp_p = %s''' #%(mod,okd)
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
            self.lineEdit_CurpT.setText('')
            self.lineEdit_Nombre_p.setText('')
            self.lineEdit_CURP_p.setText('')
            self.comboBoxEdad_p.setCurrentIndex(-1)
            self.lineEdit_Direccion_p.setText('')  
        finally:
            print(" TERMINADO")
    
    #----------------CONSULTAR PACIENTE---------------------------------------------------------------------------
    #declaracion de la funcion para el boton consultar    
    def Consultar_clicked(self):
        try:
            consulta = str(self.lineEdit_CURP_p.text())
            self.cursor.execute("SELECT * from paciente WHERE curp_p =%s",consulta)
            row = self.cursor.fetchone()
                
            if  row != None:
                print(" ")
                #QMessageBox.information(self,"EXITOSO","PACIENTE ENCONTRADO",QMessageBox.Ok)   
            else:
                self.lineEdit_CurpT.setText('')
                self.lineEdit_CURP_p.setText('')
                self.lineEdit_Nombre_p.setText('')
                self.comboBoxEdad_p.setCurrentIndex(-1)
                self.lineEdit_Direccion_p.setText('')
                raise ValueError
        except ValueError :
            QMessageBox.information(self,"NO Encontrado","EL PACIENTE NO EXISTE, VERIFICA EL CURP",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            self.lineEdit_CurpT.setText(str(row[0]))
            self.lineEdit_CURP_p.setText(str(row[1]))
            self.lineEdit_Nombre_p.setText(str(row[2]))
            self.comboBoxEdad_p.setCurrentText(str(row[3]))
            self.lineEdit_Direccion_p.setText(str(row[4]))
        finally:
            print(" TERMINADO")
            
            
    #----------------CONSULTAR PACIENTE---------------------------------------------------------------------------
    #declaracion de la funcion para el boton consultar    
    def Consultar2_clicked(self):
        try:
            consulta = str(self.lineEdit_CURP_p.text())
            self.cursor.execute("SELECT * from paciente WHERE curp_p =%s",consulta)
            row = self.cursor.fetchone()
            #print(row)
                
            if  row != None:
                print(" ")
                #QMessageBox.information(self,"EXITOSO","PACIENTE ENCONTRADO",QMessageBox.Ok)   
            else:
                self.lineEdit_CurpT.setText('')
                self.lineEdit_Nombre_p.setText('')
                self.lineEdit_Edad_p.setText('')
                self.lineEdit_Direccion_p.setText('')
                raise ValueError
        except ValueError :
            QMessageBox.information(self,"NO Encontrado","EL PACIENTE NO EXISTE, VERIFICA EL CURP",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            
            self.lineEdit_CURP_p.setText(str(row[0]))
            self.lineEdit_CurpT.setText(str(row[1]))
            self.lineEdit_Nombre_p.setText(str(row[2]))
            self.lineEdit_Edad_p.setText(str(row[3]))
            self.lineEdit_Direccion_p.setText(str(row[4]))
        finally:
            print(" TERMINADO")
    

    #--------------------------------------------------BIENE---------------------------------------------------------------------------------
        
    def volverG(self):
        respuesta = QMessageBox.information(self,"SALIR","¿ESTAS SEGURO DE QUERER SALIR DE MENÚ PACIENTES?",QMessageBox.Yes, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.close() 
        else:
            self.show() 
        
    ##IR A MENU------------------
    def BotonVolverMenu_paci_clicked(self):    
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Paciente.ui", self)
        self.setWindowTitle("MENU")  
        
        PacienteWindowClass()#ACCION AGREGAR
        
        #BOTONES DE MENU
        self.pbAgregar_paci.clicked.connect(self.BotonAgregar_paci_clicked)
        self.pbModificar_paci.clicked.connect(self.BotonModificar_paci_clicked)
        self.pbConsultar_paci.clicked.connect(self.BotonConsultar_paci_clicked)
        self.pbEliminar_paci.clicked.connect(self.BotonEliminar_paci_clicked)
        
        self.pbMenuP.clicked.connect(self.volverG)
        
    #>>>IR A AGREGAR
    def BotonAgregar_paci_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Agregar_Paciente.ui", self)
        self.setWindowTitle("AGREGAR PACIENTE")

        PacienteWindowClass()#ACCION AGREGAR 
         #BOTONES DE AGREGAR--------------------------------------
        self.pbAgregar_paci.clicked.connect(self.BotonAgregar_paci_clicked)
        
        self.pbGuardar_paci.clicked.connect(self.AgregarPaciente_clicked)
        self.pbMENU_paci.clicked.connect(self.BotonVolverMenu_paci_clicked)
        self.pbEliminar_paci.clicked.connect(self.BotonEliminar_paci_clicked)
        self.pbModificar_paci.clicked.connect(self.BotonModificar_paci_clicked)
        self.pbConsultar_paci.clicked.connect(self.BotonConsultar_paci_clicked)
        self.pbCancelar_paci.clicked.connect(self.BotonCancelar_paci_clicked)
    
    #>>>IR A ELIMINAR 
    def BotonEliminar_paci_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Eliminar_Paciente.ui", self)
        self.setWindowTitle("ELIMINAR PACIENTE")
        
        PacienteWindowClass()#ACCION AGREGAR 
        self.pbDelete_paci.clicked.connect(self.EliminarPaciente_clicked)
        self.pbInfo_paci.clicked.connect(self.Consultar2_clicked)
        
        self.pbConsultar_paci.clicked.connect(self.BotonConsultar_paci_clicked)
        self.pbMENU_paci.clicked.connect(self.BotonVolverMenu_paci_clicked)
        self.pbAgregar_paci.clicked.connect(self.BotonAgregar_paci_clicked)
        self.pbModificar_paci.clicked.connect(self.BotonModificar_paci_clicked)
        self.pbCancelar_paci.clicked.connect(self.BotonCancelar_paci1_clicked)
        
    #>>>IR A CONSULTAR
    def BotonConsultar_paci_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Consultar_Paciente.ui", self)
        self.setWindowTitle("CONSULTAR PACIENTE") 
        
        PacienteWindowClass()#ACCION AGREGAR 
        self.pbInfo_paci.clicked.connect(self.Consultar2_clicked)
        
        self.pbAgregar_paci.clicked.connect(self.BotonAgregar_paci_clicked)
        self.pbMENU_paci.clicked.connect(self.BotonVolverMenu_paci_clicked)
        self.pbEliminar_paci.clicked.connect(self.BotonEliminar_paci_clicked)
        self.pbModificar_paci.clicked.connect(self.BotonModificar_paci_clicked)
        self.pbCancelar_paci.clicked.connect(self.BotonCancelar_paci1_clicked)
    #>>>IR A MODIFICAR
    def BotonModificar_paci_clicked(self):    
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Actualizar_Paciente.ui", self)
        self.setWindowTitle("ACTUALIZAR PACIENTE") 
        PacienteWindowClass()#ACCION AGREGAR 
        
        self.pbGuardar_paci.clicked.connect(self.Modificar_clicked)
        self.pbInfo_paci.clicked.connect(self.Consultar_clicked)
        
        
        self.pbConsultar_paci.clicked.connect(self.BotonConsultar_paci_clicked)
        self.pbAgregar_paci.clicked.connect(self.BotonAgregar_paci_clicked)
        self.pbMENU_paci.clicked.connect(self.BotonVolverMenu_paci_clicked)
        self.pbEliminar_paci.clicked.connect(self.BotonEliminar_paci_clicked)
        self.pbCancelar_paci.clicked.connect(self.BotonCancelar_paci_clicked)
        
if __name__ == '__main__':
    app = QApplication([])
    MyWindow = PacienteWindowClass()
    MyWindow.show()
    #app.exec_() ejecuta con o sin errores
    sys.exit(app.exec())
        