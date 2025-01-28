'''
Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
'''
from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
def groupAnagrams(strs):
    res = defaultdict(list)
    
    for s in strs:
        count = [0] * 26
        for j in s:
            count[ord(j) - ord("a")] += 1
        res[tuple(count)].append(s)
    return list(res.values())
    
print(groupAnagrams(strs))