age = 23
if age >= 18:
    print("You are allowed to vote!")
else:
    print("You are not allowed to vote...yet")

if age >= 18:
    print("You are allowed to watch R rated movies.")
elif age >= 13:
    print("You are allowed to watch pg13 movies.")
else:
    print("You are under the age of 13... sorry.")
    
gravity = 9.81
if gravity == 9.81:
    print("You are on Earth.")
else:
    print("You are not on Earth.")

budget = 5000
spendings = 3000

if(budget - spendings) > 1000:
    budget = 6000
    
print(budget)

secret_message = "missionbit"
name = input("Enter your name: ")
lname = input("Enter your last name: ")
age = 25

if name == "Zhenyu" and lname == "Yu":
    print("Welcome Zhenyu! The secret message is", secret_message".")
elif name == "Hunter" or lname == "Lee":
    print("Hunter go home! Stop trying to get my secret message.")
elif age > 25:
    print("You are old enough to see the secret message. Here you go: ", secret_message")
elif (age == 45 or lname == "Yu")
    print("You can see the program.")
else:
    print("Stop trying to hack my program...")