age = 15
if age >= 18:
    print("You are allowed to watch R-rated movies.")
elif age >= 13:
    print("You are allowed to watch PG-13 movies.")
elif age >= 10:
    print("You are allowed to watch PG rated movies.")
elif age >= 7:
    print("You are allowed to watch G rated movies.")
else:
    print("You are too young to come to our movie theaters.")

secret_message = "SeCrEt MeSsAgE"
name = input("Enter your name: ")
if name == "Zhenyu" or name == "Zhenyu Yu":
    print("The secret message is:",secret_message.)
else:
    print("You are not allowed to see the secret message.")