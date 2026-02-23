# Proyecto de Termodinámica – Sistema de Medición de Temperatura

## Profesor: Yonathan Armando Loredo Sáenz

| ID                 | Name                               |
| ------------------ | -----------------------------------| 
|  A00843568         | Leonardo Sánchez Alegre            |
|  A00845424         | Axel Daniel Vázquez Montoya        |
|  A00845476         |	Jesús Rojas Martínez              |
|  A00845929         |  Luis Diego Chapa Santos           |
|  A00845553         |  Marco Alejandro Galindo de la Cruz| 

Este proyecto contiene el sistema de medición y registro de temperatura utilizado en nuestro experimento de hielera.

Incluye:

- Código para Arduino (lectura del sensor)
- Script en Python para graficar en tiempo real
- Exportación automática de datos a CSV

---

##  Hardware utilizado

- Arduino Uno (o compatible)
- Sensor DS18B20 impermeable
- Resistencia 4.7kΩ – 5kΩ (pull-up)

---

#  Estructura del Proyecto

Termodinamica /
│
├── src/
│   └── main.cpp        # Código del Arduino
│
├── Graficador.py       # Script para graficar en tiempo real
│
└── README.md

El archivo `main.cpp` dentro de la carpeta `src` contiene el código que debe cargarse al Arduino.

---

# Cómo usar el proyecto

## 1️⃣ Cargar el código al Arduino

1. Abre el archivo `src/main.cpp`.
2. Compílalo y súbelo a tu Arduino.
3. Verifica que el monitor serial esté en **9600 baudios**.

El Arduino enviará la temperatura cada 5 minutos por el puerto serial.

---

## 2️⃣ Configurar el entorno de Python (recomendado usar entorno virtual)

Desde la carpeta del proyecto:

python3 -m venv venv
source venv/bin/activate
pip install pyserial matplotlib

---

## 3️⃣ Configurar el puerto serial

Edita el archivo `Graficador.py` y cambia esta línea según tu sistema:

puerto = "/dev/tty.usbmodemXXXX"

Puertos comunes:

Windows:
puerto = "COM3"

Mac/Linux:
puerto = "/dev/tty.usbmodemXXXX"

Para ver tu puerto en Mac/Linux:

ls /dev/tty.*

---

## 4️⃣ Ejecutar el graficador

Con el entorno virtual activado:

python Graficador.py

El sistema:

- Escucha continuamente los datos del Arduino  
- Grafica la temperatura en tiempo real  
- Guarda automáticamente las mediciones en un archivo CSV  
- Registra datos durante 12 horas (144 mediciones)

---

# Salida del sistema

Al finalizar se genera:

- Un archivo CSV con las temperaturas registradas
- La gráfica completa del comportamiento térmico

---

# Objetivo del proyecto

Analizar el comportamiento térmico de una hielera a lo largo del tiempo, aplicando conceptos de:

- Transferencia de calor
- Aislamiento térmico
- Modelos de enfriamiento
