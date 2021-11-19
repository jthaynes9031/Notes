#If statements
print("welcome to the rollercoaster")
height = int(input("type your Hieght in cm "))

#if statements rely on indentation like below
#requires boolean
if height < 120:
    print("cannot ride")
else:
    print("can ride")

#comparison Operators
# < greater than
# > less than
# <= greater than or equal to
# >= less than or equal to
# == equal to
# != not equal to


#odd or even
number = int(input("Which number do you want to check "))
if number / 2 == 1:
    print("this number is Even !")
else:
    print("this number is odd")


#Nested if's
#taking previous example
print("welcome to the rollercoaster")
height = int(input("type your Hieght in cm "))

#if statements rely on indentation like below
#requires boolean
if height > 120:
    print("can ride")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("please pay $7 ")
    else:
        print("please pay $12")
else:
    print("cannot ride")



#BMI 2.0
height = float(input("enter your height in m:"))
weight = float(input("enter your weight in kg:"))
bmi = round(weight / height **2)
if bmi < 18.5:
    print(f"your bmi is {bmi}, you are underweight")
elif bmi < 25:
    print(f"your bmi is {bmi}, you have normal weight")
elif bmi < 30:
    print(f"your bmi is {bmi}, you are overweight")
elif bmi < 35:
    print(f"your bmi is {bmi}, you are obese")
else:
    print(f"your bmi is {bmi} , you are clinically obese")


#Pizza Order
print("Welcome to python pizza Deleveries")
size = input("What size pizza do you want ? S, M, L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
price = 0
if size == 'S':
    price += 15
elif size == 'M':
    price += 20
elif size == 'L':
    price += 30

if add_pepperoni == 'Y':
    if size == 'S':
        price += 2
else:
    price += 3


if extra_cheese == 'Y':
    price += 1

print(price)

#Logical operators uses or and and 