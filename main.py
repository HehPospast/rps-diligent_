import random
import time
import os

"""----------------Stone scissors paper----------------"""



# -----Очистка консоли-----
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
# -----Очистка консоли-----


# -----Вывод имени компьютера-----
def check_computer_name(computer):
    if computer == 1:
        computer_name = "Камень"
        return computer_name
    elif computer == 2:
        computer_name = "Ножницы"
        return computer_name
    else:
        computer_name = "Бумага"
        return computer_name


# -----Input игрока-----
def get_input():
    valid = False
    cls()
    print("*/*/*/* ROCK PAPER SCISSORS */*/*/* BY HehPospast")
    print("Выберите предмет\n"
          "1 - камень\n"
          "2 - ножницы\n"
          "3 - бумага")
    while not valid:
        player_answer = input('[Выбор]-')
        try:
            player_answer = int(player_answer)
        except:
            print("Неверный числовой диапазон")
            continue
        if 1 <= player_answer <= 3:
            valid = True
            return player_answer
        else:
            print("Введите другое число")
# -----Input игрока-----


# -----Вывод имени игрока-----
def check_username(user):
    if user == 1:
        username = "Камень"
        return username
    elif user == 2:
        username = "Ножницы"
        return username
    else:
        username = "Бумага"
        return username
# -----Вывод имени игрока-----


# -----Проверка победы-----
def check_win(user):
    computer = random.randrange(1, 4, 1)
    username = check_username(user)
    computer_name = check_computer_name(Computer)
    time.sleep(2)
    print("[Игрок]-" + username + " VS " + "[Компьютер]-" + computer_name)
    if user == Computer:
        print("Ничья")
        winner = "Ничья"
    elif (user == 1 and Computer == 3) or (user == 3 and Computer == 1):
        winner = "Бумага"
    elif (user == 1 and Computer == 2) or (user == 2 and Computer == 1):
        winner = "Камень"
    else:
        winner = "Ножницы"

    time.sleep(1)
    if winner == username:
        print("Игрок победил")
    elif winner == "Ничья":
        print("Выиграла дружба")
    else:
        print("Компьютер победил")
# -----Проверка победы-----


# -----Запуск сея чуда-----
def main():
    check_win(get_input())
# -----Запуск сея чуда-----


main()


# -----Реиграбельность-----
while True:
    print("Если хотите продолжить играть нажмите ENTER, чтобы закончить играть введите любой текст!")
    get_input_2 = input(str())
    if get_input_2 == "":
        cls()
        main()
    else:
        exit(1000 - 7)
