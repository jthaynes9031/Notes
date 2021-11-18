#Data Types

#String
welcome = 'hey'
print(welcome)

#Subscripting
print("Hello"[0])
#should return 'H'
print("Hello"[1])
#should return 'e'
print("Hello"[4])
#should return 'o'

#Integer
print(123 + 456)
print(123_456_789)

#Float
print(3.14159)

#Boolean 
yes = True
no = False

#Type Error
num_char = len(input("What is your name?"))
#print("Your name has" + num_char + " characters.") #this line Breaks 

print(type(num_char))

#type casting or coversion
new_num_char = str(num_char)
print("your name has " + new_num_char + " Characters.") #this line works


#exercise mini project
two_digit = input("Type a two digit number:")
first_digit = two_digit[0]
second_digit = two_digit[1]
result = int(first_digit) + int(second_digit)
print(result)
#takes the 2 digit number and seperate the digits then adds them to together and returns sum
#Example: (34) 3 + 4 = 7

#Operations
3+5
5-2
3*3
6/3
2**3 # 2 * 2 * 2
#PEMDAS
# ()
# **
# * /
# + - 

print(3 * 3 + 3 / 3 - 3)

#Mini App BMI calculator
height = input("enter your height in feet:")
weight = input("enter your weight in lbs:")
result = float(weight) / float(height) * float(height)
bmi_asInt = int(result)
print(bmi_asInt)


#Number Manipulation

#rounding
print(round(8 / 3,2))
#rounds number to 2 decimal places


#Excercise 3
age = input("What is your current age?")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days = years_remaining * 365
weeks = years_remaining * 52
months = years_remaining * 12
remaining ="you have {0} days remaining or {1} weeks remaining or {2} weeks remaining".format(days,weeks,months)
print(remaining)