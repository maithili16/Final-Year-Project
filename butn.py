# Simple Quiz GUI app
# Create a question and multiple choice options of which one is correct
# When correct option is clicked a message displays that option is correct!
import tkinter
from tkinter import *
import sys
import os
import time

# keep the question in a separate json file
q = [
    "1) x = ['ab', 'cd']. print(len(list(map(list, x)))))).What will be the output of the following Python code?",
    "2) Which of these is not a core data type?",
    "3) What data type is the object.L = [1, 23, ‘hello’, 1]?",
    "4) In the following options which are python libraries which are used for data analysis and scientific computations?",
    "5) 2**2**3**1.What is the value of this expression?",
]

options = [
    ["2", "4", "Error", "None of the mentioned"],
    ["Lists","Dictionary","Tuples","Class"],
    ["List","Dictionary","Tuples","Array"],
    ["Numpy","Scipy","Pandas","All of the above"],
    ["12","64","126","256"]
]

a = [3, 4,1,4,4]

# start_time = time.time()
# end_time = time.time()
class Quiz:
    def __init__(self, master):
        self.opt_selected = IntVar()
        self.qn = 0
        self.start_time = time.time()
        self.end_time = time.time()
        self.correct = 0
        self.ques = self.create_q(master, self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        self.button = Button(master, text="Back", command=self.back_btn, padx=30)
        self.button.pack(side=RIGHT)
        self.button = Button(master, text="Next", command=self.next_btn,padx=30)
        self.button.pack(side=RIGHT)

    def create_q(self, master, qn):
        w = Label(master, text=q[qn],font='Helvetica 14 bold')
        w.pack(side=TOP)
        return w

    def create_options(self, master, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="foo", variable=self.opt_selected, value=b_val+1, font='Helvetica 14 bold',padx=50,pady=20)
            b.append(btn)
            btn.pack(side=TOP, anchor="w")
            b_val = b_val + 1
        return b

    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def check_q(self, qn):
        if self.opt_selected.get() == a[qn]:
            if(qn == 0):
                print("You are strong in basic python")
            elif(qn == 1):
                print("You are strong in topic datas tructures")
            elif(qn == 2):
                print("You are strong in topic objects and classes")
            elif(qn == 3):
                print("You have knowledge about various python libraries")
            elif(qn == 4):
                print("You have knowledge about exponential functions")
            return True
        else:
            if(qn == 0):
                print("You are weak in basic python")
            elif(qn == 1):
                print("You are weak in topic data structures")
            elif(qn == 2):
                print("You are weak in topic objects and classes")
            elif(qn == 3):
                print("Please improve your knowledge about various libraries")
            elif(qn == 4):
                print("Please improve your knowledge in basic funtionalities")
            return False
        return False

    def print_results(self):
        print("Score: ", self.correct, "/", len(q))
        sys.exit("Error message")


    def back_btn(self):
        print("go back")

    def next_btn(self):
        self.end_time = time.time()
        seconds_spent = self.end_time - self.start_time
        # take timestamp for seeing the endTime of question(x)
        flag = False
        if self.check_q(self.qn):
            print("Correct")
            self.correct += 1
            flag = True
        else:
            print("Wrong")
        self.qn = self.qn + 1
        with open("timestamp_data_file.txt", "a") as data:
            data.write(str(self.start_time)+","+str(self.end_time)+","+str(seconds_spent)+","+str(flag)+"\n")
        self.start_time = time.time()
        if self.qn >= len(q):
            self.print_results()
        else:
            self.display_q(self.qn)
        

root = Tk()
label = tkinter.Label(root, text = "WELCOME TO ONLINE TEST!!!",font='Helvetica 18 bold',pady=100).pack()
root.geometry("1500x650")
# Start capturing video and capture startTime of ques1
# start_time = time.time()
app = Quiz(root)
root.mainloop()

# TODO: Shuffle answers
# TODO: Display the answer on the GUI
