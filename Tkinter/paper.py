
import random
from tkinter import *
window = Tk()
window.geometry("400x350")
window.configure(bg="#131417")
window.title("Rock Paper Scissor")
# now creating user and computer as player
user_score = 0
comp_score = 0
user_choice = ""
comp_choice = ""
# now creating methods
# choice to number


def choice_to_number(choice):
    rps = {"rock": 0, "paper": 1, "scissor": 2}
    return rps[choice]


def number_to_choice(number):
    rps = {0: "rock", 1: "paper", 2: "scissor"}
    return rps[number]

# creating random computer choice


def random_computer_choice():
    return random.choice(["rock", "paper", "scissor"])
# now creating the score count method



def result(human_choice, comp_choice):
    global user_score
    global comp_score
    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)
    if (user == comp):
        print("Tie")
    elif((user-comp) % 3 == 1):
        print("You Win!!")
        user_score += 1
    else:
        print("Computer Wins")
        comp_score += 1

# now creating methods for buttons


def Rock():
    global user_choice
    global comp_choice
    user_choice = "rock"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)


def Paper():
    global user_choice
    global comp_choice
    user_choice = "paper"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)


def Scissor():
    global user_choice
    global comp_choice
    user_choice = "scissor"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)


# creating buttons
btn1 = Button(text="  Rock  ", width=10, height=4,
                 bg="#abbccc", command=Rock)

btn1.grid(row=1, column=0, padx=3, pady=3)

btn2 = Button(text="  Paper  ", width=10, height=4, bg="#fffaaa", command=Paper)

btn2.grid(row=1, column=1, padx=3, pady=3)

btn3 = Button(text="  Scissor  ", width=10,
                 height=4, bg="#67aaa2", command=Scissor)

btn3.grid(row=1, column=2, padx=3, pady=3)



window.mainloop()
