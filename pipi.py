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

def transform_filename(name: str) -> str:
    """Заменяет пробелы и подчёркивания на перенос строки."""
    name_no_ext, ext = os.path.splitext(name)
    transformed = name_no_ext.replace(' ', '<br>').replace('_', '<br>')
    return f"{transformed}{ext}"

# Печатаем как JS-массив
print("const imageFiles = [")
for i, filename in enumerate(image_files):
    comma = ',' if i < len(image_files) - 1 else ''
    transformed_name = transform_filename(filename)
    print(f'  "{transformed_name}"{comma}')
print("];")