#Data Types

#string

print("Hello"[0])
print("123" + "345")

#integer

print(123 + 345)

#float

print(3.14)

#boolean

True
False

num_char = len(input("What is your name?\n"))
#print("Your name has" + num_char + "characters.") - выдаст ошибку
print(type(num_char))
new_num_char = str(num_char)
print(type(new_num_char))
print("Your name has " + new_num_char + " characters.")

#На входе получаем  двузначное число и печатаем сумму его цифр
two_digit_number = input("Type a two digit number: ")
a = int(two_digit_number[0])
b = int(two_digit_number[1])
print(a + b)

# Математические операции
# 2+3 -
# 3-2
# 3/2
# 3*2
# 2**3 = 2*2*2
# Порядок выполнения действий () , ** , * / , + - 

#Калькулятор веса
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = int(weight)/float(height)**2
bmi_as_int = int(bmi)
print(int(bmi_as_int))

result = 4/2
result /=2
score = 0
score +=1

#f-String - позволяет выводить различные типы данных
print(f"your score is {result}")

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_int = int(age)
age_lost = 90-age_int
days = age_lost*365
weeks = age_lost*52
months = age_lost*12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")

#Если счет составил $150.00, разделенный на 5 человек, с 12% чаевых. 

#Каждый человек должен заплатить (150,00 / 5) * 1,12 = 33,6
#Отформатируйте результат с точностью до 2 знаков после запятой = 33,60

#Совет: Существует два способа округления числа. Возможно, вам придется немного погуглить, чтобы решить эту проблему.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
would = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip = would / 100
result = (bill / people) + (bill / people) * tip
print(f"Each person should pay: ${round(result, 2)}")

