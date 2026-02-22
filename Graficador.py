import serial
import matplotlib.pyplot as plt
from collections import deque

# Cambia el puerto según tu sistema
# Windows: "COM3"
# Mac/Linux: "/dev/tty.usbmodemXXXX"
puerto = "/dev/tty.usbmodem113101"

ser = serial.Serial(puerto, 9600)

plt.ion()  # modo interactivo

datos = deque(maxlen=200)  # guarda últimas 200 mediciones
tiempo = deque(maxlen=200)

contador = 0

while True:
    linea = ser.readline().decode('utf-8').strip()
    
    try:
        temp = float(linea)
        
        datos.append(temp)
        tiempo.append(contador)
        contador += 1
        
        plt.clf()
        plt.plot(tiempo, datos)
        plt.xlabel("Medición")
        plt.ylabel("Temperatura (°C)")
        plt.title("Temperatura en tiempo real")
        plt.pause(0.1)
        
    except:
        pass