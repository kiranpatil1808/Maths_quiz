from tkinter import *
import random
from random import choice

root = Tk()
root.geometry("600x500")
root.title("Maths Quiz")

headingLabel= Label(root,text="Maths Quiz",font=("aerial",25))
headingLabel.grid(row=0,column=0)

question=StringVar()  #stores string value
answer=StringVar()
givenAnswer=StringVar()
score=IntVar()
questionNumber=IntVar()

def generateQuestion():


    global questionLabel
    global question,answer

    questionNumber.set(questionNumber.get()+1)

    number1=random.randint(1,10)
    number2=random.randint(1,10)

    operator=choice(["+","-","*","/"])

    question.set(str(number1)+operator+str(number2))
    answer.set(eval(question.get()))

    if questionLabel:
        questionLabel.destroy()

    questionLabel=Label(root,text=f"Question : {question.get()}",font=("aerial",20))
    questionLabel.grid(row=2,column=0)




def Checkanswer():

    global scoreLabel

    if questionNumber.get()>10:
        return

    global resultLabel
    if resultLabel:
        resultLabel.destroy()


    if str(answer.get())==givenAnswer.get():
        print("correct")
        score.set(score.get()+1)
        resultLabel=Label(root,text="correct",font=("aerial",20),fg="green")
        resultLabel.grid(row=6,column=0)

        scoreLabel=Label(root,text=f"Score : {score.get()}",font=("aerial",20),fg="black")
        scoreLabel.grid(row=7,column=0)

    else:
        print("incorrect")
        resultLabel=Label(root,text="incorrect",font=("aerial",20),fg="red")
        resultLabel.grid(row=6,column=0)

    if questionNumber.get()==10:
        scoreLabel.destroy()
        scoreLabel=Label(root,text=f"Final Score : {score.get()}",font=("aerial",20),fg="black")
        scoreLabel.grid(row=7,column=0)

    else: 
        generateQuestion()


def restart():
    global scoreLabel 
    scoreLabel.destroy()

    score.set(0)
    questionNumber.set(0)
    generateQuestion()

    scoreLabel=Label(root,text=f"Score : {score.get()}",font=("aerial",20),fg="black")
    scoreLabel.grid(row=7,column=0)


#Gui

questionScale=Scale(root,from_=0,to=10,orient=HORIZONTAL,length=400,variable=questionNumber)
questionScale.grid(row=1,column=0)

questionLabel=Label(root,text=question.get(),font=("aerial",20))
questionLabel.grid(row=2,column=0)

completequestionLabel=Label(root,text="10th question")
completequestionLabel.grid(row=1,column=1)

answerEntry=Entry(root,textvariable=givenAnswer,font=("Aerial",20),width=25)
answerEntry.grid(rows=3,column=0)

submitButton=Button(root,text="submit",font=("aerial",15),command=Checkanswer)
submitButton.grid(row=4,column=1)

resultLabel=Label(root,text="Result",font=("aerial",20),fg="black")
resultLabel.grid(row=6,column=0)

scoreLabel=Label(root,text=score.get(),font=("aerial",20),fg="black")
scoreLabel.grid(row=7,column=0)

restartButton=Button(root,text="Restart",font=("aerial",15),command=restart,width=35)
restartButton.grid(row=8,column=0)

generateQuestion()

print(question.get())
print(answer.get())


root.mainloop()