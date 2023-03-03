from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checks = "✔"
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global checks
    global reps
    checks = ""
    window.after_cancel(my_timer)
    reps = 0
    timer_label.config(text="Timer", fg=GREEN)
    check_marks.config(text=checks)
    canvas.itemconfig(timer_text, text="00:00")



def start():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break😌", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short Break💆🏼", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work💪", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global checks
    global my_timer
    mins = int(count / 60)
    min_list = []
    for digit_str in str(mins):
        min_list.append(int(digit_str))
    if len(min_list) == 2:
        m10 = min_list[0]
        m1 = min_list[1]
    else:
        m10 = 0
        m1 = min_list[0]
    sec = count % 60
    sec_list = []
    for digit_str in str(sec):
        sec_list.append(int(digit_str))
    if len(sec_list) == 2:
        s10 = sec_list[0]
        s1 = sec_list[1]
    else:
        s10 = 0
        s1 = sec_list[0]

    canvas.itemconfig(timer_text, text=f"{m10}{m1}:{s10}{s1}")
    if count > 0:
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start()
        if reps % 2 == 0:
            check_marks.config(text=checks)
            checks = checks + "✔"


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# fg = GREEN for font
# for check mark paste it

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

start_button = Button(text="Start", command=start, borderwidth=0, highlightbackground=YELLOW)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", command=reset, highlightthickness=0, highlightbackground=YELLOW)
reset_button.grid(row=3, column=3)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=1, column=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
check_marks.grid(row=4, column=2)

window.mainloop()
