# print("Привет мир!")
# print("Привет программист!")
# print(2 + 2)
# print(10 / 3)

# name = 'Андрей'
# print(name)

# print('  Привет!'.strip())
# url = 'learn.python.ru'
# parts = url.split('.')
# print(parts)

# x = 2
# print(type(x))
# x = 'abc'
# print(type(x))
# print(x == None)

# v = input('Введите число от 1 до 10: ')
# print(int(v) + 10)

# print(bool(1))
# print(int(2.5))

boys = ["Alex", "Roma", "Vlad", "Sergei", 1, 3.14]
boys.append("Nikita")
boys.append("Nikita")
# print(boys)
# print(boys.count("Nikita"))
# print(boys[1:2])
# print(boys[-2:])
# print(boys[:-2])
# print(boys.index("Vlad"))
# boys.sort()
# print(boys)
print("Nikita" in boys)

del boys[1]
print(boys)
boys.remove("Nikita")
# только первое вхождение
print(boys)