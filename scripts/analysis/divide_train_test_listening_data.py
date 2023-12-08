import pandas as pd
from sklearn.model_selection import train_test_split
from globals import FILTERED
# Загрузка данных
if FILTERED:
    data = pd.read_excel('../../data/processed/listening_month_by_day_data_filtered.xlsx')
else:
    data = pd.read_excel('../../data/processed/listening_month_by_day_data.xlsx')

# Предполагаем, что "Первый день" - это предиктор, а "Первый месяц" - целевая переменная
X = data[['Первый день']]
y = data['Первый месяц']

# Разделение данных на обучающую и тестовую выборки
# В этом примере 80% данных пойдет на обучение, а 20% на тестирование
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Сохранение обучающей и тестовой выборок
train_data = pd.concat([X_train, y_train], axis=1)
test_data = pd.concat([X_test, y_test], axis=1)

if FILTERED:
    train_data.to_excel('../../data/processed/train_listening_data_filtered.xlsx', index=False)
    test_data.to_excel('../../data/processed/test_listening_data_filtered.xlsx', index=False)
else:
    train_data.to_excel('../../data/processed/train_listening_data.xlsx', index=False)
    test_data.to_excel('../../data/processed/test_listening_data.xlsx', index=False)
