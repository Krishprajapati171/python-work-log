dict={}

for i in range(5):
    k = str(input("enter the keys::"))
    v = int(input("Enter the values::"))
    print(dict.update({k:v}))
print(dict)
