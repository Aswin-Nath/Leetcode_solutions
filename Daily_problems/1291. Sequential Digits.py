An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9

# solution
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        res=[]
        n =10
        for length in range( len(str(low)), len(str(high))+1):
            for start in range(n - length): 
                num = int(digits[start : start + length])
                print(num,start)
                if low <= num <= high:
                    res.append(num)
        return res


        
