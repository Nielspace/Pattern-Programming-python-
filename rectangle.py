def print_rectangle(n, m) : 
      
    for i in range(1, n+1) : 
        for j in range(1, m+1) : 
            if (i == 1 or i == n or
                j == 1 or j == m) : 
                print('*', end="")             
            else : 
                print(" ", end="")             
          
        print() 
  
  
rows = 6
columns = 20
print_rectangle(rows, columns) 


print("========================================")

def print_squaredi(n) : 
    for i in range(1, n+1) : 
        for j in range(1, n+1) : 
            if (i==1 or i==n or j==1 or j==n  
                or i==j or j==(n - i + 1)) : 
                print("*", end = "")             
            else : 
                print(" ", end = "")             
          
        print() 
          
rows = 8
print_squaredi(rows) 