num = int(input("Enter the number"))
for i in range(num):
    for j in range(num-i):
        print(" ",end="")
    for k in range(i+1): 
          n = i+1
          if k==0:
              print('*',end=' ')
          elif k==(n-1):
              print('*',end=' ')
          elif i==num-1:  
              print('*',end=' ')
          else:
              print(' ',end=' ')
    print('')