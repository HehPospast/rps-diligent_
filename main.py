import random

"""----------------Stone scissors paper----------------"""

# -----Переменные-----
Computer = random.randrange(1, 4, 1)
# -----Вывод имени компьютера-----
def checkComputername(Computer):
    if Computer == 1:
        Computername = "Камень"
        return Computername
    elif Computer == 2:
        Computername = "Ножницы"
        return Computername
    else:
        Computername = "Бумага"
        return Computername
#-----Инпут игрока-----
def get_input():
    Valid=False
    print("*/*/*/* ROCK PAPER SCISSORS */*/*/* BY HehPospast")
    print("Выберите предмет\n"
          "1 - камень\n"
          "2 - ножницы\n"
          "3 - бумага")
    while not Valid:
     player_answer= input()
     try:
         player_answer = int(player_answer)
     except:
         print("Неверный числовой диапозон")
         continue
     if player_answer >= 1 and player_answer <= 3:
         Valid = True
         return player_answer
     else:
         print("Введите другое число")
#-----Вывод имени игрока-----
def checkUsername(User):
    if User == 1:
        Username = "Камень"
        return Username
    elif User == 2:
        Username = "Ножницы"
        return Username
    else:
        Username = "Бумага"
        return Username
#-----Проверка победы-----
def checkWin(User):
    Username= checkUsername(User)
    Computername=checkComputername(Computer)
    print("[Игрок]-"+Username + " VS " +"[Компьютер]-"+ Computername)
    if(User==Computer):
        print("Ничья")
        winner = "Ничья"
    elif((User == 1 and Computer == 3) or (User == 3 and Computer == 1)):
        print("Бумага Выиграла")
        winner = "Бумага"
    elif((User == 1 and Computer == 2) or (User == 2 and Computer == 1)):
        print("Камень Выиграл")
        winner = "Камень"
    else:
        print("Ножницы Выиграли")
        winner = "Ножницы"


    if winner==Username:
        print("Игрок победил")
    elif winner=="Ничья":
        print("Выиграла дружба")
    else:
        print("Компьютер победил")
#-----Запуск сея залупы-----
def main():
    checkWin(get_input())

main()
#-----Реиграбельность-----
while True:
    print("Если хотите продолжить играть введите S или s")
    getinput= input(str())
    if((getinput=="S")or(getinput=="s")):
        main()
    else:
        exit(1000-7)
