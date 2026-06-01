
#count smaller after self


import bisect

def countsmaller(nums):
    res = []
    sorted_list = []

    for num in reversed(nums):
        idx = bisect.bisect_left(sorted_list,num)
        res.append(idx)
        bisect.insort(sorted_list,num)

    return res[::-1]
#testing
print(countsmaller([5,2,6,1])) #output: [2,1,1,0]