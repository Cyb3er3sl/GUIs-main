import tkinter as tk

window = tk.Tk()

from die import Die
from scorecard import Scorecard

scorecard = Scorecard()

def roll_dice(dice:list[Die]):

    for die in dice:
        if die.can_roll.get():
            die.roll()
        
    scorecard.score_full_house(dice)



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

window.mainloop()

