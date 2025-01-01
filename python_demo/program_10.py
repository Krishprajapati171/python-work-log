def printing_num(n):
    if n>0:
       print(n)
    else:
        return printing_num(n*(n-1))
printing_num(1)
printing_num(2)
printing_num(3)
printing_num(4)
printing_num(5)