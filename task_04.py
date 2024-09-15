# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

COUNT = 10
step = 0

num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(f"Рандомное число = {num}")

while step < COUNT:
    val = int(input("Введите число: "))
    if val > num:
        print('Меньше')
    elif val < num:
        print('Больше')
    else:
        print('Число угадано')
        break
    step += 1
    print(f'Осталось {COUNT - step} попыток!')
    print('-' * 30)

else:
    print("Число не угадано!")