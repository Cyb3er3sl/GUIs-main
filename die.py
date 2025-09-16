
from PIL import ImageTk, Image
import random
import tkinter as tk

def crop_dice_images():
    image_path = "dice.jpg"
    spritesheet = Image.open(image_path)
    color = "gold"

    colors = {
        "red" : 0,
        "gold" : 1,
        "green": 2,
        "blue" : 3,
        "purple": 4,
        "gray" : 5
    }
    w, h = spritesheet.size
    dice_images = []

    for i in range(6):
        left = 0 + (i * w//6)
        top = 0 + (colors[color] * h//6)
        right = w//6* (1+i) #w // 6 + (i * w//6)
        bottom = h//6 + (colors[color] * h//6)

        red_die = spritesheet.crop((left, top, right, bottom))
        dice_images.append(ImageTk.PhotoImage(red_die))
    return dice_images

class Die:
    
    #IMAGES = dice_images
    def __init__(self, position, label):

        self.IMAGES = crop_dice_images()


        
        self.position = position
        self.value = None
        self.can_roll = tk.IntVar()
        self.image = None
        self.label = label
        

        
    def roll(self):
        self.value = random.randint(1,6)
        self.image = self.IMAGES[self.value -1] # Because index 0 has the picure with one dot
        print(self.position, self.value)
        if self.label:
            self.label["image"] = self.image
            self.label.grid(column=self.position, row=2)