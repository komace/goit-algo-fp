import turtle


# Функція для малювання дерева
def draw_tree(branch_length, level, angle):
    if level == 0:
        return
    
    turtle.forward(branch_length)
    turtle.left(angle)
    draw_tree(branch_length * 0.7, level - 1, angle)
    turtle.right(2 * angle)
    draw_tree(branch_length * 0.7, level - 1, angle)
    turtle.left(angle)
    turtle.backward(branch_length)

def main():
    # Ініціалізація екрану та черепахи
    turtle.speed("fastest")
    turtle.left(90)
    turtle.up()
    turtle.backward(100)
    turtle.down()
    
    # Отримання рівня рекурсії від користувача
    level = int(input("Введіть рівень рекурсії: "))
    
    # Малювання дерева
    draw_tree(100, level, 30)
    
    # Завершення малювання
    turtle.done()

if __name__ == "__main__":
    main()
