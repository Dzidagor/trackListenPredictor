import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from joblib import dump
from globals import FILTERED

# Загрузка и подготовка данных
if FILTERED:
    data = pd.read_excel('../../data/processed/train_listening_data_filtered.xlsx')
else:
    data = pd.read_excel('../../data/processed/train_listening_data.xlsx')
X = data[['Первый день']]
y = data['Первый месяц']

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели LinearRegression
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Сохранение обученной модели
if FILTERED:
    dump(linear_model, '../../results/models_configs/linear_regression_filtered.joblib')
else:
    dump(linear_model, '../../results/models_configs/linear_regression.joblib')

