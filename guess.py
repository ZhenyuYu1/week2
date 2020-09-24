correct_num = 39
guessed_num = int(input("Enter your guess (1-100): "))
if guessed_num == correct_num:
    print("You guessed the correct number! The number was:",correct_num)
elif guessed_num > correct_num:
    print("You guessed too high!. Try guessing lower.")
elif guessed_num < correct_num:
    print("You guessed too low!. Try guessing higher.")
else:
    print("Please enter a number 1-100.")