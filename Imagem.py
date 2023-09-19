import cv2
import mediapipe as mp
import matplotlib .pyplot as plt

webcam = cv2.VideoCapture(0)
reconhecimento = mp.solutiuons.face_detection
reconhecedor = reconhecimento.FaceDetection()
desenho=mp.solutions.drawing_utils
verificador, frame = webcam.read()
if not verificador:
    lista_rostos= reconhecedor.process(frame)

if lista_rostos.detection:
    for rosto in lista_rostos.detection:
        desenho.draw_detection(frame,rosto)

    if cv2.waitKey(5) == 27:
        cv2.imwrite('.png', frame)
        break

cv2.imshow('Rostos', frame)
webcam.release()
cv2.destroyAllWindows()

#Precisa colocar o endereço da imagem entre parenteses
img= cv2.imread('', cv2.IMREAD_COLOR)
img_rgb= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)



