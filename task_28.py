# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def get_value_from_user(message: str) -> int:
    flag = True
    
    while flag:
        try:
            user_value = int(input(message))

            if user_value < 0:
                print("Число должно быть положительным!")
                continue
            
            flag = False
        except ValueError:
            print("Вы ввели неправильное значение!Введите целое, неотрицательное число!")
    
    return user_value

def sum_numb(value_1: int, value_2: int, res_sum: int) -> int:
    if value_1 > 0 and value_2 > 0:
        res_sum += 1 + 1
        return sum_numb(value_1 - 1, value_2 - 1, res_sum)
    elif value_1 > 0:
        res_sum += 1
        return sum_numb(value_1 - 1, value_2, res_sum)
    elif value_2 > 0:
        res_sum += 1
        return sum_numb(value_1, value_2 - 1, res_sum)

    return res_sum

def print_report(res):
    print(f"Результат суммы данных двух чисел -> {res}")

##################################################################

numb_1 = get_value_from_user("Введите целое, неотрицательное число №1: ")
numb_2 = get_value_from_user("Введите целое, неотрицательное число №2: ")

res_numb = 0
result = sum_numb(numb_1, numb_2, res_numb)

print()
print_report(result)