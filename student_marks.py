import tkinter as tk
import matplotlib.pyplot as plt


root = tk.Tk()
root.title("Student Marks Display")
root.geometry("800x800")

subjects=["science","chem","maths"]
marks={}

input_frame=tk.Frame(root)
input_frame.grid(row=1,column=0)

for subject in subjects:
    marks[subject]=tk.IntVar(value=0)

for i,subject in enumerate(subjects):
    tk.Label(input_frame,text=f"mark of {subject}").grid(row=i,column=0)
    tk.Entry(input_frame,textvariable=marks[subject]).grid(row=i,column=1)

def gradeFinding(marks):
    if marks >=90 :
        return "A+"
    elif marks < 90 and marks >= 80:
        return "A"
    elif marks < 80 and marks >= 70:
        return "B+"
    else:
        return "Fail"

def generate_report():
    print(marks['science'].get())
    print(marks['chem'].get())
    print(marks['maths'].get())

    total_marks=0
    result_text=""

    for subject in subjects:
        total_marks+=float(marks[subject].get())
        result_text+=f"marks of {subject} ({gradeFinding(marks[subject].get())}) = {marks[subject].get()} \n"
    
    result_text+=f"total Marks = {total_marks}"
    print(total_marks)
    result_label.config(text=result_text)
    print("in here")

tk.Button(input_frame,text="Generate Report",command=generate_report).grid(row=4,column=0)
result_label=tk.Label(input_frame,text="Result")
result_label.grid(row=5,column=0)



root.mainloop()
