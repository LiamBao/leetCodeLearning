class Solution(object):
'''
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example:
Input: "cbbd"
Output: "bb"
'''

	def Longest_Palindramic_String(self,s):
		"""
		you only need to scan from beginning to the end, 
		adding one character at a time, keeping track of maxPalindromeLen, 
		and for each added character, you check if the substrings ending with this new character, 
		with length P+1 or P+2, are palindromes, and update accordingly.
		"""
		if len(s)==0:
			return s
		maxLen =1
		start = 0
		for i in range(len(s)):
			if i -maxLen >=1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::i]:
				start = i-maxLen-1
				maxLen += 2
				continue

			if i-maxLen>=0 and s[i-maxLen:i+1] == s[i-maxLen+1][::i]:
				maxLen +=1
		return s[start:start+maxLen]
