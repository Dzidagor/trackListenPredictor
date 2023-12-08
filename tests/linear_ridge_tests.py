import pandas as pd
from joblib import load
from sklearn.metrics import mean_squared_error, r2_score
from globals import FILTERED
# Загрузка тестовых данных и загрузка моделей
if FILTERED:
    data = pd.read_excel('../data/processed/test_listening_data_filtered.xlsx')
    linear_model = load('../results/models_configs/linear_regression_filtered.joblib')
    ridge_model = load('../results/models_configs/ridge_filtered.joblib')
else:
    data = pd.read_excel('../data/processed/test_listening_data.xlsx')
    linear_model = load('../results/models_configs/linear_regression.joblib')
    ridge_model = load('../results/models_configs/ridge.joblib')

X_test = data[['Первый день']]
y_test = data['Первый месяц']

# Словарь для хранения результатов
results = {}

# Тестирование моделей
for model_name, model in [('Linear Regression', linear_model), ('Ridge Regression', ridge_model)]:
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    results[model_name] = {'MSE': mse, 'R2': r2}
    print(f"{model_name}:\n MSE: {mse}, R2: {r2}\n")

# Определение лучшей модели
best_model = min(results, key=lambda k: results[k]['MSE'])
print(f"Лучшая модель: {best_model} с MSE: {results[best_model]['MSE']} и R2: {results[best_model]['R2']}")
