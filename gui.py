import tkinter as tk
from tkinter import Entry

root=tk.Tk()
root.title("sudoku solver")
canvas=tk.Canvas(root,height=100,width=100)
canvas.pack()
height = 4
width = 4
b=matrix=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def result():
    print("i")

'''for i in range(height): #Rows
    for j in range(width): #Columns
        b[i][j]= Entry(canvas, width=10)
        b[i][j].grid(row=i, column=j)
        b[i][j].insert(0, lst[i][j])
    '''

def callback():
    for i in range(4):
        for j in range(4):
            t=b[i][j].get()
            if t!='':
                matrix[i][j]=int(t)
            else:
                matrix[i][j]=0
 
               

def make_matrix():
    for i in range(4):
        for j in range(4):
            b[i][j]= Entry(canvas, width=10)
            b[i][j].grid(row=i, column=j)
            #print(b[i][j].get())
    
    
make_matrix()    
button = tk.Button(root, text="get", width=10, command=callback)
button.pack()

root.mainloop()

