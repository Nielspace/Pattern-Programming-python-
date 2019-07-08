def holidaybush(n):
    z=n-1
    x=1
    for i in range(0,n):
        for i in range(0,z):
            print(' ',end='')
        for i in range(0,x):
            print(i,end='')
        x=x+2
        z=z-1
        print()


holidaybush(5)



print('==================================================')


H = int(input('Enter a number ')) # specify the tree's height
print((H+2)*' '+'Merry Christmas!')
for i in range(H):
    print((H-i)*2*' '+'o'+ i*'~x~o')
    print(((H-i)*2-1)*' '+(i*2+1)*'/'+'|'+(i*2+1)*'\\')



print("==================================================")


def tree(a,b,space, n):
      

    while b< a-1 and a>0:
        print(' '*a+'*'+'*'*b)
        a-=1
        b+=2

    for _ in range(n):
        print(' '*(space-1)+'|||')
    print(' '*(space-5), '\_@_@_@_/')


a = 40 
b =0
space = 40
n = 4

tree(a,b,space, n)