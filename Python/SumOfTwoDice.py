import random

def sum_of_two_dice():
    
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    
    total = die1 + die2
    
    
    print(f"The sum of the two dice is: {total}")


sum_of_two_dice()
