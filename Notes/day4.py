#Randomisation
import random

random_number = random.randint(1,50)
print (random_number)

#prints floats
#random_f = random.random(0,1)
#print(random_f)

#you can have different modules and by doing so is making another file and importing it to anoter
#make new file 
#import file in main.py

#heads or tails
heads_or_tails = int(input("type '1' for heads type '2' for 'tails'"))
h_f = random.randint(1,2)
if(h_f == heads_or_tails):
    print(h_f)
    print(f"you chose {heads_or_tails} you win")
else:
    print(h_f)
    print(f"you chose {heads_or_tails} you lose ")