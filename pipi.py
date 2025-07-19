import os

# Путь к папке с изображениями
folder_path = 'images/каменка'  # например: r'C:\Users\Ivan\Desktop\картинки'

# Поддерживаемые расширения
image_extensions = {'.png', '.jpg', '.jpeg', '.webp'}

# Получаем список файлов
image_files = [
    f for f in os.listdir(folder_path)
    if os.path.isfile(os.path.join(folder_path, f)) and os.path.splitext(f)[1].lower() in image_extensions
]

# Сортируем по имени (можно убрать при необходимости)
image_files.sort()

# Пишем в формате JavaScript массива
print("const imageFiles = [")
for i, filename in enumerate(image_files):
    comma = ',' if i < len(image_files) - 1 else ''
    print(f'  "{filename}"{comma}')
print("];")
