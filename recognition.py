import cv2
import numpy as np

# Загрузка предварительно обученной модели (например, на базе данных MNIST)
# Здесь предполагается, что вы уже обучили модель на соответствующем наборе данных
# Если нет, сначала обучите модель
# model = load_your_model()

# Функция предобработки изображения и распознавания объекта
def preprocess_and_detect(frame):
    # Ваш код для предобработки изображений и распознавания объекта
    # Вернуть распознанный объект и его цвет
    return detected_object, detected_color

# Функция для обработки нажатий клавиш
def process_key(key, x, y, w, h):
    move_step = 10
    size_step = 5

    if key == ord("w"):
        y -= move_step
    elif key == ord("s"):
        y += move_step
    elif key == ord("a"):
        x -= move_step
    elif key == ord("d"):
        x += move_step
    elif key == ord("+"):
        w += size_step
        h += size_step
    elif key == ord("-"):
        w -= size_step
        h -= size_step

    return x, y, w, h

cap = cv2.VideoCapture(0)

# Начальные параметры рамки
x, y, w, h = 100, 100, 100, 100

while True:
    ret, frame = cap.read()

    # Выделение рамки на изображении
    roi = frame[y:y+h, x:x+w]

    # Предобработка и распознавание объекта в рамке
    detected_object, detected_color = preprocess_and_detect(roi)

    # Отображение рамки и информации о найденном объекте
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(frame, f"Object: {detected_object}, Color: {detected_color}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Frame', frame)

    # Обработка нажатия клавиш
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    x, y, w, h = process_key(key, x, y, w, h)

cap.release()
cv2.destroyAllWindows()