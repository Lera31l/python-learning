
name= (input("Введи имя: "))
print("Привет", name)

# Список героев
heroes = ["Purge", "Reaver", "Specter", "Bastion"]

# Список стартового оружия (порядок должен совпадать с героями)
weapons = ["Plasma Rifle", "Railgun", "Nano Swarm Launcher", "EMP Cannon"]

print("=== Добро пожаловать в Void Cleaner ===")
print("Доступные герои:")

# Показываем героев с номерами
print("1.", heroes[0])
print("2.", heroes[1])
print("3.", heroes[2])
print("4.", heroes[3])

# Игрок выбирает героя
choice = input("Выбери номер героя (1-4): ")
choice = int(choice)

# Проверяем, правильный ли номер
if choice >= 1 and choice <= 4:
    hero_index = choice - 1          # потому что список начинается с 0
    selected_hero = heroes[hero_index]
    selected_weapon = weapons[hero_index]

    print("Ты выбрал героя:", selected_hero)
    print("Стартовое оружие:", selected_weapon)

    # Спрашиваем про NeuroShards
    shards = input("Сколько NeuroShards потратить на улучшение оружия? ")
    shards = int(shards)

    if shards >= 50:
        print("Оружие успешно улучшено!")
        print(selected_hero, "готов к зачистке сектора с улучшенным", selected_weapon)
    else:
        print("Недостаточно NeuroShards. Нужно минимум 50.")
        print(selected_hero, "выходит в сектор со стандартным оружием.")
else:
    print("Ошибка! Такого героя нет.")

