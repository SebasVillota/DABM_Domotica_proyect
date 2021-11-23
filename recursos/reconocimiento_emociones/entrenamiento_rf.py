import cv2
import os
import numpy as np
import time

def obtenerModelo(method,facesData,labels):
    if method == 'EigenFaces':emotion_recognizer= cv2.face.EigenFaceRecognizer_create()
    if method == 'FisherFaces':emotion_recognizer= cv2.face.FisherFaceRecognizer_create()
    if method == 'LBPH':emotion_recognizer= cv2.face.LBPHFaceRecognizer_create()
    #Entrenar reconocimiento 
    print('Entrenando('+method+')...')
    inicio = time.time()
    emotion_recognizer.train(facesData, np.array(labels))
    tiemporEntrenamiento = time.time()-inicio
    print('Tiempo de entrenamiento('+method+'); ', tiemporEntrenamiento)

    #Almacenando modelo obtenido
    emotion_recognizer.write('modelo'+method+'.xml')

dataPath= 'C:/Users/sebas/Desktop/Universidad/Decimo Semestre/DABM/PROYECTO_FINAL/recursos/reconocimiento_emociones/Data'
emotionlist = os.listdir(dataPath)
print('Lista de personas: ', emotionlist)

labels = []
facesData = []
label = 0

for nameDir in emotionlist:
    personPath = dataPath + "/" + nameDir
    print('leyendo las imagenes')

    for fileName in os.listdir(personPath):
        #print('Rostros: ', nameDir + '/' + fileName)
        labels.append(label)
        facesData.append(cv2.imread(personPath+ '/'+fileName,0))
        image= cv2.imread(personPath+'/'+fileName,0)
    label = label + 1

#obtenerModelo('EigenFaces',facesData,labels)
obtenerModelo('FisherFaces',facesData,labels)
obtenerModelo('LBPH',facesData,labels)
