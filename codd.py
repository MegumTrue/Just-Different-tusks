from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Загружаем изображение и преобразовываем его в черно-белое
img = Image.open("C:\photo_2024-12-07_19-53-26.jpg").convert('L')
bw_pixels = np.array(img)

# Функция для кодирования методом длин серий
def run_length_encoding(pixels):
    encoding = []
    previous_pixel = pixels[0]
    count = 1
    for pixel in pixels[1:]:
        if pixel == previous_pixel:
            count += 1
        else:
            encoding.append((previous_pixel, count))
            previous_pixel = pixel
            count = 1
    encoding.append((previous_pixel, count))
    return encoding

# Применяем кодирование к первой строке
first_row_bw = bw_pixels[0]
encoded_row = run_length_encoding(first_row_bw)

# Визуализация
plt.figure(figsize=(12, 6))

# Исходное черно-белое изображение
plt.subplot(1, 2, 1)
plt.title("Черно-белое изображение")
plt.imshow(bw_pixels, cmap='gray')
plt.axis("off")

# Создаем массив для закодированного изображения
max_length = sum(count for _, count in encoded_row)
encoded_image = np.zeros(max_length, dtype=np.uint8)

# Заполняем закодированное изображение
index = 0
for pixel, count in encoded_row:
    encoded_image[index:index+count] = pixel
    index += count

# Переупаковываем закодированное изображение в 2D для отображения
encoded_image_2d = encoded_image.reshape(1, -1)

plt.subplot(1, 2, 2)
plt.title("Закодированное изображение")
plt.imshow(encoded_image_2d, cmap='gray', aspect='auto')
plt.axis("off")

plt.show()

# Вывод результатов
length_bw = len(first_row_bw) * 8
length_encoded = sum(len(bin(count)) + 1 for _, count in encoded_row)
compression_ratio = length_bw / length_encoded

print("Длина бинарного кода исходного изображения:", length_bw)
print("Длина закодированного изображения:", length_encoded)
print("Степень сжатия:", compression_ratio)

# Загружаем изображение
original_image = Image.open("C:\photo_2024-12-07_19-53-26.jpg")

# Rotate image
rotated_image = original_image.transpose(method=Image.ROTATE_270)

# Extract first column of pixels
first_column_original = list(rotated_image.getdata())[:rotated_image.height]

# Convert image to black and white
bw_image = rotated_image.convert("L")
bw_pixels = list(bw_image.getdata())
first_column_bw = bw_pixels[:bw_image.height]

# Print results
print("Первый столбец пикселей оригинального изображения:", first_column_original)
print("Первый столбец пикселей черно-белого изображения:", first_column_bw)