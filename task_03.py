# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input('Введите число: '))
min_val = 0
max_val = 100_000


def check_num(val):
    if val < min_val or val > max_val:
        return False
    return True


def check_value(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
            if count > 2:
                return False
    return True


if check_num(num) is False:
    print(f'Требовалось ввести число в диапазоне от {min_val} до {max_val}')
else:
    if check_value(num) is False:
        print("Число является составным")
    else:
        print("Число является простым")
