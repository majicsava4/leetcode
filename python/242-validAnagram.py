'''
Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true
'''


s = "rat" 
t = "car"

def validAnagram(t,s):
    if(len(s) != len(t)): return false
    dicts = {}
    dictt = {}
    for i in s:
        dicts[i] = dicts.get(i,0) + 1
    for i in t:
        dictt[i] = dictt.get(i,0) + 1
    return dictt == dicts
        

print(validAnagram(t,s))