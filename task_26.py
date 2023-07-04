# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def get_value_from_user(message: str) -> int | float:                       # Данная функция приглашает юзера к вводу и проверяет ввод на исключения,
    flag = True                                                             # а также даёт возможность пользователю вводить вещественные числа как с точкой,
                                                                            # так и с запятой, убирает пробелы между знаком и числом и определяет, нужно ли вернуть
    while flag:                                                             # float, либо int, в зависимости от числа и от того, нужна ли нам степень(по условию целое число),
        if message == "Введите число: ":                                    # либо число(нет строгих указаний в условию по числу, может быть дробным и целым)
            try:
                user_value = input(message)
                user_value = user_value.replace(" ", "")

                if user_value.count(",") > 0 or user_value.count(".") > 0:
                    user_value = float(user_value.replace(",", "."))
                else:
                    user_value = int(user_value)

                flag = False
            except ValueError:
                print("Вы ввели неправильное значение!Введите число!")
        else:
            try:
                user_value = int(input(message).replace(" ", ""))
                flag = False
            except ValueError:
                print("Вы ввели неправильное значение!Степень должна быть целым числом!")

    return user_value

def numb_exponent(value: float | int, pow: int) -> int | float | None:          # Данная фукнция возвращает None в случае, если у нас число = 0, а степень < 0,
    if value == 0 and pow < 0:                                                  # так как так на 0 делить нельзя, а в иных случаях возвращает результат согласно
        return                                                                  # входным данным. Данная функция может возводить как в отрицательную целую степень,
                                                                                # так и положительную, а при степени 0 всегда вернёт единицу. 
    if pow == 0:
        return 1
    elif pow < 0:
        return value * (1 / numb_exponent(value, abs(pow - 1)))
    else:
        return value * numb_exponent(value, pow - 1)

def print_report(res: int | float | None) -> None:
    if res == None:
        print(f"Нельзя возвести число '0' в отрицательную степень!")
    else:
        print(f"Результатом возведения в степень данного числа стало значение -> {res}")

###########################################################

number = get_value_from_user("Введите число: ")
numb_pow = get_value_from_user("Введите целую степень для возведения числа: ")

result = numb_exponent(number, numb_pow)

print()
print_report(result)