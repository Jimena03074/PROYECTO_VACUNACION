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



class AplicarWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #CARGAR EL ARCHIVO .UI
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/comprobante.ui", self)
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Aplicar_vacuna.ui", self)
        
        self.setWindowTitle("APLICAR VACUNA")

       
        #AGREGAR CONEXION DE LA BD
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","vacunacion2")
        self.cursor = self.con.cursor()
        
             
        #ASIGNA EL EVENTO AL BOTON
        #---------------------------VENTANA APLICAR VACUNA-----------------------------------
        self.pbGuardarAplicar.clicked.connect(self.Guardar_aplicacion_clicked)#pbInfo_paci
        self.pbInfo_paci.clicked.connect(self.Info_paci_clicked)#pbInfo_paci
        self.pbImprimir_apli.clicked.connect(self.Imprimir_clicked)
        self.pbCancelar_paci.clicked.connect(self.BotonCancelar_paci_clicked)
        self.pbMENU_paci.clicked.connect(self.volverGe)
        
        
        self.pbRegresa.clicked.connect(self.BotGuardar_clicked)
        
        
        
    #Boton para limpieza del formulario
    def BotonCancelar_paci_clicked(self):
        self.lineEdit_CURP_p.setText('')
        self.lineEdit_CURP_t.setText('')
        self.lineEdit_Nombre_p.setText('')
        self.lineEdit_Edad_p.setText('')
        self.comboBox_Vacuna.setCurrentIndex(-1)
        self.comboBox_Dosis.setCurrentIndex(-1)
        self.dateEdit_Fecha.setDate(QDate.currentDate())
        self.con.commit()
    
    
    
    #Funcion para Actualizar Inventario
    def ActualizarInventario(self,vac,cant):

        sql = "SELECT lote_vacuna, nombre_vacuna FROM vacuna WHERE nombre_vacuna = '%s' "  %vac
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        
    
        #Función para actualizar el inventario
        if row!=None:
            vac = str(row[0])
            
            
        #Creando la variable @x 
        vacuna = "SELECT disponibilidad into @dis FROM vacunas WHERE lote_vacuna = '%s'" %vac
        self.cursor.execute(vacuna)
        self.conne.commit()
        
        
        #Línea para hacer el decremento en inventario
        asignar = "set @dis = @dis - '%s'" %cant
        self.cursor.execute(asignar)
        self.conne.commit() 
        
        
        #Actualizando los datos en inventario
        vacuna = "update vacuna set disponibilidad = @dis where lote_vacuna = '%s'" %vac
        self.cursor.execute(vacuna)
        self.conne.commit()
        print("si funciona")
       
    
    
    
    
        
    ##----------GUARDAR INFORMACION DE LA APLICACION    
    def Guardar_aplicacion_clicked(self):
        try:
            
            """consulta = str(self.lineEdit_CURP_p.text())
            self.cursor.execute("SELECT * from comprobante WHERE curp_p=%s ",consulta)
            row = self.cursor.fetchone()
            """
            #ASIGNAR VALORES DE ENTRADA
            curp_p = str(self.lineEdit_CURP_p.text())
            curp1 = len(curp_p)
    
            curp_t = str(self.lineEdit_CURP_t.text())
            nombre_p = str(self.lineEdit_Nombre_p.text())
            edad_p = str(self.lineEdit_Edad_p.text())
            nom_vacuna = str(self.comboBox_Vacuna.currentText())
            dosis = str(self.comboBox_Dosis.currentText())
            fecha_apli = str(self.dateEdit_Fecha.text())
           
            
            if curp1 == 18:
                
                inserta_registros = '''insert into comprobante(curp_p,curp_t,nombre_p, edad_p, nombre_vacuna, dosis, fecha_apli)
                values(%s,%s,%s,%s,%s,%s,%s)'''
                datos = (curp_p,curp_t,nombre_p,edad_p,nom_vacuna,dosis,fecha_apli)
                self.cursor.execute(inserta_registros,datos)
                
                inserta_registros2 = '''insert into reporte(CurpPaciente,NombreVacuna,NoDosis,fecha)
                values(%s,%s,%s,%s)'''
                datos2 = (curp_p,nom_vacuna,dosis,fecha_apli)
                self.cursor.execute(inserta_registros2,datos2)
                self.con.commit()
                
            else:
                raise ValueError
        except ValueError:
            QMessageBox.information(self,"NO GUARDADO","VERIFICA LOS DATOS",QMessageBox.Ok)
        else: # es la operacion que se va a realizar
                """#VACIAR lINEEDITS
                self.lineEdit_CURP_p.setText('')
                self.lineEdit_CURP_t.setText('')
                self.lineEdit_Nombre_p.setText('')
                self.lineEdit_Edad_p.setText('')
                self.comboBox_Vacuna.setCurrentIndex(-1)
                self.comboBox_Dosis.setCurrentIndex(-1)
                self.dateEdit_Fecha.setDate(QDate.currentDate())
                """
                
                QMessageBox.information(self, "EXITOSO","GUARDADO CON EXITO", QMessageBox.Ok)
                    
        finally:
            print(" TERMINADO")
            
    #----------------CONSULTAR INFORMACION
    #declaracion de la funcion para el boton consultar    
    def Info_paci_clicked(self):
        consulta = str(self.lineEdit_CURP_p.text())
        self.cursor.execute("SELECT * from paciente WHERE curp_p =%s",consulta)
        row = self.cursor.fetchone()
        #print(row)
        
        if row != None:
            self.lineEdit_CURP_p.setText(str(row[0]))
            self.lineEdit_CURP_t.setText(str(row[1]))
            self.lineEdit_Nombre_p.setText(str(row[2]))
            self.lineEdit_Edad_p.setText(str(row[3]))
            #self.lineEdit_Direccion_p.setText(str(row[3]))
        else:
            QMessageBox.information(self,"NO ENCONTRADO","EL PACIENTE NO EXISTE, VERIFICA EL CURP",QMessageBox.Ok)
            #self.lineEdit_CURP_p.setText('')
            self.lineEdit_CURP_t.setText('')
            self.lineEdit_Nombre_p.setText('')
            self.lineEdit_Edad_p.setText('')
            self.comboBox_Vacuna.setCurrentIndex(-1)
            self.comboBox_Dosis.setCurrentIndex(-1)
            self.dateEdit_Fecha.setDate(QDate.currentDate())
    
    
    #----------------CONSULTAR INFORMACION
    #declaracion de la funcion para el boton consultar    ***********************************************PENDIENTE**************//******        
    def Imprimir_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/comprobante.ui", self)
        
        
        AplicarWindowClass()
        self.pbRegresa.clicked.connect(self.BotGuardar_clicked)
        
        
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

    
            
    def BotVolverA_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/comprobante.ui", self)
        self.setWindowTitle("COMPROBANTE DE VACUNACION")  
        
        AplicarWindowClass()
        self.pbRegresa.clicked.connect(self.BotGuardar_clicked)
        
        
        
    def BotGuardar_clicked(self):
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/Aplicar_vacuna.ui", self)
        self.setWindowTitle(" VACUNACION")  
        
        AplicarWindowClass()
        
        self.pbGuardarAplicar.clicked.connect(self.Guardar_aplicacion_clicked)#pbInfo_paci
        self.pbInfo_paci.clicked.connect(self.Info_paci_clicked)#pbInfo_paci
        self.pbImprimir_apli.clicked.connect(self.Imprimir_clicked)
        self.pbCancelar_paci.clicked.connect(self.BotonCancelar_paci_clicked)
        self.pbMENU_paci.clicked.connect(self.volverGe)
    
    
    def volverGe(self):
        respuesta = QMessageBox.information(self,"SALIR","¿ESTAS SEGURO DE QUERER SALIR DE APLICAR VACUNA?",QMessageBox.Yes, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.close() 
        else:
            self.show()

if __name__ == '__main__':
    app = QApplication([])
    MyWindow = AplicarWindowClass()
    MyWindow.show()
    sys.exit(app.exec())