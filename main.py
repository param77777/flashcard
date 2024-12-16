from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("flashcard/words_to_learn")
except:
    original_data = pd.read_csv(r"C:\Users\tyt36\OneDrive\Desktop\All\GitDemo\flashcard\french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    windows.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image= card_front_img)
    flip_timer = windows.after(3000, func=flip_card)
    
def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    global current_card, to_learn
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("flashcard/words_to_learn", index=False)
    next_card()

windows = Tk()
windows.title("Flash Card")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = windows.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=r"C:\Users\tyt36\OneDrive\Desktop\All\GitDemo\flashcard\card_front.png")
card_back_img = PhotoImage(file=r"C:\Users\tyt36\OneDrive\Desktop\All\GitDemo\flashcard\card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel",40,"italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0,row=0, columnspan=2)


cross_image = PhotoImage(file=r"C:\Users\tyt36\OneDrive\Desktop\All\GitDemo\flashcard\wrong.png")
unknow_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknow_button.grid(column=0, row=1)


check_image = PhotoImage(file=r"C:\Users\tyt36\OneDrive\Desktop\All\GitDemo\flashcard\right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

windows.mainloop()
