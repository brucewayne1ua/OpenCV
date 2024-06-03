import cv2

# Загрузка предварительно обученного классификатора каскада Хаара для лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Захват видеопотока с веб-камеры
cap = cv2.VideoCapture(0)

while True:
    # Считываем кадр с камеры
    ret, frame = cap.read()

    # Преобразование изображения в оттенки серого
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Обнаружение лиц на кадре
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Отрисовка прямоугольника вокруг обнаруженных лиц
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Отображение кадра с лицами
    cv2.imshow('Face Detection', frame)

    # Для выхода из приложения нажмите 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()
