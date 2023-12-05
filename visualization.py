import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
df = pd.read_excel('filtered_data.xlsx')

# Преобразование даты в формат datetime
df['Дата'] = pd.to_datetime(df['Дата'], format='%d-%m-%Y')

# Создание столбца с количеством дней с момента релиза
df['Дни с релиза'] = df.groupby('UPC')['Дата'].transform(lambda x: (x - x.min()).dt.days)

# Ограничение данных до 30 дней с момента релиза
df = df[df['Дни с релиза'] <= 30]

# Группировка данных по UPC и количеству дней с момента релиза, суммирование прослушиваний
grouped_data = df.groupby(['UPC', 'Дни с релиза'])['Все прослушивания'].sum().reset_index()

# Настройки визуализации
sns.set(style="whitegrid")
plt.figure(figsize=(15, 10))

# Создание графиков для каждого трека
for upc in grouped_data['UPC'].unique():
    track_data = grouped_data[grouped_data['UPC'] == upc]
    plt.plot(track_data['Дни с релиза'], track_data['Все прослушивания'], label=upc)

# Настройка легенды и осей
plt.legend()
plt.xlabel('Дни с момента релиза')
plt.ylabel('Все прослушивания')
plt.title('Графики прослушиваний треков по дням с момента релиза')
plt.xticks(range(0, 31, 1))
plt.tight_layout()

# Сохранение графика в файл
plt.savefig('tracks_listening_graph.png')
plt.show()
