
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def rgb_to_grayscale(image):
    return image.convert("L")
# кодирование длины серий
def rle_encode(image):
    pixels = np.array(image).flatten()
    encoded = []
    prev_pixel = pixels[0]
    count = 1

    for pixel in pixels[1:]:
        if pixel == prev_pixel:
            count += 1
        else:
            encoded.append((prev_pixel, count))
            prev_pixel = pixel
            count = 1
    encoded.append((prev_pixel, count))
    return encoded
# возвращение данных
def rle_decode(encoded, width):
    decoded = []
    for pixel, count in encoded:
        decoded.extend([pixel] * count)
    return np.array(decoded).reshape(-1, width)

def calculate_compression_ratio(original_size, encoded_size):
    return original_size / encoded_size

def to_binary_string(encoded):
    binary_string = ''
    for pixel, count in encoded:
        binary_string += f'{pixel:08b}' * count 
    return binary_string

# Загружаем изображение и преобразовываем его в черно-белое
image_path = "C:\photo_2024-03-22_12-52-36.jpg"
image = Image.open(image_path)
bw_image = rgb_to_grayscale(image)

encoded_image = rle_encode(bw_image)
# определяем размеры фото
original_size = np.array(bw_image).size
encoded_size = len(encoded_image)
# высчитываем сжатие
compression_ratio = calculate_compression_ratio(original_size, encoded_size)

width = bw_image.size[0]
first_row_encoded = rle_decode(encoded_image, width)[0]

first_row_image = Image.new('L', (len(first_row_encoded), 1))
first_row_image.putdata(first_row_encoded)

binary_string = to_binary_string(encoded_image)

print(f"Первый строка пикселей оригинального изображения: {original_size}")
print(f"Первый строка пикселей черно-белого изображения: {encoded_size}")
print(f"коэфицент сжатия: {compression_ratio:.9f}")

print(f"первые 45 символов сжатого изображения:\n{binary_string[:45]}")

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Оригинальное изображение")
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Кодирование RLE")
plt.imshow(bw_image, cmap='grey')
plt.axis('off')

plt.show()