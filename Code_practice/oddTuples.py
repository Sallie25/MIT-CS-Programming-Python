"""Write a procedure called oddTuples which takes a tuple as input, and returns a new tuple as output, where every othr element of the input tuple is copied, starting with the first one. So, if test is the tuple ('I','am','a','test','tuple'), then evluating oddTuples on this input would return the tuple ('I','a','tuple')
"""
"""_______INCORRECT INTEPRETATION OF RESULT_______"""

# def oddTuples(aTup):
#     odd_tuple = ()
#     for i in aTup:
#         if i % 2 != 0:
#             odd_tuple = odd_tuple + (i,)
#         else:
#             continue    
#     return odd_tuple
# print(oddTuples((16,)))
# print(oddTuples((13,1,15,1,11,19,7,19))) 
#   

""""_________SOLUTION 1________"""
# def oddTuples(aTup):
#     odd_tuple = aTup[::2]
#     return odd_tuple    
# print(oddTuples((16,)))
# print(oddTuples((13,1,15,1,11,19,7,19))) 

"""_______SOLUTION 2_________"""
def indices(aTup):
    index = ()
    for i in range(1,len(aTup)+1):
        index = index + (i,)
    return index    

def oddTuples(aTup):
    tup = ()
    ind = 0
    for j in indices(aTup):
        # print(f"index {j}")
        if j % 2 != 0:
            tup = tup + (aTup[ind],)
            print(f"Tup for index {ind} is {tup}")
            ind += 2     
        else:
            continue
    return tup  
print(oddTuples((16,)),end = "\n\n")      
print(oddTuples((13,1,15,1,11,19,7,19)),end = "\n\n")
print(oddTuples((5,16,11,20,18,3,18,16,15)),end = "\n\n")
print(oddTuples((17,15,12,9)),end = "\n\n")


# # print(indices((13,1,15,1,11,19,7,19)))         

