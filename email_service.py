import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import logging
import os
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
load_dotenv()

class EmailService:
    def __init__(self):
        self.smtp_server = os.getenv('SMTP_SERVER')
        self.smtp_port = int(os.getenv('SMTP_PORT', 587))
        self.smtp_user = os.getenv('SMTP_USER')
        self.smtp_password = os.getenv('SMTP_PASSWORD')
        self.sender_name = os.getenv('EMAIL_SENDER_NAME', 'Sistema de Notificaciones')

    def enviar_email(self, destinatario, asunto, cuerpo):
        """
        Intenta enviar un email y retorna True si tiene éxito
        """
        if not all([self.smtp_server, self.smtp_user, self.smtp_password]):
            logger.error("Configuración SMTP incompleta en variables de entorno")
            return False

        try:
            msg = MIMEText(cuerpo, 'html')
            msg['Subject'] = asunto
            msg['From'] = formataddr(("Sistema de Notificaciones", "ismaelluchi436@gmail.com")) #Aqui deben cambiar con la config del servidor SMTP
            msg['To'] = destinatario

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_user, self.smtp_password)
                server.sendmail(self.smtp_user, destinatario, msg.as_string())
            
            return True
        except Exception as e:
            logger.error(f"Error enviando email a {destinatario}: {str(e)}")
            return False
