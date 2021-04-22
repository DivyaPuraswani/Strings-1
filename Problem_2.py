# Longest Substring without repeating character:

#Brute Force Approach: The brute force approach allows you to iterate through characters in a string and maintain another 
#list which checks for repetition if character is repeated than it breaks the iteration and returns maximum length of string.

#Time Complexity for the same is O(N square) as two passes are there and Space is O(N) as list is used but also since 26 characters are 
#there irrespective of length size it can be O(1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s==None or len(s)==0: # base case
            return 0
        longest=0
        seen=[] # list to store strings which are not having repeating characters 
        for i in range(0,len(s)): # iterating through strinig
            seen=[]
            for j in range(i,len(s)):
                if s[j] in seen: # if charcter is repeated than break
                    break
                else:
                    seen.append(s[j]) # else insert the charcter in list seen
                    #print (seen)
            longest=max(len(seen),longest) # return the string with maximum length
        return longest  


#Two Pointer and Sliding window approach: this approach uses two pointers slow and fast and a hash-map. The fast pointer gets updated with the index of element +1.
#while slow pointer gets updated only when character is repeated. longest(which returns maximum length of string) is initialized to 0 and slow is also initialized to 0. 
#The hashmap contains element as the key and its position as value. So on iterating fast pointer the presence of element is checked in hashmap and if its present than slow gets updated
#with value which is maximum out of its current and the index of element found. else element gets inserted in hashmap with its value as index+1. longest gets updated
#with maximum value out of current longest value and fast-slow+1.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s==None or len(s)==0: # base case
            return 0
        longest=0
        slow=0
        hashmap={}
        for fast in range(len(s)):
            if s[fast] in hashmap:
                slow=max(hashmap[s[fast]],slow)
                
            longest=max(longest, fast-slow+1)
            hashmap[s[fast]]=fast+1
        return longest
        
#Time Complexity for this problem is O(N) and space is constant

