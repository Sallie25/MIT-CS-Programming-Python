"""Write a procedure called 'biggest' which returns the key corresponding to the entry with the biggest number of values associated with it. If there is more than one such entry, return any one of the matching keys.
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the vlues are lists.
    returns: The key with the largest number of values associated with it.
    '''
    len_values = {}
    for keys, values in aDict.items():
        len_values[keys] = len(values)
    # return max(len_values.values())    

    return max(len_values, key = len_values.get)


animals = {'a':['aardvark'], 'b':['baboon'], 'c':['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))