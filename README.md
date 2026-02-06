# ARP & DNS Spoofing
# 🔧 Network Security Tool

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.8+-yellow.svg)
![Status](https://img.shields.io/badge/status-production-success.svg)

*Herramienta automatizada para configuración, auditoría y seguridad de infraestructura de red*

</div>

---

## 📋 Tabla de Contenidos

- [Objetivo del Script](#-objetivo-del-script)
- [Características Principales](#-características-principales)
- [Capturas de Pantalla](#-capturas-de-pantalla)
- [Topología de Red](#-topología-de-red)
- [Parámetros de Configuración](#-parámetros-de-configuración)
- [Requisitos del Sistema](#-requisitos-del-sistema)
- [Instalación](#-instalación)
- [Uso y Ejemplos](#-uso-y-ejemplos)
- [Medidas de Mitigación](#-medidas-de-mitigación)
- [Troubleshooting](#-troubleshooting)
- [Contribución](#-contribución)
- [Licencia](#-licencia)

---

## 🎯 Objetivo del Script

Este proyecto implementa un script de ARP Spoofing combinado con DNS Spoofing, con fines exclusivamente educativos y de laboratorio, ejecutado en un entorno controlado.
El objetivo es demostrar cómo un atacante puede posicionarse como Man-in-the-Middle (MitM) y redirigir el tráfico DNS de una víctima hacia un servidor falso.

### Objetivo 

El objetivo de este script es simular, en un entorno de laboratorio controlado, un ataque de ARP Spoofing y DNS Spoofing para posicionar al atacante como Man-in-the-Middle, interceptar el tráfico de red y redirigir consultas DNS hacia un servidor falso, con fines exclusivamente educativos y de análisis de seguridad.

## 🖼️ Capturas de Pantalla

Las capturas incluidas en este repositorio documentan el proceso completo del laboratorio:

- Topología de red del escenario
- 
  <img width="1366" height="893" alt="image" src="https://github.com/user-attachments/assets/68c3e16d-299e-403a-857e-65989d1adca4" />
---
- Ejecución del ataque ARP Spoofing
- 
  <img width="672" height="137" alt="image" src="https://github.com/user-attachments/assets/5271155f-80c7-4320-933f-06a40b855aa9" />

- Archivo de configuración del DNS Spoofing
- 
 <img width="672" height="160" alt="image" src="https://github.com/user-attachments/assets/2c0a73d3-dfde-465a-80b9-00b77d9392f6" />

- Tráfico DNS interceptado
- 
  <img width="599" height="209" alt="image" src="https://github.com/user-attachments/assets/389a0665-f352-4451-90bd-3edfb956e11c" />
---
- Redirección exitosa al sitio web falso

---

## ✨ Características Principales

| Característica | Descripción | Estado |
|----------------|-------------|--------|
| **Multi-vendor** | Soporte para Cisco, HP, Juniper | ✅ Operativo |
| **VLAN Management** | Creación, modificación y eliminación de VLANs | ✅ Operativo |
| **Security Audit** | Escaneo de vulnerabilidades conocidas | ✅ Operativo |
| **Backup Config** | Respaldo automático de configuraciones | ✅ Operativo |
| **API REST** | Integración con sistemas externos | 🚧 Beta |
| **Web Dashboard** | Interfaz gráfica de monitoreo | 🚧 Desarrollo |

---

## 📸 Capturas de Pantalla

### Dashboard Principal

![Dashboard Principal](./docs/screenshots/dashboard.png)

*Vista general del estado de la red con métricas en tiempo real*

### Configuración de VLANs

![Configuración VLANs](./docs/screenshots/vlan-config.png)

*Interfaz de configuración de VLANs con validación automática*

### Reporte de Seguridad

![Security Report](./docs/screenshots/security-report.png)

*Reporte detallado de auditoría de seguridad con recomendaciones*

### Ejecución en CLI

```bash
$ python network_tool.py --scan --target 192.168.1.0/24

[INFO] Iniciando escaneo de red...
[INFO] Dispositivos detectados: 15
[OK]   Switch-Core-01 (192.168.1.1) - Configuración válida
[WARN] Switch-Access-03 (192.168.1.10) - VLAN no autorizada detectada
[OK]   Router-Edge-01 (192.168.1.254) - Sin vulnerabilidades
[INFO] Generando reporte en /reports/scan_2024-02-06_14-30.pdf
[SUCCESS] Escaneo completado en 45 segundos
```

---

## 🌐 Topología de Red

### Diagrama de Topología

                                  (Cloud)
                                     |
                    +----------------+----------------+
                    |                                 |
                 e0/0                               e0/0
                  R-SD                              R-STG
           (15.0.7.0/24)      10.0.0.0/30           (15.0.8.0/24)
                 e0/2 -------------------------------- e0/2
                    |                                   |
                 e0/1              PNET              e0/1
                    |                                   |
                 e0/0                               e0/0
                  SW-SD                             SW-STG
                 /    \                             /    \
              e0/2    e0/1                       e0/1    e0/2
               |        |                         |        |
              e0       e0                       eth0     eth0
            Victima  Atacante                    TI       TI


Elementos de la red:
- MY HOUSE: Conexión a Internet/Cloud
- R-SD: Router Santo Domingo (izquierda)
- R-STG: Router Santiago (derecha)
- SW-SD: Switch Santo Domingo (izquierda)
- SW-STG: Switch Santiago (derecha)
- PNET: Internet Provider (centro)
- Dispositivos finales: Victima, Atacante (en SD) y dos TI (en STG)

Configuración:
- Red entre routers: 10.1.0.0/30
- ARP & DNS SPOOFING & SUPLIDOS (indicado en rojo)
```

### Tabla de Interfaces

#### Core Switch (192.168.1.1)

| Interface | Tipo | Modo | VLANs | Descripción |
|-----------|------|------|-------|-------------|
| Gi0/1 | Ethernet | Trunk | 1,10,20,30,99 | Uplink a Router Edge |
| Gi0/2 | Ethernet | Trunk | 1,10,20,30,99 | Downlink a Access-SW-01 |
| Gi0/3 | Ethernet | Trunk | 1,10,20,30,99 | Downlink a Access-SW-02 |
| Gi0/4 | Ethernet | Trunk | 1,10,20,30,99 | Downlink a Access-SW-03 |
| VLAN 1 | SVI | - | - | Management (192.168.1.1/24) |

#### Access Switches

| Dispositivo | Interface | Modo | VLAN | Descripción |
|-------------|-----------|------|------|-------------|
| SW-01 | Gi0/1 | Trunk | All | Uplink a Core |
| SW-01 | Gi0/2-24 | Access | 10 | Puertos de usuario IT |
| SW-02 | Gi0/1 | Trunk | All | Uplink a Core |
| SW-02 | Gi0/2-24 | Access | 20 | Puertos de usuario Admin |
| SW-03 | Gi0/1 | Trunk | All | Uplink a Core |
| SW-03 | Gi0/2-24 | Access | 30 | Puertos de usuario Guest |

### Configuración de VLANs

| VLAN ID | Nombre | Subnet | Gateway | Propósito |
|---------|--------|--------|---------|-----------|
| 1 | Management | 192.168.1.0/24 | 192.168.1.254 | Gestión de dispositivos |
| 10 | IT_Department | 10.10.10.0/24 | 10.10.10.1 | Departamento de TI |
| 20 | Admin | 10.10.20.0/24 | 10.10.20.1 | Administración |
| 30 | Guest | 10.10.30.0/24 | 10.10.30.1 | Red de invitados (aislada) |
| 99 | Native | - | - | VLAN nativa para trunks |

### Direccionamiento IP

#### Segmento de Gestión (192.168.1.0/24)

| Dispositivo | IP Address | Máscara | Gateway | Descripción |
|-------------|------------|---------|---------|-------------|
| Router-Edge-01 | 192.168.1.254 | /24 | - | Gateway principal |
| Core-Switch-01 | 192.168.1.1 | /24 | 192.168.1.254 | Switch core |
| Access-SW-01 | 192.168.1.10 | /24 | 192.168.1.254 | Switch acceso piso 1 |
| Access-SW-02 | 192.168.1.11 | /24 | 192.168.1.254 | Switch acceso piso 2 |
| Access-SW-03 | 192.168.1.12 | /24 | 192.168.1.254 | Switch acceso piso 3 |
| Server-Management | 192.168.1.100 | /24 | 192.168.1.254 | Servidor de gestión |

#### Segmentos de Usuario

| Red | Rango Usable | Broadcast | Hosts Disponibles |
|-----|--------------|-----------|-------------------|
| 10.10.10.0/24 | 10.10.10.1 - 10.10.10.254 | 10.10.10.255 | 254 |
| 10.10.20.0/24 | 10.10.20.1 - 10.10.20.254 | 10.10.20.255 | 254 |
| 10.10.30.0/24 | 10.10.30.1 - 10.10.30.254 | 10.10.30.255 | 254 |

---

## ⚙️ Parámetros de Configuración

### Archivo de Configuración Principal (`config.yaml`)

```yaml
# Configuración General
general:
  log_level: INFO
  log_file: /var/log/network_tool/app.log
  max_threads: 10
  timeout: 30
  retry_attempts: 3

# Credenciales de Dispositivos
credentials:
  default_username: admin
  default_password: ${NETWORK_PASSWORD}  # Variable de entorno
  enable_secret: ${ENABLE_SECRET}
  ssh_port: 22
  telnet_port: 23

# Dispositivos de Red
devices:
  - hostname: Core-Switch-01
    ip: 192.168.1.1
    device_type: cisco_ios
    role: core
    credentials_group: default
    
  - hostname: Access-SW-01
    ip: 192.168.1.10
    device_type: cisco_ios
    role: access
    credentials_group: default

# VLANs a Configurar
vlans:
  - id: 10
    name: IT_Department
    subnet: 10.10.10.0/24
    gateway: 10.10.10.1
    dhcp_pool:
      start: 10.10.10.100
      end: 10.10.10.200
      
  - id: 20
    name: Admin
    subnet: 10.10.20.0/24
    gateway: 10.10.20.1
    dhcp_pool:
      start: 10.10.20.100
      end: 10.10.20.200

# Políticas de Seguridad
security_policies:
  enable_port_security: true
  max_mac_addresses: 2
  violation_mode: restrict
  enable_dhcp_snooping: true
  enable_dynamic_arp_inspection: true
  enable_spanning_tree_bpduguard: true

# Auditoría
audit:
  enable_compliance_check: true
  standards:
    - PCI-DSS
    - ISO27001
  generate_pdf_report: true
  email_reports_to:
    - admin@empresa.com
    - security@empresa.com

# Backup
backup:
  enable_auto_backup: true
  backup_path: /backups/network_configs
  retention_days: 30
  schedule: "0 2 * * *"  # Cron: 2 AM diario
```

### Parámetros de Línea de Comandos

```bash
# Sintaxis general
python network_tool.py [COMANDO] [OPCIONES]

# Comandos disponibles
COMANDOS:
  scan          Escanear dispositivos de red
  configure     Aplicar configuraciones
  audit         Realizar auditoría de seguridad
  backup        Respaldar configuraciones
  restore       Restaurar desde backup
  report        Generar reportes

OPCIONES GLOBALES:
  -c, --config FILE         Archivo de configuración (default: config.yaml)
  -v, --verbose             Modo verboso
  -q, --quiet               Modo silencioso
  -l, --log-file FILE       Archivo de log personalizado
  -h, --help                Mostrar ayuda

OPCIONES DE ESCANEO:
  --target IP/CIDR          IP o rango a escanear
  --port PUERTO             Puerto específico (default: 22)
  --timeout SEGUNDOS        Timeout de conexión (default: 30)
  --threads NUM             Número de threads (default: 10)

OPCIONES DE CONFIGURACIÓN:
  --device HOSTNAME         Dispositivo específico
  --vlan ID                 VLAN específica
  --dry-run                 Simular sin aplicar cambios
  --force                   Forzar configuración sin confirmación

OPCIONES DE AUDITORÍA:
  --standard ESTÁNDAR       Estándar a verificar (PCI-DSS, ISO27001)
  --severity NIVEL          Nivel mínimo de severidad (low, medium, high, critical)
  --output FORMAT           Formato de salida (json, xml, pdf, html)

OPCIONES DE BACKUP:
  --destination PATH        Ruta de destino del backup
  --encrypt                 Encriptar backup con AES-256
  --compress                Comprimir archivos de backup
```

### Variables de Entorno

```bash
# Archivo .env (no incluir en repositorio)
NETWORK_PASSWORD="SecureP@ssw0rd123"
ENABLE_SECRET="EnableS3cr3t456"
API_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
SMTP_SERVER="smtp.empresa.com"
SMTP_PORT="587"
SMTP_USER="notifications@empresa.com"
SMTP_PASSWORD="SmtpP@ss789"
ENCRYPTION_KEY="32-byte-hex-key-here"
```

### Ejemplos de Uso

```bash
# Escanear red completa
python network_tool.py scan --target 192.168.1.0/24 --verbose

# Configurar VLANs en dispositivo específico
python network_tool.py configure --device Core-Switch-01 --vlan 10,20,30

# Auditoría de seguridad con reporte PDF
python network_tool.py audit --standard PCI-DSS --output pdf --severity high

# Backup encriptado de todos los dispositivos
python network_tool.py backup --encrypt --compress --destination /secure/backups/

# Simulación de configuración (dry-run)
python network_tool.py configure --dry-run --vlan 40

# Restaurar configuración desde backup
python network_tool.py restore --device Access-SW-01 --backup /backups/2024-02-06/

# Generar reporte de estado mensual
python network_tool.py report --type monthly --email admin@empresa.com
```

---

## 📦 Requisitos del Sistema

### Requisitos de Hardware

| Componente | Mínimo | Recomendado |
|------------|--------|-------------|
| CPU | 2 cores @ 2.0 GHz | 4 cores @ 2.5 GHz |
| RAM | 2 GB | 4 GB |
| Disco | 10 GB libres | 50 GB SSD |
| Red | 100 Mbps | 1 Gbps |

### Requisitos de Software

#### Sistema Operativo

- ✅ Linux (Ubuntu 20.04+, CentOS 8+, Debian 11+)
- ✅ macOS 11.0+
- ✅ Windows 10/11 (con WSL2 recomendado)

#### Python y Dependencias

```bash
# Versión de Python
Python 3.8 o superior (3.10+ recomendado)

# Librerías principales
netmiko >= 4.1.0          # Conexión SSH a dispositivos
paramiko >= 2.12.0        # Protocolo SSH
pyyaml >= 6.0             # Parsing de configuración
jinja2 >= 3.1.0           # Templates de configuración
cryptography >= 39.0.0    # Encriptación
requests >= 2.28.0        # HTTP requests
pandas >= 1.5.0           # Análisis de datos
matplotlib >= 3.6.0       # Gráficos de reportes
reportlab >= 3.6.0        # Generación de PDFs
```

#### Software Adicional

```bash
# SSH Client
OpenSSH >= 8.0

# Git (para clonar repositorio)
git >= 2.30

# Opcional: Docker
Docker >= 20.10 (para despliegue en contenedor)
```

### Dispositivos de Red Compatibles

#### Switches

| Fabricante | Modelos Soportados | Versión OS | Estado |
|------------|-------------------|------------|--------|
| Cisco | Catalyst 2960, 3560, 3750, 9300 | IOS 15.0+ | ✅ Completo |
| HP/Aruba | ProCurve 2530, 2920, 3810 | K.15+ | ✅ Completo |
| Juniper | EX2200, EX3300, EX4300 | Junos 12.3+ | ⚠️ Beta |
| Dell | PowerConnect 6224, N2000, N3000 | DNOS 9+ | 🚧 Desarrollo |

#### Routers

| Fabricante | Modelos Soportados | Versión OS | Estado |
|------------|-------------------|------------|--------|
| Cisco | ISR 1900, 2900, 4000 | IOS 15.0+ | ✅ Completo |
| MikroTik | RB3011, RB4011, CCR | RouterOS 6.4+ | ✅ Completo |

### Conectividad Requerida

- ✅ Acceso SSH (puerto 22) a dispositivos de red
- ✅ Acceso a Internet (para actualizaciones y descargas de CVE)
- ✅ SMTP (puerto 587) para envío de reportes por email
- ⚠️ Acceso Telnet (puerto 23) - **NO RECOMENDADO** excepto para dispositivos legacy

### Permisos y Accesos

#### Usuario del Sistema

```bash
# El usuario debe tener permisos para:
- Lectura/escritura en /var/log/network_tool/
- Lectura/escritura en /backups/network_configs/
- Lectura del archivo de configuración
- Ejecución de Python y sus módulos
```

#### Credenciales de Red

```yaml
# Privilegios mínimos requeridos en dispositivos:
- Nivel de privilegio: 15 (enable mode)
- Comandos necesarios:
  * show running-config
  * show vlan
  * configure terminal
  * write memory
  * copy running-config startup-config
```

---

## 🚀 Instalación

### Método 1: Instalación Manual

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/network-security-tool.git
cd network-security-tool

# 2. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# 4. Copiar y configurar archivo de configuración
cp config.yaml.example config.yaml
nano config.yaml  # Editar con tus parámetros

# 5. Crear archivo de variables de entorno
cp .env.example .env
nano .env  # Agregar credenciales

# 6. Crear directorios necesarios
mkdir -p logs backups reports

# 7. Verificar instalación
python network_tool.py --version
python network_tool.py --help
```

### Método 2: Instalación con Docker

```bash
# 1. Clonar repositorio
git clone https://github.com/tu-usuario/network-security-tool.git
cd network-security-tool

# 2. Construir imagen
docker build -t network-tool:latest .

# 3. Ejecutar contenedor
docker run -d \
  --name network-tool \
  -v $(pwd)/config.yaml:/app/config.yaml \
  -v $(pwd)/backups:/app/backups \
  -v $(pwd)/logs:/app/logs \
  -e NETWORK_PASSWORD=${NETWORK_PASSWORD} \
  network-tool:latest

# 4. Ejecutar comandos en el contenedor
docker exec -it network-tool python network_tool.py scan --target 192.168.1.0/24
```

### Método 3: Instalación con pip (paquete publicado)

```bash
# Instalar desde PyPI
pip install network-security-tool

# Inicializar configuración
network-tool init

# Configurar credenciales
network-tool config --set-credentials
```

---

## 💻 Uso y Ejemplos

### Ejemplo 1: Escaneo Básico de Red

```bash
# Escanear subnet completa
python network_tool.py scan --target 192.168.1.0/24

# Salida esperada:
[2024-02-06 14:30:15] INFO: Iniciando escaneo...
[2024-02-06 14:30:16] SUCCESS: 192.168.1.1 - Core-Switch-01 (Cisco IOS 15.2)
[2024-02-06 14:30:17] SUCCESS: 192.168.1.10 - Access-SW-01 (Cisco IOS 15.0)
[2024-02-06 14:30:18] SUCCESS: 192.168.1.11 - Access-SW-02 (Cisco IOS 15.0)
[2024-02-06 14:30:19] WARNING: 192.168.1.50 - Unknown device (Timeout)
[2024-02-06 14:30:45] INFO: Escaneo completado: 3/4 dispositivos alcanzables
```

### Ejemplo 2: Configuración de VLANs

```bash
# Aplicar configuración de VLAN 40 en todos los switches
python network_tool.py configure --vlan 40 --verbose

# Configuración aplicada:
Creating VLAN 40...
Setting VLAN name to "Developers"...
Configuring gateway 10.10.40.1...
Enabling DHCP snooping...
Saving configuration...
[SUCCESS] VLAN 40 configurada en 3 dispositivos
```

### Ejemplo 3: Auditoría de Seguridad

```bash
# Auditar cumplimiento PCI-DSS
python network_tool.py audit --standard PCI-DSS --output pdf

# Reporte generado:
╔══════════════════════════════════════════════╗
║      REPORTE DE AUDITORÍA PCI-DSS           ║
╠══════════════════════════════════════════════╣
║ Fecha: 2024-02-06 14:45:00                  ║
║ Dispositivos auditados: 5                    ║
║ Hallazgos críticos: 2                        ║
║ Hallazgos altos: 5                           ║
║ Hallazgos medios: 12                         ║
║ Estado general: REQUIERE ATENCIÓN           ║
╚══════════════════════════════════════════════╝

Archivo generado: /reports/pci-dss-audit-2024-02-06.pdf
```

---

## 🛡️ Medidas de Mitigación

### Análisis de Riesgos y Controles

| ID | Riesgo Identificado | Severidad | Probabilidad | Impacto | Medida de Mitigación Implementada |
|----|---------------------|-----------|--------------|---------|-----------------------------------|
| R-001 | Credenciales expuestas en configuración | **CRÍTICO** | Media | Alto | • Uso obligatorio de variables de entorno<br>• Encriptación AES-256 de archivos de configuración<br>• Integración con HashiCorp Vault (opcional)<br>• Nunca almacenar credenciales en código |
| R-002 | Acceso no autorizado a dispositivos | **ALTO** | Alta | Crítico | • Autenticación SSH con claves públicas<br>• Implementación de 2FA en acceso administrativo<br>• Logging de todos los intentos de acceso<br>• Rate limiting: máx 3 intentos/minuto |
| R-003 | Modificación no autorizada de configuraciones | **ALTO** | Media | Alto | • Modo dry-run obligatorio antes de cambios<br>• Backup automático pre-cambio<br>• Rollback automático en caso de fallo<br>• Auditoría de cambios con firma digital |
| R-004 | Interrupción del servicio de red | **ALTO** | Baja | Crítico | • Validación sintáctica antes de aplicar configs<br>• Timeout de 30s en operaciones críticas<br>• Mantener sesión de emergencia activa<br>• Plan de rollback documentado |
| R-005 | Inyección de comandos maliciosos | **CRÍTICO** | Media | Crítico | • Sanitización de todos los inputs<br>• Lista blanca de comandos permitidos<br>• Validación con expresiones regulares<br>• Modo sandbox para testing |
| R-006 | Fuga de información sensible en logs | **MEDIO** | Alta | Medio | • Ofuscación automática de credenciales en logs<br>• Rotación de logs cada 7 días<br>• Permisos 600 en archivos de log<br>• Logs almacenados en volumen encriptado |
| R-007 | Man-in-the-Middle en comunicaciones | **ALTO** | Baja | Alto | • Uso exclusivo de SSH con verificación de host keys<br>• Rechazo de conexiones Telnet no encriptadas<br>• Verificación de certificados SSL/TLS<br>• Alertas de cambio de fingerprint |
| R-008 | Denegación de servicio por sobrecarga | **MEDIO** | Media | Medio | • Límite de 10 threads concurrentes<br>• Cola de trabajos con priorización<br>• Circuit breaker en conexiones fallidas<br>• Throttling de operaciones intensivas |
| R-009 | Pérdida de backups de configuración | **ALTO** | Baja | Alto | • Backups automáticos diarios a las 2 AM<br>• Replicación en 3 ubicaciones físicas<br>• Verificación de integridad SHA-256<br>• Retención de 30 días + archivos mensuales |
| R-010 | Ejecución de código arbitrario | **CRÍTICO** | Baja | Crítico | • Validación estricta de plugins/extensiones<br>• Ejecución en contenedor Docker aislado<br>• Principio de mínimo privilegio<br>• Análisis estático de código con Bandit |

### Controles de Seguridad Implementados

#### 1. Autenticación y Autorización

```yaml
# Control de acceso basado en roles (RBAC)
roles:
  administrator:
    permissions:
      - read_config
      - write_config
      - delete_config
      - execute_audit
      - manage_users
    
  operator:
    permissions:
      - read_config
      - execute_audit
      - create_backup
    
  auditor:
    permissions:
      - read_config
      - execute_audit
      - view_reports

# Autenticación multi-factor
mfa:
  enabled: true
  method: totp  # Time-based One-Time Password
  required_for:
    - configuration_changes
    - backup_restoration
    - user_management
```

#### 2. Encriptación

```python
# Encriptación de credenciales en reposo
- Algoritmo: AES-256-GCM
- Gestión de claves: HashiCorp Vault o AWS KMS
- Rotación de claves: cada 90 días

# Encriptación en tránsito
- Protocolo: SSH v2, TLS 1.3
- Cifrados permitidos: 
  * ECDHE-RSA-AES256-GCM-SHA384
  * ECDHE-RSA-AES128-GCM-SHA256
- Cifrados prohibidos: DES, 3DES, RC4, MD5
```

#### 3. Logging y Auditoría

```python
# Eventos registrados
logged_events = [
    'authentication_attempt',
    'authentication_success',
    'authentication_failure',
    'configuration_change',
    'backup_created',
    'backup_restored',
    'audit_executed',
    'critical_error',
    'privilege_escalation',
    'suspicious_activity'
]

# Formato de log
{
    "timestamp": "2024-02-06T14:30:15.123Z",
    "level": "INFO",
    "user": "admin@empresa.com",
    "source_ip": "10.10.10.100",
    "action": "configuration_change",
    "device": "Core-Switch-01",
    "details": "Created VLAN 40",
    "result": "success",
    "session_id": "abc123def456"
}
```

#### 4. Validación de Entrada

```python
# Validación de inputs críticos
def validate_vlan_id(vlan_id):
    """Valida ID de VLAN según IEEE 802.1Q"""
    if not isinstance(vlan_id, int):
        raise ValueError("VLAN ID debe ser entero")
    if not 1 <= vlan_id <= 4094:
        raise ValueError("VLAN ID fuera de rango válido (1-4094)")
    if vlan_id == 1002 or vlan_id == 1003 or vlan_id == 1004 or vlan_id == 1005:
        raise ValueError("VLAN reservada para uso interno")
    return True

# Sanitización de comandos
ALLOWED_COMMANDS_REGEX = r'^(show|configure|copy|write|enable|exit)\s.*$'
FORBIDDEN_PATTERNS = ['rm ', 'del ', 'format', 'erase', '| sh']

def sanitize_command(command):
    """Previene inyección de comandos"""
    if any(pattern in command.lower() for pattern in FORBIDDEN_PATTERNS):
        raise SecurityError("Comando contiene patrón prohibido")
    if not re.match(ALLOWED_COMMANDS_REGEX, command, re.IGNORECASE):
        raise SecurityError("Comando no permitido")
    return command.strip()
```

#### 5. Rate Limiting y Protección DDoS

```python
# Configuración de rate limiting
rate_limits = {
    'authentication': {
        'max_attempts': 3,
        'window_seconds': 300,  # 5 minutos
        'lockout_minutes': 30
    },
    'api_calls': {
        'max_requests': 100,
        'window_seconds': 60,  # 1 minuto
        'burst_size': 10
    },
    'concurrent_connections': {
        'max_per_ip': 5,
        'max_total': 50
    }
}
```

#### 6. Backup y Recuperación

```bash
# Estrategia de backup 3-2-1
# - 3 copias de datos
# - 2 medios diferentes (disco + cloud)
# - 1 copia off-site

# Backup automático
Programación: Diario a las 02:00 AM
Retención: 
  - Diarios: 7 días
  - Semanales: 4 semanas
  - Mensuales: 12 meses
  - Anuales: 5 años

# Verificación de integridad
Algoritmo: SHA-256
Frecuencia: En cada backup
Alertas: Si hash no coincide

# Encriptación de backups
Algoritmo: AES-256
Compresión: gzip nivel 9
Ubicaciones:
  1. /backups/local/ (RAID-1)
  2. AWS S3 (us-east-1)
  3. Azure Blob Storage (offsite)
```

#### 7. Monitoreo de Seguridad

```python
# Alertas de seguridad configuradas
security_alerts = {
    'critical': {
        'multiple_failed_logins': {
            'threshold': 5,
            'window_minutes': 10,
            'action': 'lock_account + notify_admin'
        },
        'unauthorized_config_change': {
            'threshold': 1,
            'action': 'rollback + notify_security_team'
        },
        'suspicious_command': {
            'patterns': ['rm -rf', 'format', 'erase'],
            'action': 'block + log + alert'
        }
    },
    'high': {
        'unusual_login_location': {
            'action': 'require_mfa + notify_user'
        },
        'configuration_deviation': {
            'action': 'create_incident + notify_admin'
        }
    }
}
```

### Matriz de Cumplimiento Normativo

| Estándar | Requisito | Control Implementado | Estado |
|----------|-----------|---------------------|--------|
| **ISO 27001** | A.9.4.2 - Procedimiento seguro de inicio de sesión | MFA + SSH keys + rate limiting | ✅ Completo |
| **ISO 27001** | A.12.3.1 - Copias de respaldo | Backup automático 3-2-1 | ✅ Completo |
| **ISO 27001** | A.12.4.1 - Registro de eventos | Logging centralizado con timestamps | ✅ Completo |
| **PCI-DSS** | Req. 2.2 - Configuraciones seguras | Templates hardened + auditoría | ✅ Completo |
| **PCI-DSS** | Req. 8.2 - Autenticación multi-factor | TOTP implementado | ✅ Completo |
| **PCI-DSS** | Req. 10.2 - Registros de auditoría | Logs inmutables en WORM storage | ✅ Completo |
| **NIST CSF** | ID.AM-1 - Inventario de activos | Escaneo y catalogación automática | ✅ Completo |
| **NIST CSF** | PR.AC-4 - Control de acceso | RBAC + principio mínimo privilegio | ✅ Completo |
| **GDPR** | Art. 32 - Seguridad del tratamiento | Encriptación AES-256 + pseudonimización | ⚠️ Parcial |

### Plan de Respuesta a Incidentes

```markdown
## Procedimiento en Caso de Incidente de Seguridad

### FASE 1: DETECCIÓN (0-15 minutos)
1. Sistema detecta anomalía y genera alerta
2. Equipo de seguridad notificado automáticamente
3. Revisión inicial de logs y métricas

### FASE 2: CONTENCIÓN (15-60 minutos)
1. Aislar sistemas afectados
2. Preservar evidencia digital
3. Ejecutar snapshot de estado actual
4. Bloquear accesos comprometidos

### FASE 3: ERRADICACIÓN (1-4 horas)
1. Identificar causa raíz del incidente
2. Eliminar artefactos maliciosos
3. Parchear vulnerabilidades explotadas
4. Cambiar credenciales comprometidas

### FASE 4: RECUPERACIÓN (4-24 horas)
1. Restaurar desde último backup conocido bueno
2. Verificar integridad de configuraciones
3. Re-habilitar servicios gradualmente
4. Monitoreo intensivo 72 horas

### FASE 5: LECCIONES APRENDIDAS (1-2 semanas)
1. Documentar timeline completo del incidente
2. Identificar gaps en controles de seguridad
3. Actualizar procedimientos y playbooks
4. Entrenamiento del equipo
```

### Checklist de Seguridad Pre-Despliegue

```markdown
## Antes de Usar en Producción

- [ ] Variables de entorno configuradas (no credenciales hardcoded)
- [ ] Archivo .env en .gitignore (nunca commitear secretos)
- [ ] Permisos de archivos configurados (600 para configs, 700 para scripts)
- [ ] SSH keys generadas y distribuidas a administradores
- [ ] Telnet deshabilitado en todos los dispositivos
- [ ] Protocolos inseguros bloqueados (HTTP, FTP, TFTP)
- [ ] Backups automáticos programados y verificados
- [ ] Logs enviándose a SIEM centralizado
- [ ] Alertas de seguridad configuradas en email/Slack/PagerDuty
- [ ] Firewall rules configuradas (permitir solo IPs de gestión)
- [ ] Rate limiting habilitado
- [ ] Prueba de rollback exitosa documentada
- [ ] Plan de respuesta a incidentes revisado por equipo
- [ ] Contactos de emergencia actualizados
- [ ] Ventana de mantenimiento programada y comunicada
```

---

## 🔧 Troubleshooting

### Problemas Comunes y Soluciones

#### Error: "Connection Timeout"

```bash
# Síntoma
ERROR: Timeout connecting to 192.168.1.1:22

# Causas posibles
1. Dispositivo apagado o inaccesible
2. Firewall bloqueando puerto SSH
3. IP incorrecta en configuración

# Solución
# 1. Verificar conectividad
ping 192.168.1.1

# 2. Verificar puerto SSH abierto
nmap -p 22 192.168.1.1

# 3. Verificar credenciales
ssh admin@192.168.1.1

# 4. Aumentar timeout en config.yaml
general:
  timeout: 60  # Aumentar a 60 segundos
```

#### Error: "Authentication Failed"

```bash
# Síntoma
ERROR: Authentication failed for device Core-Switch-01

# Solución
# 1. Verificar variables de entorno
echo $NETWORK_PASSWORD

# 2. Probar credenciales manualmente
ssh admin@192.168.1.1

# 3. Verificar enable secret
# En el dispositivo:
enable
# Debe pedir contraseña del enable secret

# 4. Regenerar hash de credenciales
python network_tool.py config --update-credentials
```

#### Error: "VLAN Already Exists"

```bash
# Síntoma
WARNING: VLAN 10 already exists on Core-Switch-01

# Solución
# 1. Usar flag --force para sobrescribir
python network_tool.py configure --vlan 10 --force

# 2. O eliminar VLAN existente primero
python network_tool.py configure --vlan 10 --action delete
python network_tool.py configure --vlan 10 --action create
```

### Logs de Depuración

```bash
# Habilitar modo debug completo
export LOG_LEVEL=DEBUG
python network_tool.py scan --target 192.168.1.0/24 --verbose

# Ver logs en tiempo real
tail -f /var/log/network_tool/app.log

# Filtrar solo errores
grep ERROR /var/log/network_tool/app.log

# Buscar eventos de un dispositivo específico
grep "Core-Switch-01" /var/log/network_tool/app.log
```

---

## 🤝 Contribución

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit de tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

### Guía de Estilo

- Seguir PEP 8 para código Python
- Documentar todas las funciones con docstrings
- Incluir tests unitarios para nuevas funcionalidades
- Actualizar README.md si es necesario

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver archivo [LICENSE](LICENSE) para más detalles.

---

## 📞 Soporte

- **Email:** support@empresa.com
- **Documentación:** https://docs.network-tool.com
- **Issues:** https://github.com/tu-usuario/network-security-tool/issues
- **Slack:** #network-automation

---

## 🙏 Agradecimientos

- Netmiko community por la excelente librería de automatización
- Cisco DevNet por documentación y recursos
- Todos los contribuidores del proyecto

---

## 📊 Estadísticas del Proyecto

![GitHub stars](https://img.shields.io/github/stars/tu-usuario/network-security-tool)
![GitHub forks](https://img.shields.io/github/forks/tu-usuario/network-security-tool)
![GitHub issues](https://img.shields.io/github/issues/tu-usuario/network-security-tool)
![GitHub pull requests](https://img.shields.io/github/issues-pr/tu-usuario/network-security-tool)

---

<div align="center">

**Desarrollado con ❤️ por el equipo de Network Automation**

[Documentación](https://docs.network-tool.com) | [Changelog](CHANGELOG.md) | [Roadmap](ROADMAP.md)

</div>
