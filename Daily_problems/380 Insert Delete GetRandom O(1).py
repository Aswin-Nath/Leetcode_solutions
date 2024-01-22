Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
 

Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104


# solution

class RandomizedSet:

    def __init__(self):
        self.has=Counter()
    def insert(self, val: int) -> bool:
        if val not  in self.has:
            self.has[val]+=1
            return 1
        else:
            return 0
    def remove(self, val: int) -> bool:
        if val in self.has:
            self.has[val]-=1
            if not self.has[val]:
                del self.has[val]
            return 1
        else:
            return 0
    def getRandom(self) -> int:
        self.r=list(self.has.keys())
        return random.choice(self.r)


