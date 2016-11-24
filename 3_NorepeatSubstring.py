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
