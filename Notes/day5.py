#Playing with loops

student_scores = [ 78, 65, 89, 86, 55]

highSco = 0
for score in student_scores:
    if score > highSco:
        highSco = score
print(f"The Highest score in the class is: {highSco}")

#should be 89 
#loops through each element in list and compares scores to the next


# Range function
# for number in range(a,b)
#    print(number)

total = 0
for number in range(1,10):
    total += number
print(total)


#FizzBuzz
for number in range(1,100):
    if number % 3 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)