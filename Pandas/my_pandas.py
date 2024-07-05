import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/Yorko/mlcourse.ai/main/data/titanic_train.csv"

# 1. Сколько мужчин и женщин было на борту?
data = pd.read_csv(url, index_col="PassengerId")

gender = data['Sex'].value_counts()
print(gender)
# --> 577 мужчин и 314 женщины

# 2. Выведите распределение переменной Pclass.
# Затем сделайте тоже самое, но для мужчин и женщин отдельно.
# Сколько мужчин из 2 класса было на бору??
data = pd.read_csv(url, index_col="PassengerId")

pclass = data['Pclass'].value_counts()
print("Распределение Pclass для всех:\n", pclass)

pclass_males = data[data['Sex'] == 'male']['Pclass'].value_counts()
pclass_females = data[data['Sex'] == 'female']['Pclass'].value_counts()

print("\nРаспределение Pclass для мужчин:\n", pclass_males)
print("\nРаспределение Pclass для женщин:\n", pclass_females)

men_in_second = pclass_males[2]
print("\nМужчин из 2 класса:", men_in_second)
# --> 108 мужчин

# 3. Какое среднее и стандратное отклонение у переменной Fare?.
# Округлите до 2 знаков.
data = pd.read_csv(url, index_col="PassengerId")

fare_mean = round(data['Fare'].mean(), 2)
fare_std = round(data['Fare'].std(), 2)

print("median -", fare_mean) # --> 32.2
print("standard deviation -", fare_std) # --> 49.69

# 4. Правда ли, что средний возраст выживших больше, чем погибших?
data = pd.read_csv(url, index_col="PassengerId")

survived = round(data[data['Survived'] == 1]['Age'].mean(), 2) # --> 28.34
not_survived = round(data[data['Survived'] == 0]['Age'].mean(), 2) # --> 30.63

if survived > not_survived:
    print("Да")
else:
    print("Нет")
# Правильный ответ "НЕТ"

# 5. Правда ли, что среди пассажиров, моложе 30,
# процент выживаемости больше, чем у пассажиров старше 60?
# Какой процент выживших среди молодых и пожилых людей?
data = pd.read_csv(url, index_col="PassengerId")

young_passengers = data[data['Age'] < 30]
old_passengers = data[data['Age'] > 60]

young_rate = young_passengers['Survived'].mean() * 100
old_rate = old_passengers['Survived'].mean() * 100

print(f"{young_rate:.1f}% среди молодых и {old_rate:.1f}% среди пожилых")
# 40.6% среди молодых и 22.7% среди пожилых

if young_rate > old_rate:
    print("Правда") # --> Правда
else:
    print("Не правда")

# 6. Правда ли, что средли выживших больше женщин?
# Какое What are shares of survived people among men and women?
data = pd.read_csv(url, index_col="PassengerId")

male_rate = data[data['Sex'] == 'male']['Survived'].mean() * 100
female_rate = data[data['Sex'] == 'female']['Survived'].mean() * 100

if female_rate > male_rate:
    print("Да, среди выживших больше женщин.") # --> Да
else:
    print("Нет, среди выживших больше мужчин.")

print(f"{male_rate:.1f}% cреди мужчин и {female_rate:.1f}% среди женщин")
# 18.9% cреди мужчин и 74.2% среди женщин

# 7. Какое самое популярное мужское имя?
data = pd.read_csv(url, index_col="PassengerId")

male_passengers_id = data[data['Sex'] == 'male']

Charles = Thomas = William = John = 0
male_names = male_passengers_id['Name'].tolist()
for i in range(len(male_names)):
    if 'Charles' in male_names[i]:
        Charles += 1
    elif 'John' in male_names[i]:
        John += 1
    elif 'William' in male_names[i]:
        William += 1
    elif 'Thomas' in male_names[i]:
        Thomas += 1

most_common_name = max(Charles, Thomas, William, John)

if most_common_name == Charles:
    print("Charles")
elif most_common_name == John:
    print("John")
elif most_common_name == William:
    print("William") # --> William
elif most_common_name == Thomas:
    print("Thomas")

# 8. Как средние возраст мужчин/женщин зависит от переменной Pclass?
# Выберите верные утверждения:
# В среднем, мужчины из 1 класса старше 40
# В среднем, женщины из 1 класса старше 40
# Мужчины из всех классов в среднем старше женщин, из того же класса
# В среднем, пассажиры первого класса старше, чем пассажиров из 2 класса, а те в свою очередь старше пассажиров из 3 класса
data = pd.read_csv(url, index_col="PassengerId")

data['Age'].fillna(data['Age'].mean(), inplace=True)

average_ages = data.groupby(['Sex', 'Pclass'])['Age'].mean().unstack()

print(average_ages, '\n')

men_first_class_avg_age = average_ages.loc['male', 1]
women_first_class_avg_age = average_ages.loc['female', 1]

print(men_first_class_avg_age > 40)# 1 вопрос
print(women_first_class_avg_age > 40)# 2 вопрос

men_older_than_women = average_ages.loc['male'] > average_ages.loc['female']
print(all(men_older_than_women))# 3 вопрос

class_age_ordered = average_ages.mean(axis=0).sort_values(ascending=False) == average_ages.mean(axis=0)
print(class_age_ordered.all())# 4 вопрос

# 9. Сравните графически распределение стоимости билетов и
# возраста у спасенных и у погибших.
# Средний возраст погибших выше, верно?
data = pd.read_csv(url, index_col="PassengerId")

data['Age'].fillna(data['Age'].mean(), inplace=True)

plt.figure(figsize=(14, 7))

sns.kdeplot(data[data['Survived'] == 1]['Fare'], label='Спасенные', shade=True)
sns.kdeplot(data[data['Survived'] == 0]['Fare'], label='Погибшие', shade=True)

plt.title('Стоимость билетов у спасенных и погибших')
plt.xlabel('Стоимость билета')
plt.ylabel('Кол-во')
plt.legend()
plt.show()

plt.figure(figsize=(14, 7))

sns.kdeplot(data[data['Survived'] == 1]['Age'], label='Спасенные', shade=True)
sns.kdeplot(data[data['Survived'] == 0]['Age'], label='Погибшие', shade=True)

plt.title('Возраст у спасенных и погибших')
plt.xlabel('Возраст')
plt.ylabel('Кол-во')
plt.legend()
plt.show()

avg_dead = data[data['Survived'] == 0]['Age'].mean()

avg_survived = data[data['Survived'] == 1]['Age'].mean()

print(f"Средний возраст погибших: {avg_dead:.2f}")
print(f"Средний возраст спасенных: {avg_survived:.2f}")

print(avg_dead > avg_survived)

# 10. Какая средняя цена билета у
# погибших мужчин и у выживших женщин?
# Верно ли, что первая цена больше?
data = pd.read_csv(url, index_col="PassengerId")

avg_fare_men = data[(data['Survived'] == 0) & (data['Sex'] == 'male')]['Fare'].mean()
avg_fare_women = data[(data['Survived'] == 1) & (data['Sex'] == 'female')]['Fare'].mean()

print(f"Средняя цена билета у погибших мужчин: {avg_fare_men:.2f}")
print(f"Средняя цена билета у выживших женщин: {avg_fare_women:.2f}")

print(avg_fare_men > avg_fare_women) # Нет