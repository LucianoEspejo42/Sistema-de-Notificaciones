from alertas_service import ProcesadorNotificaciones
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Iniciando procesador de notificaciones...")
    while True:
        try:
            ProcesadorNotificaciones.procesar_pendientes()
        except Exception as e:
            logger.error(f"Error en ciclo de procesamiento: {e}")
        
        # Esperar 60 segundos entre ejecuciones
        time.sleep(60)