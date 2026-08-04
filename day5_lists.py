
# Создаём список героев
heroes = ["Purge", "Reaver", "Specter", "Bastion"]

# Выводим каждого по отдельности
print(heroes[0])
print(heroes[1])
print(heroes[2])
print(heroes[3])

# Узнаём, сколько героев
print ("Всего героев:", len(heroes))

# Добавляем нового героя
new_hero = input("Введи имя нового героя: ")
heroes.append(new_hero)

# Смотрим, что получилось
print("Обновлённый список героев:")
print(heroes)


# Выводим первого и последнего
print("Первый герой:", heroes[0])
print("Последний герой:", heroes[-1])   # -1 всегда означает последний элемент

weapons = ["Plasma Rifle", "Railgun", "Shotgun Blaster", "EMP Cannon"]
print("Всего оружия: ",len(weapons))
