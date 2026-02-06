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

---

## 🎯 Objetivo 

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
---
-Archivo de configuración del DNS Spoofing

 <img width="672" height="160" alt="image" src="https://github.com/user-attachments/assets/2c0a73d3-dfde-465a-80b9-00b77d9392f6" />
 
---
 -Tráfico DNS interceptado
 
 - <img width="599" height="209" alt="image" src="https://github.com/user-attachments/assets/389a0665-f352-4451-90bd-3edfb956e11c" /> 
---
- Redirección exitosa al sitio web falso
 <img width="943" height="331" alt="image" src="https://github.com/user-attachments/assets/3b9a2936-b3b6-4118-967b-917abb1327ce" />

---
### Reporte de Seguridad
Durante la ejecución del laboratorio se identificó que la red evaluada carece de mecanismos básicos de protección, lo que permitió la ejecución exitosa de ataques de ARP Spoofing y DNS Spoofing. La ausencia de segmentación, validación ARP y controles de integridad DNS representa un riesgo significativo para la confidencialidad e integridad de la información.

El impacto principal del ataque es la posibilidad de interceptar tráfico, redirigir a usuarios hacia sitios falsos y capturar información sensible. En un entorno real, este tipo de vulnerabilidad podría facilitar robo de credenciales, suplantación de identidad y propagación de malware.

La implementación de controles como Dynamic ARP Inspection, segmentación por VLAN, DNS seguro y monitoreo activo permitiría reducir considerablemente la superficie de ataque.

<img width="800" height="480" alt="image" src="https://github.com/user-attachments/assets/8d4047ce-06be-4be3-b6fd-9cc79531011f" />
## 🔐 Evaluación de Seguridad




```


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

```

# Tabla de Interfaces
# Direccionamiento Router R-SD (Santo Domingo)

| Interfaz | VLAN | Dirección IP | Máscara | Descripción |
|----------|------|--------------|---------|-------------|
| e0/0 | — | IP pública | — | Enlace público |
| e0/2 | — | 10.0.0.1 | 255.255.255.252 | Enlace P2P hacia R-STG |
| e0/1.10 | VLAN 10 | 15.0.7.1 | 255.255.255.0 | Red Víctima (Gateway) |
| e0/1.888 | VLAN 888 | — | — | VLAN nativa |

### SW-SD
| Interface | Tipo | Modo  | VLANs   | Descripción |
|-----------|------|-------|---------|-------------|
| 0/1-2     | Eth0 | Acess |   10    |   VIctima   |
|  0/3      | Eth0 | trunk |   888   |    Nativa   |
|  0/0      | Eth0 | Trunk |   888   |    Nativa   |
----------------------------------------------------

## Direccionamiento Router R-STG (Santiago)
### Router
| Interfaz | VLAN/Lan | Dirección IP | Máscara | Descripción |
|----------|------|--------------|---------|-------------|
| e0/0 | Lan| IP pública | — | Enlace público |
| e0/2 | Lan | 10.0.0.2 | 255.255.255.252 | Enlace P2P hacia R-SD |
| e0/1.50 | VLAN 50 | 15.0.8.1 | 255.255.255.0 | Red TI (Gateway) |
| e0/1.888 | VLAN 888 | — | — | VLAN nativa |

### SW-STG
| Interface | Tipo | Modo  | VLANs   | Descripción |
|-----------|------|-------|---------|-------------|
| 0/1-2     | Eth0 | Acess |    50   |     TI      |
|  0/3      | Eth0 | trunk |    888  |     Nativa  |
----------------------------------------------------

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


```


### Ejemplos de Uso


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
| Cisco | Catalyst 3560| IOS 15.0+ | ✅ Completo       |
--------------------------------------------------------

#### Routers

| Fabricante | Modelos Soportados | Versión OS | Estado |
|------------|-------------------|------------|--------|
| Cisco | 2960         | ISO 15.0+ |✅ Completo |
-------------------------------------------------------

### Conectividad Requerida

- ✅ Acceso SSH (puerto 22) a dispositivos de red
- ✅ Acceso a Internet (para actualizaciones y descargas)
- ⚠️ Acceso Telnet (puerto 23) - **NO RECOMENDADO** Solo para prueba


---

## 🚀 Modo de Uso 
  
Para su ejecución, basta con ejecutarlo utilizando Python3 con privilegios de superusuario.

```bash
sudo python3 ARP.py


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

# 🛡️ Medidas de Mitigación

## Análisis de Riesgos y Controles - ARP Spoofing y DNS Spoofing

| ID | Riesgo Identificado | Severidad | Probabilidad | Impacto | Medida de Mitigación Implementada |
|----|---------------------|-----------|--------------|---------|-----------------------------------|
| R-001 | ARP Spoofing - Envenenamiento de tabla ARP | CRÍTICO | Alta | Crítico | • Implementación de DAI (Dynamic ARP Inspection)<br>• ARP estáticas para dispositivos críticos<br>• Monitoreo continuo de tabla ARP<br>• Port Security en switches<br>• Alertas ante cambios anómalos de MAC |
| R-002 | DNS Spoofing - Redirección de tráfico | CRÍTICO | Alta | Crítico | • Implementación de DNSSEC<br>• Servidores DNS confiables y validados<br>• Filtrado de respuestas DNS no solicitadas<br>• Monitoreo de consultas DNS sospechosas<br>• ACLs restrictivas en routers |
| R-003 | Man-in-the-Middle (MitM) | CRÍTICO | Alta | Crítico | • Uso obligatorio de HTTPS/TLS<br>• Validación de certificados SSL/TLS<br>• Implementación de HSTS<br>• VPN para tráfico sensible<br>• Detección de ataques MitM con IDS/IPS |
| R-004 | Acceso no autorizado a dispositivos de red | ALTO | Media | Alto | • Autenticación SSH con claves públicas<br>• Implementación de 2FA en acceso administrativo<br>• Logging de todos los intentos de acceso<br>• Rate limiting: máx 3 intentos/minuto<br>• Deshabilitar Telnet, usar solo SSH |
| R-005 | Propagación de ataques en la red | ALTO | Alta | Alto | • Segmentación de VLANs<br>• ACLs entre VLANs<br>• Private VLANs donde sea aplicable<br>• Firewall interno entre segmentos<br>• Monitoreo de tráfico anómalo |
| R-006 | Credenciales comprometidas | ALTO | Media | Crítico | • Uso de variables de entorno<br>• Encriptación AES-256 de credenciales<br>• Rotación periódica de contraseñas<br>• Integración con HashiCorp Vault<br>• Nunca almacenar credenciales en texto plano |
| R-007 | Falta de detección de ataques | ALTO | Alta | Alto | • Implementación de IDS/IPS (Snort, Suricata)<br>• SIEM para correlación de eventos<br>• Alertas en tiempo real<br>• Análisis de logs centralizados<br>• Monitoreo 24/7 |
| R-008 | Modificación no autorizada de configuraciones | MEDIO | Media | Alto | • Control de versiones (Git) para configs<br>• Backup automático pre-cambio<br>• Rollback automático en caso de fallo<br>• Auditoría de cambios con firma digital<br>• Modo dry-run obligatorio |

## Controles Específicos por Ataque

### ARP Spoofing
- **(Dynamic ARP Inspection):** Validación de paquetes ARP contra DHCP Snooping
- **IP Source Guard:** Previene spoofing de direcciones IP
- **DHCP Snooping:** Base de datos confiable de asignaciones IP-MAC
- **Port Security:** Limita MACs permitidas por puerto

### DNS Spoofing
- **DNSSEC:** Validación criptográfica de respuestas DNS
- **DNS sobre HTTPS (DoH) / DNS sobre TLS (DoT):** Encriptación de consultas
- **Cache Poisoning Protection:** Validación de respuestas DNS
- **Servidores DNS recursivos seguros:** Google DNS (8.8.8.8) o Cloudflare (1.1.1.1)

## Monitoreo y Detección

| Herramienta | Propósito | Implementación |
|-------------|-----------|----------------|
| Wireshark/tcpdump | Análisis de tráfico | Captura y análisis de paquetes sospechosos |
| arpwatch | Monitoreo ARP | Alertas de cambios en tabla ARP |
| Snort/Suricata | IDS/IPS | Detección de patrones de ataque |
| Syslog | Logging centralizado | Recolección de logs de todos los dispositivos |
| SIEM | Correlación de eventos | Análisis y alertas de seguridad |


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



---

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
