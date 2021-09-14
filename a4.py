x=int(input("enter number"))
if x>1:
    for n in range(2,x):
        if x%n==0:
            print("its not prime")
            break
    else:
        print(x ,"is prime")
else:
    print("its prime")