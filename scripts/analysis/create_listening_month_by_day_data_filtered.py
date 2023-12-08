import pandas as pd

listening_data = pd.read_excel("../../data/processed/listening_month_by_day_data.xlsx")

# Применение фильтрации выбросов с помощью IQR
Q1 = listening_data['Первый день'].quantile(0.25)
Q3 = listening_data['Первый день'].quantile(0.75)
IQR = Q3 - Q1

# Фильтрация значений, которые лежат за пределами 1.5 * IQR от Q1 и Q3
filtered_listening_data = listening_data[
    (listening_data['Первый день'] >= (Q1 - 1.5 * IQR)) &
    (listening_data['Первый день'] <= (Q3 + 1.5 * IQR))
]

# Сохранение отфильтрованных данных
filtered_listening_data.to_excel('../../data/processed/listening_month_by_day_data_filtered.xlsx', index=False)
