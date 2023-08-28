
from asyncio.windows_events import NULL
import sys
from PyQt5 import uic
import pandas as pd
from bd import ConexionBD

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


from enfermera import EnfermeraWindowClass
from vacuna import VacunaWindowClass
from reporteVacunas import ReporteWindowClass
from PACIENTE import PacienteWindowClass
from TUTOR import TutorWindowClass
from COMPROBANTE import ComprobanteWindowClass
from APLICAR_VACUNA import AplicarWindowClass


class MenuWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        
        #CARGAR EL ARCHIVO .UI====================================================================================================
    
        uic.loadUi("D:/PROYECTO_FINAL/Ventanas/menu.ui", self)
        self.setWindowTitle("MENU")  
        
        #BOTONES DE MENU GENERAL 
        self.pbPaciente.clicked.connect(self.AbrirPaciente) #ACCION IR A VAC
        self.pbTutor.clicked.connect(self.AbrirTutor) #ACCION IR A VAC
        self.pbEnfermera.clicked.connect(self.AbrirEnfermera) #ACCION IR A VAC
        self.pbVacuna.clicked.connect(self.AbrirVacuna) #ACCION IR A VAC
        self.pbAplicar.clicked.connect(self.AbrirAplicar) #ACCION IR A VAC
        self.pbComprobante.clicked.connect(self.AbrirComprobante) #ACCION IR A VAC
        self.pbReporte.clicked.connect(self.AbrirReporte) #ACCION IR A VAC

        
        
        #objeto de paciente instanciado
        self.paciente = PacienteWindowClass()
        
        #objeto de tutor instanciado
        self.tutor = TutorWindowClass()
        
        #objeto de enfermera instanciado
        self.enfermera = EnfermeraWindowClass()
        
        #objeto de vacuna instanciado
        self.vacuna = VacunaWindowClass()
        
        #objeto de aplicar instanciado
        self.aplicar = AplicarWindowClass()
    
        #objeto de comprobante instanciado
        self.comprobante = ComprobanteWindowClass() 
        
        
        #objeto de reporte instanciado
        self.reporte = ReporteWindowClass()   
    
    
    
    #Funcion que me permite abrir los .py
    def AbrirPaciente(self):
        self.paciente.show()
    
    def AbrirEnfermera(self):
        self.enfermera.show()
        
    def AbrirVacuna(self):
        self.vacuna.show()
        
        
    def AbrirReporte(self):
        self.reporte.show()
        
    def AbrirTutor(self):
        self.tutor.show()
        
    def AbrirComprobante(self):
        self.comprobante.show()
        
    def AbrirAplicar(self):
        self.aplicar.show()
    
if __name__ == '__main__':
    app = QApplication([])
    main = MenuWindowClass()
    main.show()
    sys.exit(app.exec())
    
    
    
        
        
