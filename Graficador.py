import serial
import matplotlib.pyplot as plt
from collections import deque
import time

# Cambia el puerto según tu sistema
# Windows: "COM3"
# Mac/Linux: "/dev/tty.usbmodemXXXX"
puerto = "/dev/tty.usbmodem113101"

def conectar_serial(puerto, baudrate=9600, timeout=2):
    while True:
        try:
            ser = serial.Serial(puerto, baudrate, timeout=timeout)
            print(f"Conectado a {puerto}")
            return ser
        except serial.SerialException as e:
            print(f"No se pudo conectar a {puerto}: {e}")
            print("Reintentando en 5 segundos...")
            time.sleep(5)

plt.ion()  # modo interactivo

datos = deque(maxlen=200)  # guarda últimas 200 mediciones
tiempo = deque(maxlen=200)

contador = 0

ser = conectar_serial(puerto)

print("\nMedición\tTemperatura (°C)")
while True:
    try:
        linea = ser.readline().decode('utf-8').strip()
        if not linea:
            continue
        temp = float(linea)
        datos.append(temp)
        tiempo.append(contador)
        # Imprimir en formato tabla
        print(f"{contador}\t{temp}")
        contador += 1
        plt.clf()
        plt.plot(tiempo, datos)
        plt.xlabel("Medición")
        plt.ylabel("Temperatura (°C)")
        plt.title("Temperatura en tiempo real")
        plt.pause(0.1)
    except serial.SerialException as e:
        print(f"Error de conexión: {e}")
        print("Intentando reconectar...")
        ser.close()
        ser = conectar_serial(puerto)
    except ValueError:
        # Línea recibida no es un número
        continue
    except Exception as e:
        print(f"Error inesperado: {e}")
        time.sleep(1)