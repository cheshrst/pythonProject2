## Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
month = int(input("Введите номер месяца: "))
season_lst = ["Лето", "Осень", "Зима", "Весна"]
if month ==12 or month ==1 or month ==2:
    print(season_lst[2])
elif month == 3 or month == 4 or month == 5:
    print(season_lst[3])
elif month == 6 or month == 7 or month == 8:
    print(season_lst[0])
elif month == 9 or month == 10 or month == 11:
    print(season_lst[1])
else:
    print("Несуществующий месяц")