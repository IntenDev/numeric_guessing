import random
# TODO: Добавить возможность указания правой границы для случайного числа (от 1 до n)
n = random.randint(1, 101)
print('Добро пожаловать в числовую угадайку')

def is_valid(item):
    if item.isnumeric() and int(item) / float(item) == 1.0 and 1 <= int(item) <= 100:
        return True
    else:
        return False


cnt_variant = 0
ch = True
while ch == True:
    s = input('Введите целое число от 1 до 100 - ')
    if is_valid(s):
        s = int(s)
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
    if s < n:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        cnt_variant += 1
    elif s > n:
        print('Ваше число больше загаданного, попробуйте еще разок')
        cnt_variant += 1
    elif s == n:
        print('Вы угадали поздравляем!')
        print('Количество попыток - ', cnt_variant)
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        # TODO: Добавить возможность генерации нового числа "n"
        ch = False