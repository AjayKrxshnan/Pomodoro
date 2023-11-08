from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN =5
LONG_BREAK_MIN = 20
REPS=0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    REPS = 0
    tick.config(text="")
    label.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1

    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if REPS%2 != 0 and REPS<8:
        label["text"] = "Work"
        label.config(fg=GREEN)
        window.after(1000,timer_count,work_sec)

    else:
        if REPS==8:
            label["text"] = "Long Break"

            label.config(fg=RED)
            window.after(1000,timer_count,long_break_sec)
            tick["text"] += "✔"
            tick.config(fg="#A8DF8E")
        elif REPS<8 and REPS %2==0:
            label["text"] = "Break"
            label.config(fg=PINK)
            window.after(1000, timer_count, short_break_sec)
            tick["text"] += "✔"









# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def timer_count(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    if count>=0:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        timer =window.after(1000,timer_count,count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(320,300)
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=204,height=224,highlightthickness=0)
canvas.config(bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102,112,image=tomato_img)
timer_text=canvas.create_text(102,130,text="00:00",fill="White",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)

label=Label(text="Timer",font=(FONT_NAME,30,"bold"),fg=GREEN,bg=YELLOW)
label.config(pady=20)
label.grid(row=0,column=1)

tick=Label(text="",font=(FONT_NAME,20,"bold"),fg=RED,bg=YELLOW)
tick.grid(row=3,column=1)


start_button=Button(text="start",width=10,command=start_timer)

reset_button=Button(text="reset",width=10,command=reset_timer)
start_button.grid(row=2,column=0)
reset_button.grid(row=2,column=2)




window.mainloop()