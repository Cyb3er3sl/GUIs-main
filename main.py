import tkinter as tk

window = tk.Tk()

from die import Die
from scorecard import Scorecard

scorecard = Scorecard()

def roll_dice(dice:list[Die]):

    for die in dice:
        if die.can_roll.get():
            die.roll()
        




header = tk.Label(window, text="Yahtzee")
header.grid(column=0, row = 0)

dice = []
dice_labels = []
for i in range(5):    
    label = tk.Label(window)
    label.grid(column=i, row=2)
    dice.append(Die(i, label))



check_button_0 = tk.Checkbutton(window, text="Keep", onvalue=0, offvalue=1, variable=dice[0].can_roll)
check_button_0.grid(column=0, row=3)

check_button_1 = tk.Checkbutton(window, text="Keep", onvalue=0, offvalue=1, variable=dice[1].can_roll)
check_button_1.grid(column=1, row=3)

check_button_2 = tk.Checkbutton(window, text="Keep", onvalue=0, offvalue=1, variable=dice[2].can_roll)
check_button_2.grid(column=2, row=3)

check_button_3 = tk.Checkbutton(window, text="Keep", onvalue=0, offvalue=1, variable=dice[3].can_roll)
check_button_3.grid(column=3, row=3)


check_button_4 = tk.Checkbutton(window, text="Keep", onvalue=0, offvalue=1, variable=dice[4].can_roll)
check_button_4.grid(column=4, row=3)



button1 = tk.Button(window, 
                    text="Roll",
                    command=lambda: roll_dice(dice))
button1.grid(column=2, row=4)


#######################Ones########################
ones_score = tk.IntVar()
 
def use_ones(dice: list[Die]):
    dice_vals = [die.value for die in dice]    
    score = scorecard.score_ones(dice_vals)
    ones_score.set(score)
 
ones_button = tk.Button(window, text="ones", command=lambda: use_ones(dice))
ones_button.grid(column=0, row=5)
ones_label = tk.Label(window, textvariable=ones_score)
ones_label.grid(column=1, row=5)
 
 
 
 
############Full House########################
full_house_score = tk.IntVar()
full_house_button = tk.Button(window, text="Full House", command=lambda: use_full_house(dice))
 
def use_full_house(dice: list[Die]):
    dice_vals = [die.value for die in dice]    
    score = scorecard.score_full_house(dice_vals)
    full_house_score.set(score)
    full_house_button.config(state=tk.DISABLED)
 
 
full_house_button.grid(column=3, row=5)
full_house_label = tk.Label(window, textvariable=full_house_score)
full_house_label.grid(column=4, row=5)

window.mainloop()

