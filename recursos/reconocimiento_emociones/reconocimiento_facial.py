import cv2
import os
import numpy as np
import time

def reconocimiento_Emociones():
    directorio = os.path.dirname(__file__)
    nombreArchivo = "Data"
    dataPath = os.path.join(directorio,nombreArchivo)

    nombreArchivo = "emociones.csv"
    ruta = os.path.join(directorio,nombreArchivo)

    imagePaths = os.listdir(dataPath)
    print('imagePaths=', imagePaths)

    #------Metodo usado para reconocimiento------
    #method = 'EigenFaces'
    #method = 'FisherFaces'
    method = 'LBPH'

    if method == 'EigenFaces':emotion_recognizer= cv2.face.EigenFaceRecognizer_create()
    if method == 'FisherFaces':emotion_recognizer= cv2.face.FisherFaceRecognizer_create()
    if method == 'LBPH':emotion_recognizer= cv2.face.LBPHFaceRecognizer_create()

    #-----Leer Modelo-------
    emotion_recognizer.read('modelo'+method+'.xml')  
    #-----------------------------------------------
    tiempo_feli = 0
    tiempo_sad = 0
    tiempo_serio = 0
    tiempo_sleep = 0
    tiempo_enojado = 0
    tiempototal = 0
    #Lecura del modelo
    #face_recognizer.read('C:/Users/sebas/Desktop/Universidad/Decimo Semestre/DABM/PROYECTO_FINAL/Database/modeloEigenFace.xml')

    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        if ret== False: break
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()

        inicio = time.time()
        faces = faceClassif.detectMultiScale(gray, 1.3, 5)
        for(x,y,w,h) in faces:
            rostro = auxFrame[y:y+h, x:x+w]
            rostro = cv2.resize(rostro,(150,150), interpolation = cv2.INTER_CUBIC)
            result = emotion_recognizer.predict(rostro)

            cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
            
            if method == 'EigenFaces':
                #EIGEN
                if result[1] < 5700:
                    cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                else:
                    cv2.putText(frame,'Desonocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            if method == 'FisherFaces':
                #FISHER
                if result[1] < 500:
                    cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                    print(format(imagePaths[result[0]]))
                else:
                    cv2.putText(frame,'Desonocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            if method == 'LBPH':
                #LBPH
                if result[1] < 70:
                    cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                    print(format(imagePaths[result[0]]))
                    emocion = format(imagePaths[result[0]])
                    tiempoPrograma = time.time()-inicio
                    tiempototal = tiempototal + tiempoPrograma
                    if(emocion == 'Felicidad'):
                        tiempo_feli = tiempo_feli + tiempoPrograma
                    if(emocion == 'Enojo'):
                        tiempo_enojado = tiempo_enojado + tiempoPrograma
                    if(emocion == 'Serio'):
                        tiempo_serio = tiempo_serio + tiempoPrograma
                    if(emocion == 'Tristeza'):
                        tiempo_sad = tiempo_sad + tiempoPrograma
                    if(emocion == 'Suenio'):
                        tiempo_sleep = tiempo_sleep + tiempoPrograma
                    inicio = time.time()
                    if(tiempototal > 60):
                        file = open(ruta,"r",encoding='utf-8')
                        datos = file.readlines()
                        file.close()

                        date_feliz = str(tiempo_feli)  + ";" + "Felicidad" + "\n"    
                        datos.append(date_feliz)
                        date_enojado = str(tiempo_enojado)  + ";" + "Enojo" + "\n"    
                        datos.append(date_enojado)
                        date_sad = str(tiempo_sad)  + ";" + "Tristeza" + "\n"    
                        datos.append(date_sad)
                        date_serio = str(tiempo_serio)  + ";" + "Serio" + "\n"    
                        datos.append(date_serio)
                        date_sleep = str(tiempo_sleep)  + ";" + "Dormir" + "\n"    
                        datos.append(date_sleep)

                        archivo = open(ruta,"w",encoding='utf-8')
                        for l in datos:
                            archivo.write(l)
                        archivo.close()
                        print(tiempoPrograma)                    
                        tiempototal = 0
                        tiempo_feli = 0
                        tiempo_sad = 0
                        tiempo_serio = 0
                        tiempo_sleep= 0
                        tiempo_enojado = 0
                    
                else:
                    cv2.putText(frame,'Desonocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            
        
        
        cv2.imshow('frame',frame)
        k= cv2.waitKey(1)
        if k == 32:
            break

    cap.release()
    cv2.destroyAllWindows()

reconocimiento_Emociones()