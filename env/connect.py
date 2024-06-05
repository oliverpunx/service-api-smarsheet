#conector a base oracle
import mysql.connector
import cx_Oracle
import config
import sys
import os

class Conexion():
    connection=None

    def __init__(self):
        self.connection=None

    def conectaOracle(self):
        try:
                if sys.platform.startswith("darwin"):
                    print("uno")
                    lib_dir = os.path.join(os.environ.get("HOME"), "Downloads",
                                        "instantclient_19_8")
                    print(lib_dir)
                    cx_Oracle.init_oracle_client(lib_dir=lib_dir)
                elif sys.platform.startswith("win32"):
                    print("dos")
                    lib_dir = "C:/instantclient_12_2/"
                    print(lib_dir)
                    cx_Oracle.init_oracle_client(lib_dir=lib_dir)
                elif sys.platform.startswith("win64"):
                    print("tres")
                    
                    lib_dir="C:\instantclient_12_2"
                    cx_Oracle.init_oracle_client(lib_dir=lib_dir)
                    print(lib_dir)
        except Exception as err:
                print("Ocurrió un error en el cliente BD: ")
                print(err)
                sys.exit(1)

        try:
                self.connection = cx_Oracle.connect(
                    config.username,
                    config.password,
                    config.dsn,
                    encoding=config.encoding)

                # imprime la version de la base de datos
                print("Conectado a Oracle "+self.connection.version)

        except cx_Oracle.Error as error:
                print("Ocurrió un error: "+error)

        except Exception as error:
                print("Ocurrió un error: "+type(error).__name__)                

        finally:
            return self.connection

    def closeOracle(self):
            # release the connection
            if self.connection:
                self.connection.close()

    def commitOracle(self):
            # release the connection
            if self.connection:
                self.connection.commit()                

    def conectaMysql(self):
        try:
            self.connection=mysql.connector.connect(
                host=config.hostMysql,
                port=config.portMysql,
                user=config.userMysql,
                password=config.passMysql,
                db=config.dbMysql
            )

            if self.connection.is_connected():
                print("Conectado a MySql "+self.connection.get_server_info())

            cursor=self.connection.cursor()
            cursor.execute("select id_area, descripcion from tbl_gen_area")
            #cursor.execute("select * from server_cost")
            rows=cursor.fetchall()

            for row in rows:
                print(row)    
        
        except Exception as err:
            print("Ocurrió un error al intentar conectarse a Mysql "+str(err))

        #finally:
         #   return self.connection

        
