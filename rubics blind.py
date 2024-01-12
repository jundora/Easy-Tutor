
import tkinter
import random
FONT=("メイリオ", 30)
from tkinter import Y, Tk,Label

questions= [
    {"Q":"rubics/あ.png", "a":"あ"},
    {"Q":"rubics/い.png", "a":"い"},
    {"Q":"rubics/う.png", "a":"う"},
    {"Q":"rubics/え.png", "a":"え"},
    {"Q":"rubics/か.png", "a":"か"},
    {"Q":"rubics/き.png", "a":"き"},
    {"Q":"rubics/く.png", "a":"く"},
    {"Q":"rubics/け.png", "a":"け"},
    {"Q":"rubics/さ.png", "a":"さ"},
    {"Q":"rubics/し.png", "a":"し"},
    {"Q":"rubics/す.png", "a":"す"},
    {"Q":"rubics/せ.png", "a":"せ"},
    {"Q":"rubics/ち.png", "a":"ち"},
    {"Q":"rubics/つ.png", "a":"つ"},
    {"Q":"rubics/て.png", "a":"て"},
    {"Q":"rubics/な.png", "a":"な"},
    {"Q":"rubics/に.png", "a":"に"},
    {"Q":"rubics/ぬ.png", "a":"ぬ"},
    {"Q":"rubics/ね.png", "a":"ね"},
    {"Q":"rubics/り.png", "a":"り"},
    {"Q":"rubics/る.png", "a":"る"},
    {"Q":"rubics/れ.png", "a":"れ"},
]



def question():
    answer.config(state="normal") 
    global correct
    correct=random.randint(0,len(questions)-1)
    q_image["image"]=questions[correct]["img"]

    q_image.update()
    result["text"]="答え↓"
    answer.delete(0,10)
    result.update()
    
x=0
y=0
def judge():
    
    seikai=questions[correct]["a"]
    global x
    global y
    
    if answer.get().strip()==seikai:
        result["text"]="正解"
        
        x+=1
        
        renzoku["text"]="連続正解数 "+str(x)
        
    elif len(answer.get())==0:
        pass
    elif answer.get().strip()!=seikai:
        result["text"]=f"不正解({seikai})"
        x*=0
        


    answer.config(state="disabled")   
    answer.delete(answer.index("end") - 1)
        

    result.update( )
 

def clear_text():
   answer.delete()


root=tkinter.Tk()
root.title("rubiks blind")
root.geometry("400x600")



for img in questions:
     img["img"]=tkinter.PhotoImage(file=img["Q"])


correct=random.randint (0,len(questions)-1)

renzoku=tkinter.Label(root, text="連続正解数"+str(x), font=FONT)
renzoku.pack(pady=10)
q_image=tkinter.Label(root, image =questions[correct]["img"])
q_image.pack()

result=tkinter.Label(root, text="答え↓", font=FONT)
result.pack()
answer=tkinter.Entry(root, width=15, font= FONT)
answer.pack(pady=10)


root.bind('<Return>',lambda event:judge())
    


arrow=root.bind('<Right>',lambda event:question())
arrow=root.bind('<Left>',lambda event:question())
arrow=root.bind('<Up>',lambda event:question())
arrow=root.bind('<Down>',lambda event:question())



ansbtn=tkinter.Button(root, text="解答",font=FONT,command=judge)
ansbtn.pack(pady=10)
nextbtn=tkinter.Button(root, text="次→",font=FONT, command= question)
nextbtn.pack(pady=10)

root.mainloop()
