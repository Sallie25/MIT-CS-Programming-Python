"""Write a procedure called oddTuples which takes a tuple as input, and returns a new tuple as output, where every othr element of the input tuple is copied, starting with the first one. So, if test is the tuple ('I','am','a','test','tuple'), then evluating oddTuples on this input would return the tuple ('I','a','tuple')
"""
def oddTuples(aTup):
    odd_tuple = ()
    for i in aTup:
        if i % 2 != 0:
            odd_tuple = odd_tuple + i
        else:
            continue    
    return odd_tuple

print(oddTuples((16,)))   