import random

def roll_dice():
    
    dice_drawing  ={
        1:{
            " _________",
            "|    1    |",
            "|    O    |",
            "|         |",
            "|_________|"
            
        },
        2:{
            " _________",
            "| O       |",
            "|    2    |",
            "|      O  |",
            "|_________|"
            
        },
        3:{
            " _________",
            "| O  3    |",
            "|    O    |",
            "|       O |",
            "|_________|"
            
        },
        4:{
            " _________",
            "|  O   O  |",
            "|    4    |",
            "|  O   O  |",
            "|_________|"
            
        },
        5:{
            " _________",
            "|  O 5 O  |",
            "|    O    |",
            "|  O   O  |",
            "|_________|"
            
        },
        6:{
            " ___________",
            "|  O     O  |",
            "|  O  6  O  |",
            "|  O     O  |",
            "|___________|"
            
        },
        
    }
    
    roll = input("Roll the dice? (Yes/No) : ")
    
    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
    
    print("dice rolled: {} and {}".format(dice1, dice2))
    
    roll = input("Roll again? (Yes/No): ")
    
roll_dice()    
