from tkinter.messagebox import YES


print("Welcome To My Computer Quiz!")

playing = input("Do You Want To Play The Game? ")

if playing.lower() != "yes":
    quit()

print("Okay Lets Play! :) ")
score = 0
answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("You Got " + str(score) + " questions correct! ")
print("You Got " + str((score / 4) * 100) + "%. ")
