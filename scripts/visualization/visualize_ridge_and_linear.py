import pandas as pd
import matplotlib.pyplot as plt
from joblib import load
from globals import FILTERED

# Загрузка тестовых данных и загружка моделей
if FILTERED:
    data = pd.read_excel('../../data/processed/listening_month_by_day_data_filtered.xlsx')
    linear_model = load('../../results/models_configs/linear_regression_filtered.joblib')
    ridge_model = load('../../results/models_configs/ridge_filtered.joblib')
else:
    data = pd.read_excel('../../data/processed/listening_month_by_day_data.xlsx')
    linear_model = load('../../results/models_configs/linear_regression.joblib')
    ridge_model = load('../../results/models_configs/ridge.joblib')

X_test = data[['Первый день']]
y_test = data['Первый месяц']

# Получение предсказаний
linear_pred = linear_model.predict(X_test)
ridge_pred = ridge_model.predict(X_test)

# Визуализация
plt.figure(figsize=(12, 6))
plt.scatter(X_test, y_test, color='black', label='Real Data')
plt.scatter(X_test, linear_pred, color='blue', label='Linear Regression Predictions')
plt.scatter(X_test, ridge_pred, color='red', label='Ridge Regression Predictions', alpha=0.5)
plt.xlabel('Прослушивания за первый день')
plt.ylabel('Прослушивания за первый месяц')
plt.title('Сравнение предсказаний моделей')
plt.legend()
plt.show()
