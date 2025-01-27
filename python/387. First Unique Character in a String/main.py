''' 
387. First Unique Character in a String
Easy
Topics
Companies
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.
'''


s = "leetcodel"
dict = {}
def firstUniqueChar(s):
    for i in s:
        dict[i] = dict.get(i, 0) + 1

    for i in range(len(s)):
        if(dict[s[i]] == 1):
            return i
    
    return -1 



print(firstUniqueChar(s))