

import random

print("Я загадал число от 1 до 10. Попробуй угадать! ")

secret = random.randint(1, 10)


for attempt in range(3):
    print("Попытка номер", attempt + 1)

    guess = input("Твоё число: ")
    guess = int(guess)

    if guess == secret:
        print("Поздравляю! Ты угадал!")
        break
    elif guess < secret:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")


else:
    print("Попытки закончились. Я загадал число:", secret)


