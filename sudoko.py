import tkinter as tk
from tkinter import Entry
from tkinter import messagebox
#for GUI version
def result_matrix(res_matrix):
    canvas2=tk.Canvas(root,height=100,width=100)
    canvas2.pack()
    for i in range(9): #Rows
        for j in range(9): #Columns
            b= Entry(canvas, width=10)
            b.grid(row=i, column=j)
            b.insert(0, res_matrix[i][j])

        


        
# def make_matrix(n):
#     matrix=[]
#     for i in range(n):
#         temp=[]
#         for j in range(n):
#             print ("add->",i,j,":",end="")
#             temp.append(int(input()))
#         matrix.append(temp)
#     return matrix
b=matrix=[[0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]]



def callback():
    
    for i in range(9):
        for j in range(9):
            t=b[i][j].get()
            
            if t!='' :
                if 0<int(t)<10:
                    matrix[i][j]=int(t)
                else:
                    exit
                         
            else:
                matrix[i][j]=0
            
    if solver(matrix):
         result_matrix(matrix)
    else:
        exit
        

      
   
def make_matrix(root,canvas):
    for i in range(9):
        for j in range(9):
            b[i][j]= Entry(canvas, width=5)
            b[i][j].grid(row=i, column=j)
    button = tk.Button(root, text="get", width=10, command=callback)
    button.pack()
    
    root.mainloop()

    
def column(matrix, i):
    return [row[i] for row in matrix]  

def sub_matrix(s_matrix,i,j):
    sm=[]
    i=i-i%3
    j=j-j%3
    for row in range(3):
        temp=[]
        for col in range(3):
            temp.append(s_matrix[row+i][col+j])
        sm.append(temp)
    return (sm)

def check_sub_matrix(sm,num):
    if not any(num in x for x in sm):
        return True
    else:
        return False
    
def check_row_matrix(row_matrix,num):
    if num not in row_matrix:
        return True
    else:
        return False
    

def check_col_matrix(col_matrix,num):
    if num not in col_matrix:
        return True
    else:
        return False
    
            
def find_zero(z_matrix):
    for i in range(9):
        for j in range(9):
            if z_matrix[i][j]==0:
                return (i,j)
            
    return None
                   
    
def solver(matrix):
        
    is_there=find_zero(matrix)
    if (not is_there):        
        return True
    else:    
        i,j=is_there
    
    for t in range(1,10):
        sm=sub_matrix(matrix,i,j)
        row_matrix=matrix[i]
        col_matrix=column(matrix,j)
                        
        if check_row_matrix(row_matrix,t) and check_col_matrix(col_matrix,t) and check_sub_matrix(sm,t):
                matrix[i][j]=t
                if(solver(matrix)):      
                    return True
                matrix[i][j]=0

    return False
                    
if __name__=="__main__":
    root=tk.Tk()
    root.title("sudoku solver")
    canvas=tk.Canvas(root,height=100,width=100)
    canvas.pack()    
    make_matrix(root,canvas) 
    




