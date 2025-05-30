
# Sistema de Notificaciones

Sistema automatizado para el procesamiento y envío de notificaciones por email con dashboard de visualización.

## Características

- **Procesamiento automático** de notificaciones pendientes
- **Envío de emails** con configuración SMTP
- **Dashboard interactivo** con gráficos de tendencias y estados
- **Auditoría completa** de todas las operaciones

## Estructura del Proyecto

```
├── Documentación              # Guardo la documentación del proyecto   
├── main.py                    # Punto de entrada principal
├── alertas_service.py         # Lógica de procesamiento de notificaciones
├── database_config.py         # Configuración y conexión a base de datos
├── email_service.py           # Servicio de envío de emails
├── dashboard_plotly.py        # Dashboard de visualización
└── .env                       # Variables de entorno (crear manualmente)
```

## Instalación

1. **Instalar dependencias**:
```bash
pip install pyodbc plotly pandas numpy dash python-dotenv
```

2. **Configurar variables de entorno** en archivo `.env`:
```env
# Base de datos
DB_HOST=tu_servidor
BD_NAME=tu_base_datos
BD_USER=tu_usuario
BD_PASSWORD=tu_contraseña
DB_DRIVER=ODBC Driver 17 for SQL Server

# Email SMTP
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=tu_email@gmail.com
SMTP_PASSWORD=tu_contraseña_app
EMAIL_SENDER_NAME=Sistema de Notificaciones
```

## Uso

### Procesamiento de Notificaciones
```bash
python main.py
```
Ejecuta el procesador en bucle continuo, revisando notificaciones pendientes cada 60 segundos.

### Dashboard de Visualización
```bash
python dashboard_plotly.py
```
Genera gráficos de tendencias y distribución de estados de las notificaciones.

## Base de Datos

El sistema requiere las siguientes tablas:

- `Notificaciones` - Almacena las notificaciones a enviar
- `Notificaciones_Tipo` - Define tipos de notificaciones con templates
- `Auditoria` - Registra todas las acciones del sistema

## Estados de Notificaciones

- **pendiente** - Esperando ser procesada
- **enviado** - Enviada exitosamente
- **error** - Error en el envío

## Logs y Monitoreo

El sistema genera logs detallados de todas las operaciones:
- Conexiones a base de datos
- Envío de emails
- Errores y excepciones
- Auditoría de cambios de estado

## Configuración SMTP

Para Gmail, usar:
- Habilitar autenticación de 2 factores
- Generar contraseña de aplicación
