
# subbray sum equal k
def subarraysum(nums,k):
    count = 0
    cs = 0

    ps = {0:1}
    for num in nums:
        cs += num

        diff =cs -k
        if diff in ps:
            count += ps[diff]

        ps[cs]=ps.get(cs,0) + 1

    return count

#testing
print(subarraysum([1,1,1],2)) #output: 2
print(subarraysum([1,2,3],3)) #output:2
