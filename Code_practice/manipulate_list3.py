listA = [1,4,3,0]
listB = ['x','z','t','q']

listA.sort
listA.sort()
print(listA)

listA.insert(0,100)
listA.remove(3)
listA.append(7)
print(listA)

listA + listB

listB.sort()
listB.pop()

print(listB.count('a'))

# listB.remove('a') #ValueError: list.remove(x): x not in list

listA.extend([4,1,6,3,4])

print(listA.count(4))

print(listA.index(1))

listA.pop(4)

listA.reverse()

print(listA)