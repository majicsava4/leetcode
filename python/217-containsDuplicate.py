'''Given an integer array nums, return 
true if any value appears at least twice 
in the array, and return false if every 
element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.'''


nums = [1,2,3,4]

def containsDupe(nums):
    setx = set()
    leng = len(nums)
    for i in nums:
        setx.add(i)
            
         
    
    return not (leng == len(setx))
    
print(containsDupe(nums))
