'''
NE RADI NIJE ZAVRSENO
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]


'''
nums = [1,1,1,2,2,3]
k = 2
def topKFreqElements(nums, k):
    freqmap = {}

    for i in nums:
        freqmap[i] = freqmap.get(i,0) + 1
    count = []
    j = 0
    for i in freqmap:
        if(j == freqmap[i]):
            count[j] = i        
    j += 1
    res = []    
    for i in range(len(count), k, -1):
        res[i] = count[i]
    print(res)    
topKFreqElements(nums,k)

