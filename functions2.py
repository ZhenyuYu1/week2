##def subtract_seven_and_add_eight(x):
    ##print("We are inside this other method")
    ##return x - 7 + 8

##def add_seven(num):
    ##print("We are inside of the add_seven()")
    ##return num + 7

##def large_multiple (x, y):
    ##result = x*y
    ##if result > 50:
        ##return True
    ##else:
        ##return False

##def main():
    ##print("We are inside of the main function right now...")
    ##print(add_seven(0))
    ##y = subtract_seven_and_add_eight(4)
    ##print(y)
    ##print(large_multiple(2, 10))
    
##main()

##def over_budget(subs, groc, phone, rent, budget):
    ##total_expenses = subs + groc + phone + rent
    ##if total_expenses > budget:
        ##print("You're in debt...")
    ##elif total_expenses > (.8*budget):
        ##remaining_budget = budget - total_expenses
        ##print("You have", remaining_budget, "leftover.")

##def main():
    ##print("We are inside of the main function right now...")
    ##over_budget(200,200,200,201,1000)

##main()

##def twice_as_large(num1, num2):
    ##if num1 >= (num2 * 2):
        ##return True
    ##else:
        ##return False
    ##return num1 > (num2*2)

##def main():
    ##print(twice_as_large(2,2))

##main()

##def calc_win_perc(wins, losses):
    ##total_games = wins + losses
    ##won_games = wins/total_games
    ##return won_games

##def main():
    ##print(calc_win_perc(10,20))

##main()

def average(num1, num2, num3, num4, num5, num6):
    return (num1 + num2 + num3 + num4 + num5 + num6)/6

def main():
    print(average(1,2,3,4,5,6))

main()