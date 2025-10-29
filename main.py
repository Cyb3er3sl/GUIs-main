import tkinter as tk
from tkinter import messagebox
from die import Die
from scorecard import Scorecard, CATEGORIES

class YahtzeeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Yahtzee Game")

        self.dice = [Die() for _ in range(5)]
        self.rolls_left = 3
        self.scorecard = Scorecard()

        self.dice_vars = [tk.StringVar(value="1") for _ in range(5)]
        self.hold_vars = [tk.IntVar(value=0) for _ in range(5)]
        self.roll_label = tk.Label(root, text=f"Rolls left: {self.rolls_left}")
        self.roll_label.pack()

        dice_frame = tk.Frame(root)
        dice_frame.pack(pady=10)
        for i in range(5):
            sub = tk.Frame(dice_frame)
            sub.pack(side=tk.LEFT, padx=5)
            tk.Label(sub, textvariable=self.dice_vars[i], font=("Helvetica", 24)).pack()
            tk.Checkbutton(sub, text="Hold", variable=self.hold_vars[i]).pack()

        tk.Button(root, text="Roll", command=self.roll).pack(pady=5)

        self.cat_var = tk.StringVar(value=CATEGORIES[0])
        tk.OptionMenu(root, self.cat_var, *CATEGORIES).pack(pady=5)
        tk.Button(root, text="Score Category", command=self.score_category).pack(pady=5)
        tk.Button(root, text="Show Scorecard", command=self.show_scorecard).pack(pady=5)

        self.roll()

    def roll(self):
        if self.rolls_left <= 0:
            messagebox.showinfo("No rolls left", "You must score before rolling again.")
            return
        for i, die in enumerate(self.dice):
            if not self.hold_vars[i].get():
                die.roll()
                self.dice_vars[i].set(str(die.value))
        self.rolls_left -= 1
        self.roll_label.config(text=f"Rolls left: {self.rolls_left}")

    def score_category(self):
        dice_values = [int(v.get()) for v in self.dice_vars]
        cat = self.cat_var.get()
        try:
            score = self.scorecard.set_score(cat, dice_values)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        messagebox.showinfo("Scored", f"You scored {score} points in '{cat}'.")
        self.reset_turn()

        if not self.scorecard.available_categories():
            total = self.scorecard.grand_total()
            messagebox.showinfo("Game Over", f"All categories scored!\nFinal Score: {total}")
            self.root.destroy()

    def reset_turn(self):
        self.rolls_left = 3
        for h in self.hold_vars:
            h.set(0)
        self.roll_label.config(text=f"Rolls left: {self.rolls_left}")
        self.roll()

    def show_scorecard(self):
        lines = [f"{cat}: {self.scorecard.scores[cat]}" for cat in CATEGORIES]
        lines.append(f"Total: {self.scorecard.grand_total()}")
        messagebox.showinfo("Scorecard", "\n".join(lines))

if __name__ == "__main__":
    root = tk.Tk()
    app = YahtzeeGame(root)
    root.mainloop()
