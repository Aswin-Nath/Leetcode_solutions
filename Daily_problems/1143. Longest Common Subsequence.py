Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters


#solutions


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1=len(text1)
        memo={}
        n2=len(text2)
        def back(i1,i2):
            if (i1,i2) in memo:
                return memo[(i1,i2)]
            if i1==n1 or i2==n2:
                return 0
            res=float("-inf")
            if text1[i1]==text2[i2]:
                go=max(res,1+back(i1+1,i2+1))
            else:
                go=max(res,back(i1+1,i2),back(i1,i2+1))
            memo[(i1,i2)]=go
            return memo[(i1,i2)]
        return back(0,0)
      
