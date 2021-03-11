import serial
port = serial.Serial('COM3',9600)
while (port.isOpen()):
    data = port.readline()
    print(data)