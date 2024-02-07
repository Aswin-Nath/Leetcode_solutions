Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?



# Solution

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        C=Counter()
        left=0
        cur_count=0
        T=Counter(t)
        req_count=len(T)
        min_len=float("inf")
        tar=""
        for right in range(len(s)):
            char=s[right]
            C[char]+=1
            if char in T and C[char]==T[char]:
                cur_count+=1
            while(cur_count==req_count):
                if right-left+1<min_len:
                    min_len=right-left+1
                    tar=s[left:right+1]
                l=s[left]
                C[l]-=1
                if l in C and C[l]<T[l]:
                    cur_count-=1
                left+=1
        return tar

