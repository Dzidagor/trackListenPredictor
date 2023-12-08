import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

ds = pd.read_excel('../../data/processed/listening_month_by_day_data_filtered.xlsx')

# Настройки визуализации
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Создание графика
sns.scatterplot(x='Первый день', y='Первый месяц', data=ds)

# Настройка легенды и осей
plt.xlabel('Прослушивания за первый день')
plt.ylabel('Прослушивания за первый месяц')
plt.title('Соотношение прослушиваний за первый день и первый месяц')

# Сохранение графика в файл
plt.savefig('../../results/figures/listening_month_by_day_data_filtered.png')
plt.show()
