alist = [0,1,2,3,4,5]
blist = alist
alist[2] = 'hello' 
alist == blist

print(alist is blist)
print(alist)
print(blist)


clist = [6,5,4,3,2]
dlist = []

for num in clist:
    dlist.append(num)
print(clist == dlist)    

print(clist is dlist)

clist[2] = 20
print(clist)

print(dlist)