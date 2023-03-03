from tkinter import *
from tkinter import messagebox
import pandas
import random
import shutil
import os

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
ANSWERING = 3
next_word = ""
translation = ""
french_csv = pandas.read_csv("french_words.csv")
rep = 0

word_list = []
for index, rows in french_csv.iterrows():
    my_list = [rows.French, rows.English]
    word_list.append(my_list)
try:
    french_copy_csv = pandas.read_csv("french_copy.csv")
except FileNotFoundError:
    shutil.copy('french_words.csv', 'french_copy.csv')


# reset
def reset():
    if os.path.exists("french_copy.csv"):
        os.remove("french_copy.csv")
        shutil.copy('french_words.csv', 'french_copy.csv')
    else:
        shutil.copy('french_words.csv', 'french_copy.csv')
 

def start():

    clicked()


# ____wrong____#

def wrong():
    global rep
    if rep != 0:
        clicked()
    rep = 1


# ____correct____#
def correct():
    global next_word
    global translation
    global word_list
    global rep
    global french_copy_csv
    if rep != 0:
        clicked()
    update_df = word_list
    new_df = pandas.DataFrame(update_df, columns=['French', 'English'])
    new_df.to_csv("french_copy.csv")
    rep = 1


def clicked():
    global next_word
    global translation
    global word_list
    next_word_index = random.randint(0, len(word_list))
    next_word = word_list[next_word_index][0]
    translation = word_list[next_word_index][1]
    countdown(ANSWERING)
    del word_list[next_word_index]


def countdown(count):
    global next_word
    global translation
    canvas.itemconfig(word, text=next_word)
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        canvas.itemconfig(word, text=translation)


###____ UI_____###

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ______FRONT CARD________#
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="card_front.png")
canvas.create_image(400, 265, image=front_card_img)
canvas.grid(row=0, column=0, columnspan=2)

lang_text = canvas.create_text(400, 150, text="French", font=(FONT_NAME, 40, "italic"), fill="black")

word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"), fill="black")

start_img = PhotoImage(file="start.png")
start_button = Button(image=start_img, highlightthickness=0, borderwidth=0, command=start, bg=BACKGROUND_COLOR)
start_button.grid(row=1, column=2)

wrong_img = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=wrong)
wrong_button.grid(row=1, column=0)

correct_img = PhotoImage(file="right.png")
correct_button = Button(image=correct_img, highlightthickness=0, borderwidth=0, command=correct)
correct_button.grid(row=1, column=1)

reset_img = PhotoImage(file="reset.png")
reset_button = Button(image=reset_img, highlightthickness=0, borderwidth=0, command=reset, bg=BACKGROUND_COLOR)
reset_button.grid(row=0, column=2)

window.mainloop()
