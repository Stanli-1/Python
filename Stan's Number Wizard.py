#This a program to guess a number that the user has thought of
#it will continually guess new numbers and the user will say if the
#the number is higher, lower, or correct

#math to find the midle:
#round (a + b) / 2

#import time
print("Pick a number between 0 and 100")#this a promt for the user
#time.sleep(5)

#some sort of way to repeat:
#until number is correct:
#when number is correct:

haveWon = False # Boolean, either True or False
higher =100
lower = 0

while not haveWon: # loop until I haveWon
    calculation = round((lower + higher) / 2)
    print("is your number " + str(calculation))
    humanSays = input()
    if humanSays == "higher":
        # guess a higher number
        # guess a new number between last guess and the higher bound
        lower = calculation
    elif humanSays == "lower":
        # guess a lower number
        higher = calculation
    elif humanSays =="correct":
        # win
        print("Yayy, I won!")
        haveWon = True
    else:
        # in case somthing else happens
        pass
        
