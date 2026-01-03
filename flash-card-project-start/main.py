from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_word={}
to_learn={}


try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orig_data=pandas.read_csv("data/french_words.csv")
    to_learn=orig_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

def next_card():
    global current_word,flip_timer

    if len(to_learn)==0:
        frt_pic.itemconfig(fr_title, text="Done", fill="black")
        frt_pic.itemconfig(fr_word, text="All words Learned", fill="black")
        frt_pic.itemconfig(card_bg, image=frt_image)
        windows.after_cancel(flip_timer)
        return

    windows.after_cancel(flip_timer)
    current_word=random.choice(to_learn)
    frt_pic.itemconfig(fr_title,text="French",fill="black")
    frt_pic.itemconfig(fr_word,text=current_word["French"],fill="black")
    frt_pic.itemconfig(card_bg, image=frt_image)
    flip_timer=windows.after(3000,flip_card)


def flip_card():
    global current_word
    frt_pic.itemconfig(fr_title,text="English",fill="white")
    frt_pic.itemconfig(fr_word, text=current_word["English"], fill="white")
    frt_pic.itemconfig(card_bg,image=bg_image)

def is_known():
    to_learn.remove(current_word)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()



windows=Tk()
windows.title("Flash cards captstone project")
windows.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=windows.after(3000,flip_card)
#Flash cards bg


frt_image=PhotoImage(file="./images/card_front.png")
bg_image=PhotoImage(file="images/card_back.png")
frt_pic=Canvas(width=800,height=526,highlightthickness=0)
card_bg=frt_pic.create_image(400,263,image=frt_image)
frt_pic.config(bg=BACKGROUND_COLOR,highlightthickness=0)
frt_pic.grid(column=0,row=0,columnspan=2)
fr_title=frt_pic.create_text(400,150,text="",font=("Arial",35,"italic"))
fr_word=frt_pic.create_text(400,263,text="",font=("Arial",60,"bold"))



#To button either correct or wrong
cor_img= PhotoImage(file="./images/right.png")
corr_but=Button(image=cor_img,bg=BACKGROUND_COLOR,highlightthickness=0,width=100,height=100,command=is_known)

corr_but.grid(column=1,row=1)

wrong_img= PhotoImage(file="./images/wrong.png")
wrong_but=Button(image=wrong_img,bg=BACKGROUND_COLOR,highlightthickness=0,width=100,height=100,command=next_card)

wrong_but.grid(column=0,row=1)


next_card()



windows.mainloop()