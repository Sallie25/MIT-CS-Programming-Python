"Write a procedure called 'how_many', which returns the sum of the number of values associated with a dictionary"


def how_many(aDict):
    'aDict : A dictionary'
    'Returns: Number of values associated with a dictionary'
    sum = 0
    for keys, values in aDict.items():
        sum += len(aDict[keys])

    return sum    
    
animals = {'a':['aardvark'], 'b':['baboon'], 'c':['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

# print(animals)
print(how_many(animals))