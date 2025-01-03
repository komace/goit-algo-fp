def greedy_algorithm(items, max_cost):
    
    # Сортуємо предмети за відношенням вартості до калорійності
    sorted_items = sorted(items, key=lambda x: items[x]["cost"])
    # Ініціалізуємо змінні для зберігання загальної вартості та калорійності
    total_cost = 0
    total_calories = 0
    # Ініціалізуємо список для зберігання результату
    result = []
    
    
    for item in sorted_items:
        # Перевіряємо, чи можна додати предмет до списку
        if total_cost + items[item]["cost"] <= max_cost:
            result.append(item)
            # Оновлюємо загальну вартість та калорійність
            total_cost += items[item]["cost"]
            total_calories += items[item]["calories"]
    return result, total_calories

# Перелік предметів
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

max_cost = 100
result, total_calories = greedy_algorithm(items, max_cost)
print(f"Результат: {result}")
print(f"Загальна калорійність: {total_calories}")

def dynamic_programming(items, max_cost):
    # Ініціалізуємо матрицю для зберігання результатів
    n = len(items)
    item_list = list(items.items())
    dp = [[0] * (max_cost + 1) for _ in range(n + 1)]
    
    # Заповнюємо матрицю
    for i in range(1, n + 1):
        item_name, item_info = item_list[i - 1]
        cost = item_info["cost"]
        calories = item_info["calories"]
        # Перебираємо можливі варіанти
        for j in range(max_cost + 1):
            if cost > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
    # Відновлення результату
    j = max_cost
    chosen_items = []
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            item_name, item_info = item_list[i - 1]
            chosen_items.append(item_name)
            j -= item_info["cost"]
    
    return chosen_items, dp[n][max_cost]

max_cost = 100
chosen_items, total_calories = dynamic_programming(items, max_cost)
print(f"Результат: {chosen_items}")
print(f"Загальна калорійність: {total_calories}")    