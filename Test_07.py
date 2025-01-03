import random
import matplotlib.pyplot as plt


# Функція для моделювання гри в кубики
def monte_carlo_simulation(rolls):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sums_count[dice1 + dice2] += 1

    probabilities = {s: count / rolls for s, count in sums_count.items()}
    return probabilities

rolls = 1_000_000
probabilities = monte_carlo_simulation(rolls)
# Виведення результатів
for dice_sum, probability in probabilities.items():
    print(f"Сума: {dice_sum}, ймовірність: {probability}")

# Побудова графіка
monte_carlo_table = [(dice_sum, probability) for dice_sum, probability in probabilities.items()]
monte_carlo_table.sort()

sums = [X[0] for X in monte_carlo_table]
probs = [X[1] for X in monte_carlo_table]

plt.bar(sums, probs, color='blue', edgecolor='black')
plt.xlabel('Сума')
plt.ylabel('Ймовірність')
plt.title('Моделювання методом Монте-Карло')
plt.xticks(sums)
plt.grid(axis="y")
plt.show()

print("Сума\tЙмовірність")
for dice_sum, probability in monte_carlo_table:
    print(f"{dice_sum}\t{round(probability, 4)}")