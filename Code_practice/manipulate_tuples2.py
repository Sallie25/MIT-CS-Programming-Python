# def getdata(atuple):
#     num = ()
#     word = ()
    
#     for t in atuple:
#         num = num + (t[0],)
#         if t[1] not in word:
#             word = word + (t[1],)
#     min_num = min(num)
#     max_num = max(num)
#     unique_words = len(word)
#     return(min_num,max_num,unique_words)

# (small,large,words) = getdata((
#     (1, 'mine'),
#     (3, 'yours'),
#     (5, 'ours'),
#     (7, 'mine')))

# print(small,large,words)

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)  
    max_nums = max(nums)  
    unique_words = len(words)    
    return(min_nums, max_nums, unique_words)

(small,large,words) = get_data((
    (1, 'mine'),
    (3, 'yours'),
    (5, 'ours'),
    (7, 'mine')))

print(small)
print(large)
print(words)

