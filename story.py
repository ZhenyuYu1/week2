name = int(input("Please enter your name: "))

print("Hello", name,". You will embark on a new journey today.")

place = input("Would you like to go to the forest or beach?")
if place == "forest":
    print("You go to the forest and see magical creatures.")
elif place == "beach":
    print("You swim and see many fish.")
else:
    print("I guess you have not decided.")

