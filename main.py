from posixpath import split
import speech_recognition as sr
import pyttsx3 
import pandas as pd
import os 
from datetime import datetime
import time
from recursos.funciones import *
import matplotlib.pyplot as plt

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty("rate",125)
name = 'sandra'
listener = sr.Recognizer()



def Emociones():
    print("Registro de Emociones")
    directorio = os.path.dirname(__file__)
    nombreArchivo = "recursos/reconocimiento_emociones/emociones.csv"
    ruta = os.path.join(directorio,nombreArchivo)
    file = open(ruta,"r",encoding='utf-8')
    datos = file.readlines()
    file.close()
    time_feliz = 0
    time_enojo = 0
    time_serio = 0
    time_suenio = 0
    time_triste = 0
    for dato in datos:
        tiempo,emotion = dato.split(";")
        emotion = emotion.strip('\n')
        emotion = emotion.strip('\t')
        if(emotion == "Felicidad"):
            time_feliz = time_feliz + float(tiempo)
        elif(emotion == "Enojo"):
            time_enojo = time_enojo + float(tiempo)
        elif(emotion == "Serio"):
            time_serio = time_serio + float(tiempo)
        elif(emotion == "Dormir"):
            time_suenio = time_suenio + float(tiempo)
        elif(emotion == "Tristeza"):
            time_triste = time_triste + float(tiempo)
    time_feliz=time_feliz/60
    time_enojo=time_enojo/60
    time_serio=time_serio/60
    time_suenio=time_suenio/60
    time_triste=time_triste/60

    #eje_x = ['Feliz','Triste','Durmiendo','Serio','Enojo']
    #eje_y = [time_feliz,time_triste,time_suenio,time_serio,time_enojo]
    #plt.show()

    f=['Feliz',time_feliz]
    t=['Triste',time_triste]
    d=['Durmiendo',time_suenio]
    e=['Enojo',time_enojo]
    s=['Serio',time_serio]
    lista = [f,t,d,e,s]
    listaframe = pd.DataFrame(lista,columns=['Emocion','Tiempo'])
    plt.ylabel('Tiempo de emociones')
    plt.xlabel('Tipo de emoción')
    plt.title('Emociones del paciente en minutos')
    plt.bar(listaframe['Emocion'],listaframe['Tiempo'],color=['b','r','g','m','c'])

    plt.show()
    return
    
    


def talk(text):
    engine.say(text)
    engine.runAndWait()
    

def listen():
    listener = sr.Recognizer()
    rec="NADA"
    with sr.Microphone() as source:
            print("Escuchando...")
            listener.pause_threshold=0.5
            #listener.adjust_for_ambient_noise(source,duration=1)
            voice = listener.listen(source)
            try:
                rec = listener.recognize_google(voice,language="es-CO")  
                rec = rec.lower()
                if name in rec:
                    talk(rec)
            except:
                print("Error")
    return rec


def Control_Hogar():
    print("Control de hogar por ARDUINO")

def act_des_fun(state,datos,name):
    cont =0
    if('prender' in state or 'prende' in state):
        for dato in datos:     
            objeto, estado= dato.split(";")
            estado = estado.strip("\n")
            estado = estado.strip("\t")
            if(name == objeto):
                datos[cont] = name+";ON\n"
            cont = cont+1
    cont = 0
    if('apagar' in state or 'apaga' in state):
        for dato in datos:
            objeto, estado= dato.split(";")
            estado = estado.strip("\n")
            estado = estado.strip("\t")
            if(name == objeto):
                datos[cont] = name+";OFF\n"
            cont = cont+1
    return datos

def Config_Hogar():
    print("Configuraciones")
    directorio = os.path.dirname(__file__)
    nombreArchivo = "archivos/config_objetos.csv"
    ruta = os.path.join(directorio,nombreArchivo)
    file = open(ruta,"r",encoding='utf-8')
    datos = file.readlines()
    file.close()

    talk("Bienvenido al menú de configuración de dispositivos")
    talk("Que desea modificar ")
    objeto = listen()
    if('cuarto' in objeto):
        talk("Desea prender o apagar la función")
        state = listen()
        datos = act_des_fun(state,datos,"luz cuarto")
    elif('cocina' in objeto):
        talk("Desea prender o apagar la función")
        state = listen()
        datos = act_des_fun(state,datos,"luz cocina")
    elif('sala' in objeto):
        talk("Desea prender o apagar la función")
        state = listen()
        datos = act_des_fun(state,datos,"luz sala")
    elif('baño' in objeto):
        talk("Desea prender o apagar la función")
        state = listen()
        datos = act_des_fun(state,datos,"luz baño")
    elif('puerta' in objeto):
        talk("Desea prender o apagar la función")
        state = listen()
        datos = act_des_fun(state,datos,"puerta")
    elif('ventilador' in objeto):
        talk("Desea prender o apagar la función")
        state = listen()
        datos = act_des_fun(state,datos,"ventilador")
    elif('seguridad' in objeto):
        talk("Desea prender o apagar la función")
        state = listen()
        datos = act_des_fun(state,datos,"seguridad")
            
    archivo = open(ruta,"w",encoding='utf-8')
    for l in datos:
        archivo.write(l)
    archivo.close()
    talk("Desea hacer otro cambio")
    des = listen()
    if(des in "si" or des in "sí"):
        Config_Hogar()
    else:
        return
        


def Registro_Usuarios():

    directorio = os.path.dirname(__file__)
    nombreArchivo = "archivos/Datos.csv"
    ruta = os.path.join(directorio,nombreArchivo)
    file = open(ruta,"r",encoding='utf-8')
    datos = file.readlines()
    file.close()


    print("Registro de Usuarios")
    talk("Desea Registrar un usuario nuevo")
    new = listen()
    print(new)
    if('si' in new or 'sí' in new):
        talk("Diga su usuario")
        user = listen()
        while(user == 'NADA' or user == ''):
            talk("Error por favor ingrese de nuevo")
            user = listen()
        talk("Diga su contraseña")
        password = listen()
        while(password == 'NADA' or password == ''):
            talk("Error por favor ingrese de nuevo")
            password = listen()
        
        for dato in datos:
            User_t, password_t = dato.split(";") 
            if(User_t == user):
                print("ERROR! usuario repetido")
                print("Desea salir o continuar?")
                cont = listen()
                if('continuar' in cont):
                    Registro_Usuarios()
                else:
                    return
        new_date = user + ";" + password + "\n"
        datos.append(new_date)
        print(datos)
        archivo = open(ruta,"w",encoding='utf-8')
        for l in datos:
            archivo.write(l)
        archivo.close()
        return



def espera_asistente():
    print("Esperando que me llames")
    rec = listen()
    if(rec in 'sandra'):
        return
    else:
        espera_asistente()

def espera_asistente_menu():
    print("Que opción desea: ")
    rec = listen()
    if('sandra' in rec):
        return
    else:
        espera_asistente_menu()

def Menu_principal():
    
    print("*"*60)
    print("ENTRASTE AL MENU PRINCIPAL".center(50," "))
    print("*"*60)
    print("1. CONTROL DEL HOGAR".center(50," "))
    print("2. Configuración de Control".center(50," "))
    print("3. Registro de usuarios".center(50," "))
    print("4. Emociones".center(50," "))
    print("5. Salir".center(50," "))
    espera_asistente_menu()
    talk("Que opción desea ingresar")
    a= listen()
    if('1' in a):
        op="1"
    elif('2' in a):
        op="2"
    elif('3' in a):
        op="3"
    elif('4' in a):
        op="4"
    elif('5' in a):
        op="5"
    else:
        op=''

    if(op == "1"):
        Control_Hogar()
        input("Salir(Enter)")
    elif(op == "2"):
        Config_Hogar()
    elif(op == "3"):
        Registro_Usuarios()
        input("Salir(Enter)")
    elif(op == "4"):
        Emociones()
        input("Salir(Enter)")
    elif(op == "5"):
        time.sleep(3)
        run()    
    else:
        print("Opción NO valida")
        Menu_principal()
    Menu_principal()

def error_usuario():
    print("Error al decir usuario o contraseña, Intenta de nuevo")
    run()

def comprueba_Contrasena(pasword_t, User_t):
    pasword_t = pasword_t.strip('\n')
    pasword_t = pasword_t.strip('\t')
    print(pasword_t)
    password = listen()
    print(password)
    if(pasword_t == password):
        talk("Bienvenido "  + User_t + " has entrado al menú")
        Menu_principal()
    error_usuario()


def comprueba_usuario(usuario):
    talk(usuario)
    print(usuario)

    directorio = os.path.dirname(__file__)
    nombreArchivo = "archivos/Datos.csv"
    ruta = os.path.join(directorio,nombreArchivo)
    file = open(ruta,"r",encoding='utf-8')
    datos = file.readlines()
    file.close()
    print(datos)
    cont=0
    for dato in datos:
        User_t, password_t = dato.split(";")
        if (User_t == usuario):
            talk("usuario correcto, diga su contraseña")
            comprueba_Contrasena(password_t, User_t)
        cont = cont + 1
    error_usuario()



def run():
    talk("Hola Usuario Bienvenido al Login")
    espera_asistente()
    talk('Que desea ingresar?')
    rec = listen()
    print (rec)
    if 'usuario' in rec:
        talk("Ingrese su usuario")
        usuario=""
        usuario = listen()
        comprueba_usuario(usuario)
    print("No habla")
    run()


if __name__ == "__main__":
    run()
    