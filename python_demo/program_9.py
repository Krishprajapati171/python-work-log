n1=int(input("Enter the value of n1::"))
n2=int(input("Enter the value of n2::"))
def addition(n1,n2):
    z=n1+n2
    print("The sum of the n1 and n2 is ::",z)

    if(z>=100):
        print("The sum is found to be more than 100")

    else:
        print("The sum is less than 100")

addition(n1,n2)