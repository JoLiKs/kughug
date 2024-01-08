import cv2
import matplotlib.pyplot as plt

def get_average_color(image):
    # Преобразование изображение из цветового пространства BGR в RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Вычисление среднего цвета по каждому каналу RGB
    average_color = rgb_image.mean(axis=(0, 1))
    return average_color

def on_click(event):
    # Получение координат клика мышью
    x, y = event.xdata, event.ydata
    if x is None or y is None:
        return
    # Вычисление преобладающего цвета и среднего цвета для области вокруг клика
    roi = image[int(y)-5:int(y)+5, int(x)-5:int(x)+5]
    dominant_color = roi.reshape(-1, 3).mean(axis=0)
    average_color = get_average_color(roi)
    # Вывод информации о цветах
    print("Преобладающий цвет:", dominant_color)
    print("Средний цвет:", average_color)

# Загрузка изображения
image = cv2.imread("r1.png")

# Отображение изображения с использованием matplotlib
plt.imshow(image)
plt.axis('off')

# Привязка обработчика клика мышью
fig = plt.gcf()


# Отображение окна с изображением
plt.show()

