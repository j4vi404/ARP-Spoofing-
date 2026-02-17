# ARP & DNS Spoofing
# 🔧 Network Security Tool

<div align="center">

![Python](https://img.shields.io/badge/python-3.8+-yellow.svg)

*Herramienta automatizada para configuración, auditoría y seguridad de infraestructura de red*

</div>

---
Demostración del ataque 
https://youtu.be/OqYd2B7tEYM
---

## 📋 Tabla de Contenidos

- [Objetivo del Script](#-objetivo-del-script)
- [Características Principales](#-características-principales)
- [Capturas de Pantalla](#-capturas-de-pantalla)
- [Topología de Red](#-topología-de-red)
- [Parámetros de Configuración](#-parámetros-de-configuración)
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
# ARP Spoofing - Man in the Middle Attack

Script de Python que utiliza Scapy para realizar ataques ARP Spoofing (MITM) interceptando tráfico entre una víctima y el router.

## Requisitos
```bash
pip install scapy
```

## Uso
```bash
git clone https://github.com/j4vi404/ARP-Spoofing-.git
cd /ARP-Spoofing-
chmod +x ARP-Spoofing-
sudo python3 ARP.py
```
## Características

- 🎯 **ARP Spoofing (MITM)**: Intercepta tráfico entre víctima y router
- 🔄 **Envenenamiento bidireccional**: Envenena tanto a la víctima como al router
- ⚡ **IP Forwarding automático**: Habilita reenvío de paquetes
- ✅ **Restauración automática**: Restaura tablas ARP al detener (Ctrl+C)
- ✅ **Limpieza segura**: Deshabilita IP forwarding al finalizar
- 📊 **Mensajes informativos**: Indica estado de cada fase
- 🔧 **Configuración simple**: Variables fáciles de modificar

## Configuración

Edita las siguientes variables según tu red:
```python
victima_ip = "15.0.7.3"     # IP de la víctima
router_ip = "15.0.7.1"      # IP del gateway/router
interface = "eth0"           # Interfaz de red
```

## Notas

⚠️ **Advertencia**: Este script requiere privilegios de root para manipular tablas ARP.

⚠️ **Uso responsable**: Utiliza este script únicamente en entornos de prueba autorizados y con fines educativos.

⚠️ **Legal**: El uso no autorizado de este script puede ser ilegal. Asegúrate de tener permiso explícito.

## Cómo funciona

1. **Habilita IP Forwarding**: Permite que los paquetes pasen a través de tu máquina
2. **Envenena ARP**: Envía paquetes ARP falsos a la víctima y al router
3. **Intercepta tráfico**: Todo el tráfico pasa por tu máquina
4. **Restaura al salir**: Limpia las tablas ARP y deshabilita forwarding

## Detección

Este ataque puede ser detectado mediante:
- Monitoreo de tablas ARP
- Detección de MAC duplicadas
- IDS/IPS configurados

## Autor

**MR.J4VI MINYETE**






---
### Reporte de Seguridad
Durante la ejecución del laboratorio se identificó que la red evaluada carece de mecanismos básicos de protección, lo que permitió la ejecución exitosa de ataques de ARP Spoofing y DNS Spoofing. La ausencia de segmentación, validación ARP y controles de integridad DNS representa un riesgo significativo para la confidencialidad e integridad de la información.

El impacto principal del ataque es la posibilidad de interceptar tráfico, redirigir a usuarios hacia sitios falsos y capturar información sensible. En un entorno real, este tipo de vulnerabilidad podría facilitar robo de credenciales, suplantación de identidad y propagación de malware.

La implementación de controles como Dynamic ARP Inspection, segmentación por VLAN, DNS seguro y monitoreo activo permitiría reducir considerablemente la superficie de ataque.

<img width="800" height="480" alt="image" src="https://github.com/user-attachments/assets/8d4047ce-06be-4be3-b6fd-9cc79531011f" />

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
# Parámetros Usados

## Configuración de Red

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| **Red Víctima** | 15.0.7.0/24 | VLAN 10 - Segmento de red objetivo |
| **Red TI** | 15.0.8.0/24 | VLAN 50 - Segmento administrativo |
| **Enlace P2P** | 10.0.0.0/30 | Conexión entre R-SD y R-STG |
| **VLAN Nativa** | 888 | VLAN para tráfico no etiquetado |

## Parámetros de Ataque

### ARP Spoofing
| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| **IP Objetivo (Víctima)** | 15.0.7.10 | Host a interceptar |
| **IP Gateway** | 15.0.7.1 | Router/Gateway de la red |
| **MAC Atacante** | Variable | MAC del equipo atacante |
| **Intervalo de envío** | 2 segundos | Frecuencia de paquetes ARP falsos |
| **Modo** | Bidireccional | Envenenamiento víctima ↔ gateway |

### DNS Spoofing
| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| **Dominio falso** | rondom.git.com | Dominio a suplantar |
| **IP falsa** | 15.0.7.4 | IP del servidor malicioso |
| **Puerto DNS** | 53 | Puerto estándar DNS |
| **Protocolo** | UDP | Protocolo de transporte |
-------------------------------------------------
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

```

---

## 🛡️ Medidas de Mitigación

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

<div align="center">

**Practica 3 Seguridad de Redes**


</div>
