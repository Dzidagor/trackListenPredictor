import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import Ridge
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

# Поиск лучших параметров для Ridge
ridge = Ridge()
parameters = {'alpha': [0.01, 0.1, 1, 10, 100]}
ridge_cv = GridSearchCV(ridge, parameters, scoring='neg_mean_squared_error', cv=5)
ridge_cv.fit(X_train, y_train)

# Обучение модели Ridge с лучшими параметрами
best_ridge_model = ridge_cv.best_estimator_
best_ridge_model.fit(X_train, y_train)

# Сохранение обученной модели
if FILTERED:
    dump(best_ridge_model, '../../results/models_configs/ridge_filtered.joblib')
else:
    dump(best_ridge_model, '../../results/models_configs/ridge.joblib')

