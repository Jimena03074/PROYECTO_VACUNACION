#Autor: Luis Alberto Sanchez Salazar
#Matricula: 181803050
#Fecha de creacion: 20/10/2022
#Ultima Fecha de modificacion: 13/11/2022
#Profesora: Rebeca Rodríguez Huesca
#Proyecto: Sistema de vacunacion
#Modulo del sistema: Modulo de Tutor
#Version: 2.0

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from bd import ConexionBD


class TutorWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Tutor.ui", self)
        #CARGAR EL ARCHIVO .UI
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Agregar_Tutor.ui", self)
        #self.setWindowTitle("Agregar Paciente")
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Actualizar_Tutor.ui", self)
        #self.setWindowTitle("Modificar Paciente")
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Eliminar_Tutor.ui", self)
        #self.setWindowTitle("Eliminar Paciente")
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Consultar_Tutor.ui", self)
        
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Tutor.ui", self)
        #self.setWindowTitle("Consultar Paciente")
        
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","vacunacion2")
        self.cursor = self.con.cursor()
        
        #ASIGNAR  EVENTOs A BOTONES=================================================================================================
        #BOTONES DE MENU------
        self.pbMENU.clicked.connect(self.BotonVolverMenu_clicked)
        self.pbMenuTu.clicked.connect(self.volverG)
        
        #BOTONES DE AGREGAR--------------------------------------
        self.pbGuardar_tu.clicked.connect(self.AgregarT_clicked)
        self.pbMENU.clicked.connect(self.BotonVolverMenu_clicked)
        
        self.pbEliminar_tu.clicked.connect(self.BotonEliminar_tu_clicked)
        self.pbModificar_tu.clicked.connect(self.BotonModificar_tu_clicked)
        self.pbConsultar_tu.clicked.connect(self.BotonConsultar_tu_clicked)
        self.pbCancelar.clicked.connect(self.BotonCancelar_clicked)
        
        #BOTONES DE ELIMINAR-------------------------------------
        self.pbDelete_tu.clicked.connect(self.EliminarT_clicked)
        self.pbInfo_tu.clicked.connect(self.ConsultarT_clicked)
        self.pbMENU.clicked.connect(self.BotonVolverMenu_clicked)
        
        self.pbConsultar_tu.clicked.connect(self.BotonConsultar_tu_clicked)
        self.pbAgregar_tu.clicked.connect(self.BotonAgregar_tu_clicked)
        self.pbModificar_tu.clicked.connect(self.BotonModificar_tu_clicked)
        self.pbCancelar_tu.clicked.connect(self.BotonCancelar_tu_clicked)
        
        #BOTONES DE CONSULTAR-------------------------------------
        self.pbInfo_tu.clicked.connect(self.ConsultarT_clicked)
        self.pbMENU.clicked.connect(self.BotonVolverMenu_clicked)
        
        
        self.pbAgregar_tu.clicked.connect(self.BotonAgregar_tu_clicked)
        self.pbEliminar_tu.clicked.connect(self.BotonEliminar_tu_clicked)
        self.pbModificar_tu.clicked.connect(self.BotonModificar_tu_clicked)
        self.pbCancelar.clicked.connect(self.BotonCancelar_clicked)
        
        #BOTONES DE ACTUALIZAR-------------------------------------
        self.pbGuardar_tu.clicked.connect(self.ModificarT_clicked)
        self.pbInfo_tu.clicked.connect(self.ConsultarT_clicked)
        self.pbMENU.clicked.connect(self.BotonVolverMenu_clicked)
        
        
        self.pbConsultar_tu.clicked.connect(self.BotonConsultar_tu_clicked)
        self.pbAgregar_tu.clicked.connect(self.BotonAgregar_tu_clicked)
        self.pbEliminar_tu.clicked.connect(self.BotonEliminar_tu_clicked)
        self.pbCancelar.clicked.connect(self.BotonCancelar_clicked)
    
    
    #Boton para limpieza del formulario
    def BotonCancelar_clicked(self):
        self.lineEdit_CURP.setText('')
        self.lineEdit_Nombre.setText('')
        self.lineEdit_Correo.setText('')
        self.lineEdit_Edad.setText('')
        self.lineEdit_Direccion.setText('')
        self.con.commit()
    
    def BotonCancelar_tu_clicked(self):
        self.lineEdit_CURP.setText('')
        self.lineEdit_Nombre.setText('')
        self.lineEdit_Correo.setText('')
        self.lineEdit_Edad.setText('')
        self.lineEdit_Direccion.setText('')
        self.con.commit()
    
    #Boton para limpieza del formulario
    def BotonCancelar_clicked(self):
        self.lineEdit_CURP.setText('')
        self.lineEdit_Nombre.setText('')
        self.lineEdit_Correo.setText('')
        self.lineEdit_Edad.setText('')
        self.lineEdit_Direccion.setText('')
        self.con.commit()
        
    
    
    #--------AGREGAR TUTOR---------
    #declaracion de la funcion para el boton guardar    
    def AgregarT_clicked(self):
        try:
            #ASIGNAR VALORES DE ENTRADA
            curp = str(self.lineEdit_CURP.text())
            curp1 = len(curp)
            consulta = '''SELECT curp_t from tutor WHERE curp_t=%s'''  
            self.cursor.execute(consulta,curp)
            row = self.cursor.fetchone() 
            
            if row == None and curp1 == 18: #Corrobora que no exista el datos a ingresar
                #se declaran variables para las entradas de datos
                curp=str(self.lineEdit_CURP.text())
                nombre=str(self.lineEdit_Nombre.text())
                correo=str(self.lineEdit_Correo.text())
                edad=int(self.lineEdit_Edad.text())
                direc=str(self.lineEdit_Direccion.text())
                
                inserta_registros = '''insert into tutor(curp_t, nombre_t, correo_t, edad_t,direccion_t)
                values(%s,%s,%s,%s,%s)'''
                datos = (curp, nombre, correo, edad, direc)
                self.cursor.execute(inserta_registros,datos)
                
            else:
                raise ValueError
        except ValueError:
            QMessageBox.information(self,"NO GUARDADO","VERIFICA LOS DATOS",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            #Limpia por completo el formulario
            self.lineEdit_CURP.setText('')
            self.lineEdit_Nombre.setText('')
            self.lineEdit_Correo.setText('')
            self.lineEdit_Edad.setText('')
            self.lineEdit_Direccion.setText('')
            self.con.commit()
            QMessageBox.information(self, "EXITOSO","GUARDADO CON EXITO", QMessageBox.Ok)
            
        finally:
            print(" TERMINADO")
    
    
    
    #--------------ELIMINAR TUTOR---------------------------------------------
    def EliminarT_clicked(self):
        try:
            ELI=str(self.lineEdit_CURP.text())
            consultar_registro = '''SELECT * from tutor WHERE curp_t=%s'''
            row=self.cursor.execute(consultar_registro,ELI)
            
            if row != None:
                reply = QMessageBox.information(self,"EXITOSO","¿ESTAS SEGURO DE QUERER ELIMINAR AL PACIENTE?",
                                               QMessageBox.Yes, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    eliminar_registro  ='''DELETE from tutor WHERE curp_t=%s''' #% ELI
                    row=self.cursor.execute(eliminar_registro,ELI)
                    self.con.commit()
                    QMessageBox.information(self, "EXITOSO","TUTOR ELIMINADO", QMessageBox.Ok)
                else:
                    raise ValueError
            else:
                raise ArithmeticError
        except ArithmeticError :
            QMessageBox.information(self,"ERROR","CANCELADO",QMessageBox.Ok)
        except ValueError :
            QMessageBox.information(self,"NO ELIMINADO","CANCELADO",QMessageBox.Ok)
            
        else: # es la operacion que se va a realizar
            #VACIAR lINEEDITS
            self.lineEdit_CURP.setText('')
            self.lineEdit_Nombre.setText('')
            self.lineEdit_Correo.setText('')
            self.lineEdit_Edad.setText('')
            self.lineEdit_Direccion.setText('')
        finally:
            print(" TERMINADO")
    
    
     #FUNCION CONSULTAR*********************************************************************************
    def ConsultarT_clicked(self):
        try:
            consulta = str(self.lineEdit_CURP.text())
            self.cursor.execute("SELECT * from tutor WHERE curp_t =%s",consulta)
            row = self.cursor.fetchone()
            
            if row != None:
               print('')
            else:
                raise ValueError
        except ValueError :
            QMessageBox.information(self,"NO Encontrado","EL PACIENTE NO EXISTE, VERIFICA EL CURP",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            self.lineEdit_CURP.setText(str(row[0]))
            self.lineEdit_Nombre.setText(str(row[1]))
            self.lineEdit_Edad.setText(str(row[2]))
            self.lineEdit_Correo.setText(str(row[3]))
            self.lineEdit_Direccion.setText(str(row[4]))
        finally:
            print(" TERMINADO")
    
    
    
     #FUNCION MODIFICAR*********************************************************************************
    def ModificarT_clicked(self):
        try:
            #ASIGNAR VALORES DE ENTRADA
            edad=int(self.lineEdit_Edad.text())
            correo=str(self.lineEdit_Correo.text())
            direc=str(self.lineEdit_Direccion.text())
            
            curp = str(self.lineEdit_CURP.text())
            consulta = '''SELECT * from tutor WHERE curp_t=%s'''  
            self.cursor.execute(consulta,curp)
            row = self.cursor.fetchone() 
    
                  
            if row != None: 
                respuesta = QMessageBox.information(self,"EXITOSO","¿ESTAS SEGURO DE QUERER MODIFICAR ESTE TUTOR?",QMessageBox.Yes, QMessageBox.No)
                if respuesta == QMessageBox.Yes:
                    actualizar_registro  ='''UPDATE tutor SET edad_t=%s, correo_t=%s, direccion_t=%s WHERE curp_t=%s'''
                    self.cursor.execute(actualizar_registro,( edad,correo,direc,curp))
                    self.con.commit()
                    QMessageBox.information(self, "EXITOSO","GUARDADO CON EXITO", QMessageBox.Ok)
                else: 
                    #Ignore
                    raise ValueError
            else:
                raise ArithmeticError
        except ValueError:
            QMessageBox.information(self,"NO MODIFICADO","CANCELADO",QMessageBox.Ok)
        except ArithmeticError :
            QMessageBox.information(self,"ERROR","EL TUTOR NO EXISTE, VERIFICA EL CURP",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
            #VACIAR lINEEDITS
            self.lineEdit_CURP.setText('')
            self.lineEditNomTE.setText('')
            self.lineEditEdadTE.setText('')
            self.lineEditDireccionTE.setText('') 
        finally:
            print(" TERMINADO")
    
            
    



        
    def volverG(self):
        respuesta = QMessageBox.information(self,"SALIR","¿ESTAS SEGURO DE QUERER SALIR DE MENÚ TUTORES?",QMessageBox.Yes, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.close() 
        else:
            self.show() 
     
        
    ##IR A MENU------------------
    def BotonVolverMenu_clicked(self):    
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Tutor.ui", self)
        self.setWindowTitle("MENU")  
        
        TutorWindowClass()#ACCION AGREGAR
        
        #BOTONES DE MENU
        self.pbAgregar_tu.clicked.connect(self.BotonAgregar_tu_clicked)
        self.pbModificar_tu.clicked.connect(self.BotonModificar_tu_clicked)
        self.pbConsultar_tu.clicked.connect(self.BotonConsultar_tu_clicked)
        self.pbEliminar_tu.clicked.connect(self.BotonEliminar_tu_clicked)
        
        self.pbMenuTu.clicked.connect(self.volverG)
        
    #>>>IR A AGREGAR
    def BotonAgregar_tu_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Agregar_Tutor.ui", self)
        self.setWindowTitle("AGREGAR TUTOR")

        TutorWindowClass()#ACCION AGREGAR 
         #BOTONES DE AGREGAR--------------------------------------
        self.pbAgregar_tu.clicked.connect(self.BotonAgregar_tu_clicked)
        
        self.pbGuardar_tu.clicked.connect(self.AgregarT_clicked)
        self.pbMENU.clicked.connect(self.BotonVolverMenu_clicked)
        self.pbEliminar_tu.clicked.connect(self.BotonEliminar_tu_clicked)
        self.pbModificar_tu.clicked.connect(self.BotonModificar_tu_clicked)
        self.pbConsultar_tu.clicked.connect(self.BotonConsultar_tu_clicked)
        self.pbCancelar.clicked.connect(self.BotonCancelar_clicked)
    
    #>>>IR A ELIMINAR 
    def BotonEliminar_tu_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Eliminar_Tutor.ui", self)
        self.setWindowTitle("ELIMINAR TUTOR")
        
        TutorWindowClass()#ACCION AGREGAR
        
        self.pbDelete_tu.clicked.connect(self.EliminarT_clicked)
        self.pbConsultar_tu.clicked.connect(self.BotonConsultar_tu_clicked)
        self.pbMENU.clicked.connect(self.BotonVolverMenu_clicked)
        self.pbAgregar_tu.clicked.connect(self.BotonAgregar_tu_clicked)
        self.pbModificar_tu.clicked.connect(self.BotonModificar_tu_clicked)
        self.pbInfo_tu.clicked.connect(self.ConsultarT_clicked)
        self.pbCancelar_tu.clicked.connect(self.BotonCancelar_tu_clicked)
    
    #>>>IR A CONSULTAR
    def BotonConsultar_tu_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Consultar_Tutor.ui", self)
        self.setWindowTitle("CONSULTAR TUTOR")
        
        TutorWindowClass()#ACCION AGREGAR
        
        self.pbAgregar_tu.clicked.connect(self.BotonAgregar_tu_clicked)
        self.pbMENU.clicked.connect(self.BotonVolverMenu_clicked)
        self.pbEliminar_tu.clicked.connect(self.BotonEliminar_tu_clicked)
        self.pbModificar_tu.clicked.connect(self.BotonModificar_tu_clicked)
        self.pbInfo_tu.clicked.connect(self.ConsultarT_clicked)
        self.pbCancelar.clicked.connect(self.BotonCancelar_clicked)
    
    #>>>IR A MODIFICAR
    def BotonModificar_tu_clicked(self):    
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Actualizar_Tutor.ui", self)
        self.setWindowTitle("MODIFICAR TUTOR")
        TutorWindowClass()#ACCION AGREGAR
        
        self.pbGuardar_tu.clicked.connect(self.ModificarT_clicked)
        self.pbConsultar_tu.clicked.connect(self.BotonConsultar_tu_clicked)
        
        self.pbAgregar_tu.clicked.connect(self.BotonAgregar_tu_clicked)
        self.pbMENU.clicked.connect(self.BotonVolverMenu_clicked)
        self.pbEliminar_tu.clicked.connect(self.BotonEliminar_tu_clicked)
        self.pbInfo_tu.clicked.connect(self.ConsultarT_clicked)
        self.pbCancelar.clicked.connect(self.BotonCancelar_clicked)
    
if __name__ == '__main__':
    app = QApplication([])
    MyWindow = TutorWindowClass()
    MyWindow.show()
    #app.exec_() ejecuta con o sin errores
    sys.exit(app.exec())