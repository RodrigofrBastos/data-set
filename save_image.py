import cv2
import os
import datetime as dt
# Open the default camera
cap = cv2.VideoCapture(0)

# Read a single frame from the camera
ret, frame = cap.read()
cap.release()

#armazena o horario e data da foto retirada
data = dt.datetime.now()
data_string = data.strftime("%A %d %B %y %I:%M")
data_datetime = dt.datetime.strptime(data_string,"%A %d %B %y %I:%M")

# escrevendo a data-horario na imagem
cv2.putText(frame,"{}".format(data_datetime),(10,30),cv2.FONT_HERSHEY_PLAIN,1,(255))


# Nome do arquivo
filename = "img/image.jpg"

# Se o arquivo já existe, adicione um número sequencial ao nome
if os.path.exists(filename):
    index = 1
    while os.path.exists(f"{os.path.splitext(filename)[0]}-{index}{os.path.splitext(filename)[1]}"):
        index += 1
    filename = f"{os.path.splitext(filename)[0]}-{index}{os.path.splitext(filename)[1]}"




# Agora, filename contém um nome de arquivo exclusivo
cv2.imwrite('{}'.format(filename), frame)
print(filename)
