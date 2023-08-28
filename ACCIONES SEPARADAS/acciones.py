import pymysql
import pandas as pd
from programa.bd import ConexionBD

class PruebaCRUD():
    def __init__(self):
        self.c = ConexionBD()
        self.con = self.c.CreateDBConnection("localhost",3306,"root","","vacunacion")
        self.cursor = self.con.cursor()

#INSERTAR REGISTROS EN LA BD--
    def insertar(self):
        try:
            nom = input("Ingresa el nombre del paciente: ")
            curp = input("Ingresa el curp del paciente: ")
            edad = int(input("Ingresa la edad del paciente: "))
            
            consulta = '''SELECT * from paciente WHERE curp_paciente=%s'''
            if curp <= 18 and consulta != None:
                insertar_registros = '''insert into paciente (nombre_paciente,curp_paciente,edad,direccion) 
                values (%s,%s,%s,%s)
                '''
                self.cursor.execute(insertar_registros,(nom,curp,edad,direc))
                self.con.commit()
            else:
                raise ValueError
        except ValueError as err:
            print("VERIFICA LOS DATOS INGRESADOS", err)
        else: # es la operacion que se va a realizar
            print("!!!INGRESADO EXITOSAMENTE!!!")
        finally:
            print(" TERMINADO")
    
    def consultar_2(self): #consultar id especifico de la tabla
        try:
            con = input("Ingresa el curp del paciente a consultar: ")
            consultar_registro = '''SELECT * from paciente WHERE curp_paciente=%s'''
            self.cursor.execute(consultar_registro,con)
            row = self.cursor.fetchone()
            
            if row  != None:
                print(row)
                while row:
                    print("nombre_paciente=%s curp_paciente=%s edad=%s  direccion=%s" %(row[0], row[1], row[2], row[3]))
                    row = self.cursor.fetchone() 
            else:
                raise ValueError
        except ValueError :
            print("VERIFICA EL CURP INGRESADO")
        else: # es la operacion que se va a realizar
            print("!!!ENCONTRADO EXITOSAMENTE!!!")
        finally:
            print(" TERMINADO")       
    
    
    def actualizar(self):
            try: 
                curp = input("Ingresa el curp del paciente a actualizar: ")


                edad = int(input("Ingresa la nueva edad: "))
                if edad <=6:
                    dir = input("Ingresa la nueva direccion: ")
                    actualizar_registro = '''UPDATE paciente SET edad = %s, direccion = %s WHERE curp_paciente = %s''' #%(mod,okd)
                    self.cursor.execute(actualizar_registro,(curp,edad,dir))
                    self.con.commit()
                else:

                    raise ValueError
            except ValueError as err:
                print("VERIFICA LOS DATOS INGRESADOS")
            else: # es la operacion que se va a realizar
                print("!!!ACTUALIZADO EXITOSAMENTE!!!")
            finally:
                print(" TERMINADO")
    
    def eliminar(self): 
        try:
            okd = input("Ingresa el curp del paciente a eliminar: ")
            consultar_registro = '''SELECT * from paciente WHERE curp_paciente=%s'''
            self.cursor.execute(consultar_registro,okd)
            row = self.cursor.fetchone()

            if row != None:
                eliminar_registro = '''DELETE FROM paciente WHERE curp_paciente=%s'''
                self.cursor.execute(eliminar_registro,okd)
                self.con.commit()
            else:
                raise ValueError
        except ValueError as err:
            print("EL ID NO EXISTE")
        else: # es la operacion que se va a realizar
            print("!!!ID ELIMINDO EXITOSAMENTE!!!")
        finally:
            print(" TERMINADO")

if __name__=="__main__":
    prueba = PruebaCRUD()
    prueba.insertar()
    #prueba.consultar_2()
    prueba.actualizar()
    #prueba.eliminar()
    