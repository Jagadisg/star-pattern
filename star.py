value=int(input("Enter the no "))
for i in range(value):
    for j in range(1,value-i):
        print(end=" "+ " ")
    for k in range(i+1):
        print("*",end=" ")
    if i==0:
        print(end=" ")
    else:
        for k in range(i):
            print("*",end=" ")
    print("\n")