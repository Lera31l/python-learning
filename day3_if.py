
# =====Задание 1 =====

age = input("Сколько тебе лет? ")
age = int(age)

if age >= 18:
    print("Доступ разрешён")
else:
    print("Доступ запрещён")


# ===== Задание 2 ====

shards = input("Сколько у тебя NeuroShards?  ")
shards = int(shards)

if shards >= 100:
    print("Можно купить улучшение оружия")
else:
    print("Нужно ещё фармить")

# ==== Задание 3 ====

number = input("Напиши число: ")
number = int(number)

if number > 0:
    print("Положительное")
elif number == 0:
    print("Ноль")
else:
    print("Отрицательное")

