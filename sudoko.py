
def show_matrix(matrix):
    for i in matrix:
        print(' '.join(str(i)))
        
def make_matrix(n):
    matrix=[]
    for i in range(n):
        temp=[]
        for j in range(n):
            print ("add->",i,j,":",end="")
            temp.append(int(input()))
        matrix.append(temp)
    return matrix
    
    
def column(matrix, i):
    return [row[i] for row in matrix]  

def sub_matrix(matrix,i,j):
    sm=[]
    i=i-1 if i%2==1 else i
    j=j-1 if j%2==1 else j
    for row in range(2):
        temp=[]
        for col in range(2):
            temp.append(matrix[row+i][col+j])
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
    
            
def find_zero(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j]==0:
                return (i,j)
            
    return None
                   
    
def solver(matrix):
        
    is_there=find_zero(matrix)
    if (not is_there):        
        return True
    else:    
        i,j=is_there
    
    
    for t in range(1,5):
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
    test_matrix=make_matrix(4) 
    if solver(test_matrix):
        print("solution is:")
        show_matrix(test_matrix)
    else:
        print("not a valid grid")





