import random
import tkinter as tk
# create window
window=tk.Tk()
window.geometry("400x400")
window.title("Rock-Paper-Scissors Game")
U_SCORE=0
COMP_SCORE=0
U_CHOICE=""
C_CHOICE=""
## CONVERT USER CHOICE TO NUMBER 
def ch_to_no(ch):
    rps={'rock':0,'paper':1,'scissor':2}
    return rps[ch]
def no_to_ch(no):
    rps={0:'rock',1:'paper',2:'scissor'}
    return rps[no]
def random_co_ch():
    return random.ch(['rock','paper','scissor'])


def result(human_ch,comp_ch):
    global U_SCORE
    global COMP_SCORE
    user=ch_to_no(human_ch)
    comp=ch_to_no(comp_ch)
    if(user==comp):
        print("Tie")
    elif((user-comp)%3==1):
        print("You win")
        U_SCORE+=1
    else:
        print("Comp Win")
        COMP_SCORE+=1
    text_area=tk.Text(master=window,height=12,width=30,bg="#FFFF99")
    text_area.grid(column=0,row=4)
    ans="Your choice: {uc} \n Comp Choice:{cc} \n Your SCore:{u} \n Comp score:{c}".format(uc=U_CHOICE,cc=C_CHOICE,u=U_SCORE,c=COMP_SCORE)
    text_area.insert(tk.END,ans)



def rock():
    global U_CHOICE
    global C_CHOICE
    U_CHOICE='rock'
    C_CHOICE=random_co_ch()
    result(U_CHOICE,C_CHOICE)

def paper():
    global U_CHOICE
    global C_CHOICE
    U_CHOICE='paper'
    C_CHOICE=random_co_ch()
    result(U_CHOICE,C_CHOICE)


def scissor():
    global U_CHOICE
    global C_CHOICE
    U_CHOICE='scissor'
    C_CHOICE=random_co_ch()
    result(U_CHOICE,C_CHOICE)


# lets build three buttons so that user can click them to play game
button1=tk.Button(text="Rock",bg="purple" ,command=rock)
button1.grid(column=0,row=1)

button2=tk.Button(text="paper",bg="skyblue" ,command=rock)
button2.grid(column=1,row=1)

button3=tk.Button(text="scissor",bg="purple" ,command=rock)
button3.grid(column=2,row=1)
 
 #finally run everything inside the window using the mainloop
window.mainloop()