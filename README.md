# 🟣 Guardian-Engine: Ultra Ego SIEM Core
![Ultra Ego](https://img.shields.io/badge/Mode-Ultra_Ego-blueviolet?style=for-the-badge&logo=dragonball)
![Python](https://img.shields.io/badge/Power-Python_3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Status-Active_Defense-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Instinct-Ultra_Ego-blueviolet)
![Type](https://img.shields.io/badge/SIEM-Event--Driven-red)

> **"Un verdadero guerrero no busca evitar el golpe, lo utiliza para aplastar a su enemigo."**

## 🛡️ Descripción del Proyecto
**Guardian-Engine** es un motor de procesamiento de eventos de seguridad (SIEM) de alto rendimiento desarrollado en **Python**. Diseñado bajo una arquitectura **Event-Driven**, este sistema actúa como el núcleo central de defensa, absorbiendo y monitoreando logs en tiempo real para detectar, analizar y registrar amenazas con la ferocidad del **Ultra Ego**.

Mientras otros sistemas se saturan, Guardian-Engine utiliza cada intento de intrusión para fortalecer el registro de seguridad, transformando el caos de la red en control total. 

![Tests Status](https://github.com/yfajardomoya11/guardian-engine/actions/workflows/python-tests.yml/badge.svg)
# 🛡️ Guardian-Engine v1.0
**Real-Time Security Orchestration & Network Monitoring Engine**

[![Python Version](https://img.shields.io/badge/python-3.14-blue.svg)](https://www.python.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Identity](https://img.shields.io/badge/Branding-The--Network--Guardian-red)](https://github.com/tu-usuario)
 
![Logo de Guardian Engine](https://github.com/yfajardomoya11/Guardian-Engine/blob/main/assets/SIEM-1.png)
## 👤 Autor
**Yananth Fajardo Moya** *Técnico Infraestructura de Redes y Desarrollador de Herramientas de Ciberseguridad**

---

## ⚠️ PRO PROFESSIONAL DISCLAIMER / DESCARGO DE RESPONSABILIDAD
> **Este proyecto fue desarrollado con fines exclusivamente educativos y de aprendizaje.** > 
> Guardian-Engine es una prueba de concepto (PoC) diseñada para demostrar habilidades en programación con Python, automatización de eventos y manejo de bases de datos. No debe ser utilizado como única medida de defensa en entornos de producción críticos sin previa auditoría y endurecimiento (hardening) profesional. 
> 
> El uso de este software para el monitoreo de redes debe realizarse siempre bajo el marco de la legalidad y con el consentimiento explícito de los propietarios de la infraestructura. El autor no se hace responsable por el mal uso de esta herramienta.

---

## 📖 Descripción
**Guardian-Engine** es un motor de procesamiento de eventos de seguridad desarrollado en Python. Diseñado bajo una arquitectura **Event-Driven**, este sistema actúa como el núcleo central de defensa, monitoreando logs en tiempo real para detectar, analizar y registrar amenazas en la infraestructura de red.

Este proyecto es la pieza central del ecosistema de herramientas creadas por mí, en mi transicion hacia la ciberseguridad


## 📸 Evidencia )de Funcionamiento (PoC)
<p align="center">
  <img src="assets/PRUEBASIEM1.png" alt="Guardian-Engine Demo" width="800">
  <br>
  <i>Captura del motor detectando y registrando alertas en tiempo real.</i>
</p>

## 🚀 Características Principales
* **Monitoreo en Tiempo Real:** Utiliza la librería `watchdog` para detectar cambios en los logs en milisegundos mediante señales del Sistema Operativo.
* **Análisis de Hilos de Log:** Algoritmo capaz de escanear y procesar múltiples líneas de forma secuencial, clasificando eventos en `INFO`, `WARNING` y `CRITICAL`.
* **Persistencia Forense:** Integración con **SQLite** para el almacenamiento estructurado de alertas, garantizando que el historial de eventos sea persistente y auditable.
* **Seguridad por Diseño:** Implementación de variables de entorno (`.env`) para proteger rutas de archivos y configuraciones sensibles del sistema.

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.14
* **Base de Datos:** SQLite3
* **Librerías Clave:** `watchdog`, `python-dotenv`, `pandas`
* **Arquitectura:** Orientada a Eventos (Event-Driven)

## 📂 Estructura del Proyecto
```text
GUARDIAN-ENGINE/
├── main.py              # Orquestador principal del motor
├── .env                 # Configuración de entorno (Excluido de Git)
├── database/            # Capa de datos y gestión de SQLite
│   ├── db_manager.py    # Lógica de escritura y lectura en DB
│   └── logs.db          # Base de datos local
├── processor/           # Lógica de análisis y clasificación de logs
└── alerts.log           # Canal de entrada de eventos monitoreados  


> ### 🟣 **LA DOCTRINA DEL ULTRA EGO EN LA RED**
> "No esperen un simple registro de eventos; esto es la **Doctrina del Ultra Ego** aplicada a la red. Mi motor de eventos no esquiva la tormenta, se sitúa en el centro de ella para absorber su fuerza. Cada intento de vulneración es desintegrado y reconstruido como un pilar de conocimiento. ¡En mi arquitectura, el ataque enemigo es la oración que invoca mi evolución!" ⚡🟣

---
> **Disclaimer:** Visual identity inspired by the concept of resilience; character art is a fan-tribute to its respective creators.