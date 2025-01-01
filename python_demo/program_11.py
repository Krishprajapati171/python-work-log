n1=int(input("Enter the starting number::"))
n2=int(input("Enter the ending number::"))

def Starting_nums(n1,n2):     #starting from order 1 to...
    if(n1<=n2):
        print(n1)
        Starting_nums(n1+1,n2)
    else:
        return
    
Starting_nums(n1,n2)

def Ending_nums(n1,n2):  #ending  in reverse...
    if(n1<=n2):
        print(n2)
        Ending_nums(n1,n2-1)
    else:
        return

Ending_nums(n1,n2)

