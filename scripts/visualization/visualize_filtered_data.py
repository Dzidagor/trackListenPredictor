import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
df = pd.read_excel('../../data/processed/filtered_data.xlsx')

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
fig, ax = plt.subplots(figsize=(15, 10))

# Перемещение осей
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Создание графиков для каждого трека
for upc in grouped_data['UPC'].unique():
    track_data = grouped_data[grouped_data['UPC'] == upc]
    ax.plot(track_data['Дни с релиза'], track_data['Все прослушивания'])

# Настройка легенды и осей
ax.set_xlabel('Дни с момента релиза')
ax.set_ylabel('Все прослушивания')
ax.set_title('Графики прослушиваний треков по дням с момента релиза')
ax.set_xticks(range(0, 31, 1))

# Сохранение графика в файл
plt.savefig('../../results/figures/filtered_data.png')
plt.show()