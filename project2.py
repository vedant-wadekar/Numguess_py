import random
random = random.randint(1,100)

# using for loop
i=0
for i in range(1,100):
    num = int(input("Guess any number in between 1 to 100: "))    
    if(num < random):
        print("Greater number")
    elif(num > random):
        print("Lower number")
    else:
        print(f"Congrats correct number in {i} attempts\n\n")
        break


    # Using while loop
i=0
num =1000
while(num != random):
    i+=1
    num = int(input("Enter the number: "))
    if(num < random):
        print("Enter Greater number")
    elif(num > random):
        print("Enter smaller number")

else:
    print(f"!!!Congrats!!!\n you have gussed number in {i} attempts")