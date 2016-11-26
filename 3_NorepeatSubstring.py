'''
Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self,s):
        start = maxLen = 0
        usedChar = {}
        for i in range(len(s)):
            # print('*'*40)
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]]+1
            else:
                maxLen = max(maxLen,i-start+1)
            
            usedChar[s[i]] = i
            # print('i:'+str(i)+'  s[i]:'+s[i]+'  maxLen:'+str(maxLen)+' start:'+str(start)+'  usedChar['+s[i]+'] : '+str(usedChar[s[i]]))
                  
        return maxLen
