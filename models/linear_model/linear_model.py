import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Загрузка данных
data = pd.read_excel('../../data/processed/listening_month_by_day_data.xlsx')

# Предполагаем, что "Первый день" - это предиктор, а "Первый месяц" - целевая переменная
X = data[['Первый день']]
y = data['Первый месяц']

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Создание и обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказание на тестовых данных
y_pred = model.predict(X_test)

# Визуализация фактических и предсказанных данных
plt.scatter(X_test, y_test, color='blue', label='Фактические данные')
plt.scatter(X_test, y_pred, color='red', label='Предсказанные данные', alpha=0.5)

# Настройка графика
plt.xlabel('Прослушивания за первый день')
plt.ylabel('Прослушивания за первый месяц')
plt.title('Предсказание прослушиваний за месяц')
plt.legend()

# Показать график
plt.show()
