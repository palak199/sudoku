import tkinter as tk
from tkinter import Entry
lst=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
root=tk.Tk()
root.title("sudoku solver")
canvas=tk.Canvas(root,height=100,width=100)
canvas.pack()
height = 4
width = 4
b=[]
for i in range(height): #Rows
    for j in range(width): #Columns
        b= Entry(canvas, width=10)
        b.grid(row=i, column=j)
        b.insert(0, lst[i][j])
        

    
    
#button = tk.Button(root, text="get", width=10, command=callback)
#button.pack()

root.mainloop()

