import json
from datetime import timedelta
import pandas as pd

# Загрузка данных из JSON-файла
with open('../../data/raw/releases.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Извлечение UPC и дат релизов
track_info = [(album['upc'], album['release_date']) for album in data['albums']]

# Объединение данных из всех Excel-файлов
excel_files = [
    '../../data/raw/data1.xlsx',
    '../../data/raw/data2.xlsx',
    '../../data/raw/data3.xlsx',
    '../../data/raw/data4.xlsx'
]
combined_df = pd.concat([pd.read_excel(file) for file in excel_files], ignore_index=True)

# Преобразование колонки UPC в строку
combined_df['UPC'] = combined_df['UPC'].astype(str)

# Функция для фильтрации данных
def filter_data(df, track_json):
    filtered_rows = []

    for upc, release_date in track_json:
        release_date = pd.to_datetime(release_date)
        end_date = release_date + timedelta(days=30)

        # Фильтрация по UPC и дате
        rows = df[(df['UPC'] == upc) & (pd.to_datetime(df['Дата'], format='%d-%m-%Y') >= release_date) & (pd.to_datetime(df['Дата'], format='%d-%m-%Y') <= end_date)]
        filtered_rows.append(rows)

    return pd.concat(filtered_rows)

# Фильтрация объединённых данных
filtered_data = filter_data(combined_df, track_info)

# Сохранение отфильтрованных данных в новый Excel-файл
filtered_data.to_excel('../processed/filtered_data.xlsx', index=False)
