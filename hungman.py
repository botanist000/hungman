import random


def hangman(word):
    wrong = 0
    stages = ["",
              "________",
              "|       ",
              "|   |   ",
              "|   0   ",
              "|  /|\  ",
              "|  / \  ",

              ]
    rletters = list(word)
    board =["_"]*len(word)
    win = False
    print("Welcome to hangman")
    while wrong<len(stages):
        msg = ("guess word")
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"

        else:
            wrong+=1

        print(" ".join(board))
        print("\n".join(stages[0:wrong]))

        if "_" not in board:
            print("you win!")
            print(" ".join(board))
            win = True
            break
    if not win:
            print("You lose")
            print("The answer is {}".format(word))

def rando():
    list =["cat","dog","rabbit","headgehog"]
    a = list[random.randint(0,3)]
    return a


hangman(rando())
