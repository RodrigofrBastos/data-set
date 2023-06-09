import cv2
import os
import datetime as dt

def switch_case(key):
    switch_dict = {
        'l': "PVC-leak/leak.jpg",
        'n': "PVC-noleak/no_leak.jpg",
    }
    return switch_dict.get(key, None)

# Open the default camera
cap = cv2.VideoCapture(2)
# Read frames from the camera
while(True):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)
# pressione a tecla "l" para tirar uma foto do vazamento ou "n" para sem vazamento
    key = chr(cv2.waitKey(1) & 0xFF)
    filename = switch_case(key)
    if filename:
        break



cap.release()
cv2.destroyAllWindows()

#armazena o horario e data da foto retirada
data = dt.datetime.now()
data_string = data.strftime("%A %d %B %y %I:%M")
data_datetime = dt.datetime.strptime(data_string,"%A %d %B %y %I:%M")

# escrevendo a data-horario na imagem
cv2.putText(frame,"{}".format   (data_datetime),(10,30),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0))

# Se o arquivo já existe, adicione um número sequencial ao nome
if os.path.exists(filename):
    index = 1
    while os.path.exists(f"{os.path.splitext(filename)[0]}-{index}{os.path.splitext(filename)[1]}"):
        index += 1
    filename = f"{os.path.splitext(filename)[0]}-{index}{os.path.splitext(filename)[1]}"


# Agora, filename contém um nome de arquivo exclusivo
cv2.imwrite('{}'.format(filename), frame)
print(filename)
