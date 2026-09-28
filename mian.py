def save_user_data(filename, data):
    file = open(filename, "w")
    file.write("--- USER DATA ---\n")
    for key, value in data.items():
        file.write(f"{key}: {value}\n")
    # Сохраняем и закрываем
    
def process_scores(scores):
    total = 0
    count = 0
    average = 0
    for score in scores:
        if score > 0:
            total += score
            count += 1  # Считаем количество положительных оценок
    if count == 0:
        raise ValueError("Нет положительных оценок")
    else:
        average = total / count
    return average

user_info = {"name": "Артёи", "age": 12, "city": "Иркутск"}
save_user_data("user.txt", user_info)

user_scores = [-5, -2, 0]
try:
    print("Средняя положительная оценка:", process_scores(user_scores))
except ValueError as e:
    print(f"Ошибка: {e}")
    