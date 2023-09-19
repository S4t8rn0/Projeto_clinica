import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
import numpy

webcam = cv2.VideoCapture(0)
reconhecimento = mp.solutions.face_detection
desenho=mp.solutions.drawing_utils
reconhecedor = reconhecimento.FaceDetection()


while webcam.isOpened():
    verificador, frame = webcam.read()
    lista_rostos= reconhecedor.process(frame)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            desenho.draw_detection(frame, rosto)

    cv2.imshow('Video', frame)

    if cv2.waitKey(5) == ord('q'):
        cv2.imwrite('OK.png', frame)
    if cv2.waitKey(0)== 27:
        break


if not verificador:
    print('ok')
    

webcam.release()
cv2.destroyAllWindows()

#Precisa colocar o endereço da imagem entre parenteses
img= cv2.imread('OK.png', cv2.IMREAD_COLOR)
img_rgb= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
