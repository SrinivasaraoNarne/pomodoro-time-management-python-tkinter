from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None


def start_timer():
    global reps
    global tick
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_secs)
        timer.config(text="Break", fg=RED)
        marks.config(text=tick)
    elif reps % 2 == 1:
        count_down(work_secs)
        timer.config(text="Work", fg=GREEN)
        tick += "✔"
    else:
        count_down(short_break_secs)
        timer.config(text="Break", fg=PINK)
        marks.config(text=tick)


def restart():
    window.after_cancel(my_timer)
    canvas.itemconfig(canvas_text, text=f"25:00")
    timer.config(text="Timer", fg=GREEN)
    marks.config(text="")
    global reps
    reps = 0


def count_down(count):
    minutes = count//60
    seconds = count % 60
    canvas.itemconfig(canvas_text, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


window = Tk()
window.title("Pomodoro")
window.minsize(width=500, height=400)
window.config(padx=100, pady=50, background=YELLOW)

canvas = Canvas(width=204, height=224, background=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image((103, 112), image=tomato)
canvas_text = canvas.create_text((102, 132), text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

timer = Label(text="Timer", font=(FONT_NAME, 40, "italic"), fg=GREEN, background=YELLOW, highlightthickness=0)
timer.grid(row=1, column=2)

start = Button(text="Start", width=10, height=2, command=start_timer)
start.grid(row=3, column=1)

reset = Button(text="Reset", width=10, height=2, command=restart)
reset.grid(row=3, column=3)

tick = ""
marks = Label(text=tick, fg=GREEN, font=(FONT_NAME, 20, "bold"), background=YELLOW, highlightthickness=0)
marks.grid(row=4, column=2)

window.mainloop()
