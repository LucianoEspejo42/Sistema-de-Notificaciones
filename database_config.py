import pyodbc
import os
import logging
from dotenv import load_dotenv

logger = logging.getLogger(_name_)
load_dotenv()

class DatabaseConfig:
    def _init_(self):
        self.server = os.getenv('DB_HOST')
        self.database = os.getenv('BD_NAME')
        self.username = os.getenv('BD_USER')
        self.password = os.getenv('BD_PASSWORD')
        self.driver = os.getenv('DB_DRIVER', 'ODBC Driver 17 for SQL Server')
        
        # Validar configuración
        if not all([self.server, self.database, self.username, self.password]):
            logger.error("Faltan variables de entorno para la base de datos")
            raise ValueError("Configuración de base de datos incompleta")
    
    def test_connection(self):
        """
        Prueba la conexión a la base de datos
        """
        try:
            with pyodbc.connect(self.get_connection_string()) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 1")
                logger.info("Conexión a base de datos exitosa")
                return True
        except Exception as e:
            logger.error(f"Error probando conexión: {e}")
            return False
        
    def get_connection_string(self):
        # Configuración más robusta con timeout y opciones adicionales
        conn_str = (
            f'DRIVER={{{self.driver}}};'
            f'SERVER={self.server};'
            f'DATABASE={self.database};'
            f'UID={self.username};'
            f'PWD={self.password};'
            f'Connection Timeout=30;'
            f'Login Timeout=30;'
            f'TrustServerCertificate=yes;'
        )
        return conn_str
    
    def execute_query(self, query, params=None):
        """
        Ejecuta una consulta SELECT y retorna los resultados como lista de diccionarios
        """
        try:
            with pyodbc.connect(self.get_connection_string()) as conn:
                cursor = conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                
                # Obtener nombres de columnas
                columns = [column[0] for column in cursor.description]
                
                # Convertir resultados a diccionarios
                results = []
                for row in cursor.fetchall():
                    results.append(dict(zip(columns, row)))
                
                return results
                
        except Exception as e:
            logger.error(f"Error ejecutando consulta: {e}")
            raise
    
    def execute_non_query(self, query, params=None):
        """
        Ejecuta una consulta INSERT, UPDATE o DELETE
        """
        try:
            with pyodbc.connect(self.get_connection_string()) as conn:
                cursor = conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                conn.commit()
                return cursor.rowcount
                
        except Exception as e:
            logger.error(f"Error ejecutando comando: {e}")
            raise

# Instancia global para usar en todo el proyecto
db_config = DatabaseConfig()
