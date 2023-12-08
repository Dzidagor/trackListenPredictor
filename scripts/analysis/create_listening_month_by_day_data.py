# Загрузка данных
import pandas as pd

df = pd.read_excel('../../data/processed/filtered_data.xlsx')

# Преобразование даты в формат datetime
df['Дата'] = pd.to_datetime(df['Дата'], format='%d-%m-%Y')

# Создание столбца с количеством дней с момента релиза
df['Дни с релиза'] = df.groupby('UPC')['Дата'].transform(lambda x: (x - x.min()).dt.days)

# Вычисление прослушиваний за первый день и первый месяц для каждого трека
first_day_listening = df[df['Дни с релиза'] == 0].groupby('UPC')['Все прослушивания'].sum()
first_month_listening = df[df['Дни с релиза'] <= 30].groupby('UPC')['Все прослушивания'].sum()

# Объединение данных в один DataFrame
listening_data = pd.DataFrame({
    'Первый день': first_day_listening,
    'Первый месяц': first_month_listening
}).reset_index()

listening_data['UPC'] = listening_data['UPC'].astype(str)
listening_data.to_excel('../../data/processed/listening_month_by_day_data.xlsx', index=False)
