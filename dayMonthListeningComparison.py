import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
df = pd.read_excel('filtered_data.xlsx')

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

# Настройки визуализации
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Создание графика
sns.scatterplot(x='Первый день', y='Первый месяц', data=listening_data)

# Настройка легенды и осей
plt.xlabel('Прослушивания за первый день')
plt.ylabel('Прослушивания за первый месяц')
plt.title('Соотношение прослушиваний за первый день и первый месяц')

# Сохранение графика в файл
plt.savefig('day_month_listening_comparison.png')
plt.show()
