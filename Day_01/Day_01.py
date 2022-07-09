print("Hello world!")

print("Hello world!\nHello world!\nHello world!")

print("Hello" + " " + "Oxana!")
#выводит приветствие по введеному имени
print("Hello " + input("What is your name? ") + "!")
#выводит количество букв в имени
print(len(input("What is your name? ")))

#Записывает в name введеное пользователем значение
name = input("What is your name? ")
print(name)
# print(len(input("What is your name? "))) =
name = input("What is your name? ")
lenght = len(name)
print(lenght)
# меняем переменые местами
a = input("a: ")
b = input("b: ")
c = a
a = b
b = c
print("a: " + a)
print("b: " + b)
# генератор названия группы
print("Welcome to the Band Name Generator.")
city = input("What's name of the city you grew up in?\n")
name = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + name)
