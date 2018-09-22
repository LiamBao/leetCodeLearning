from helper import timeit
"""
实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
示例 1：

输入: "Hello"
输出: "hello"
示例 2：

输入: "here"
输出: "here"
示例 3：

输入: "LOVELY"
输出: "lovely"
"""

class Solution:
    @timeit
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        # lower_str = ''
        # for single_char in str:
        #     ascii_num = ord(single_char)
        #     if 90>=ascii_num>=65:
        #         single_char = chr(ascii_num+32)
        #     lower_str += single_char
        # return lower_str

        return ''.join(chr(ord(s)+32) if 'A'<=s<='Z' else s for s in str)

print(Solution().toLowerCase('HKHafsdwe123KJasdfGK'))