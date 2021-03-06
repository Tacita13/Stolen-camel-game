
# Isamar López Rodríguez
# 26/10/15


import random

#Start

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your desert trek and out run the natives.")

done=False
miles=0
thirst=0
camelTiredness=0
nativeDistance = -20
canteen = 10
while not done:
#Main Menu
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    userChoice = input("Your choice? ")
    print (userChoice)

    if userChoice.upper() == "Q":
        done = True
    elif userChoice.upper() == "E":
        print("Miles traveled: ", miles)
        print("Drinks in canteen: ", canteen)
        print("The natives are %s miles behind you" %(nativeDistance))

    elif userChoice.upper() == "D":
        camelTiredness=0
        print ("The Camel is happy!")
        nativeDistance = random.randrange(7, 15)
    elif userChoice.upper() == "C":
        miles+=random.randrange(10, 21)
        print("You have traveled %s miles" %(miles))
        thirst+=1
        camelTiredness+= random.randrange(1,4)
        nativeDistance+=random.randrange(7, 15)
    elif userChoice.upper()=="B":
        miles+=random.randrange(5,13)
        print("You have traveled %s miles" %(miles))
        thirst+=1
        camelTiredness+=1
        nativeDistance+=random.randrange(7, 15)
    elif userChoice.upper() == "A":
        if canteen > 0:
            canteen-= 1
            thirst=0
        else:
            print("There is no more water in the canteen")

# Winning
    if miles >= 200:
        print ("You have successfully travled across the desert")
        print ("You won!")
        done = True

#Thirst
    if thirst > 6:
            print("You have died of thirst!")
            print ("Game over")
            done = True
    elif thirst > 4:
            print ("You are thirsty!")
            
#CamelTiredness
    if done == False:
        if camelTiredness > 8:
            print("Your camel is dead")
            print ("Game over")
            done=True
            
        elif camelTiredness > 5:
            print("Your camel is getting tired")

#nativeDistance
    if nativeDistance >= miles:
        print ("They caught you!")
        print ("Game over")
        done= True
    elif miles - nativeDistance < 15:
        print ("The natives are getting close!")

#Oasis
    if random.randrange(1,21) == random.randrange(1,21):
        print ("You have found an oasis!")
        canteen=10
        thirst=0
        camelTiredness=0
