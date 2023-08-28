def greet():
    greeting = (" Добро пожаловать в игру.\n Введете координаты своего года от 0 до 2 по приниципу:\n "
                "x - номер строки\n y - номер столбца")
    print(greeting)

field = [[" "] * 3 for i in range(3)]

def show():
    print (f" 0 1 2")
    for i in range(3):
        row_index = " ".join(field[i])
        print(f"{i} {row_index}")

def ask():
    while True:
        cords = input(" Ваш ход: ").split()
        if len(cords) != 2:
            print(" Введите 2 координаты.")
            continue
        x, y = cords
        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа.")
            continue
        x, y = map(int, cords)
        if 0 < x > 2 or 0 < y > 2:
            print(" Числа вне диапазона. Введите координаты от 0 до 2.")
            continue
        if field[x][y] != " ":
            print(" Клетка занята.")
            continue
        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)),
                ((1, 0), (1, 1), (1, 2)),
                ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)),
                ((0, 2), (1, 2), (2, 2)),
                ((0, 0), (1, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["O", "O", "O"]:
            print(" Выиграл O.")
            return True
        if symbols == ["X", "X", "X"]:
            print(" Выиграл Х.")
            return True
    return False

greet()

num = 0
while True:
    num += 1
    show()
    if num % 2 == 1:
        print(" Ходит O.")
    else:
        print(" Ходит X.")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "O"
    else:
        field[x][y] = "X"

    if check_win():
        break

    if num == 9:
        print(" Ничья.")
        break






