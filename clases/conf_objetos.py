import serial
import time

class conf_objetos():
    def __init__(self,objeto,estado):
        self.objeto = objeto
        self.estado = estado


def control(objeto,estado,opcion):
    puerto = serial.Serial("COM6",9600)
    puerto.close()
    puerto.open()
    print(objeto)
    print(estado)
    print(opcion)
    
    if(estado == "ON"):
        if(objeto == "cuarto"):
            if(opcion == "prender" or opcion == "prende"):
                print("hola")
                puerto.write("C".encode())
                time.sleep(1)
            if(opcion == "apagar" or opcion == "apaga"):
                puerto.write("c".encode())
                time.sleep(1)
        if(objeto == "cocina"):
            if(opcion == "prender" or opcion == "prende"):
                puerto.write("O".encode())
                time.sleep(1)
            if(opcion == "apagar" or opcion == "apaga"):
                puerto.write("o".encode())
                time.sleep(1)
        if(objeto == "sala"):
            if(opcion == "prender" or opcion == "prende"):
                puerto.write("S".encode())
                time.sleep(1)
            if(opcion == "apagar" or opcion == "apaga"):
                puerto.write("s".encode())
                time.sleep(1)
        if(objeto == "baño"):
            if(opcion == "prender" or opcion == "prende"):
                puerto.write("B".encode())
                time.sleep(1)
            if(opcion == "apagar" or opcion == "apaga"):
                puerto.write("b".encode())
                time.sleep(1)
        if(objeto == "puerta"):
            if(opcion == "abrir" or opcion == "abre"):
                puerto.write("P".encode())
                time.sleep(1)
            if(opcion == "cerrar" or opcion == "cierra"):
                puerto.write("p".encode())
                time.sleep(1)
        if(objeto == "ventilador"):
            if(opcion == "prender" or opcion == "prende"):
                puerto.write("V".encode())
                time.sleep(1)
            if(opcion == "apagar" or opcion == "apaga"):
                puerto.write("v".encode())
                time.sleep(1)
        if(objeto == "seguridad"):
            if(opcion == "abrir" or opcion == "abre"):
                puerto.write("E".encode())
                time.sleep(1)
            if(opcion == "cerrar" or opcion == "cierra"):
                puerto.write("e".encode())
                time.sleep(1)
    elif(estado == "OFF"):
        return("ERROR")
    return("Correct")
    