class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        e=[]
        r=list(set(arr))
        for i in r:
            e.append(arr.count(i))
        if len(set(e))<len(e):
            return False
        else:
            return True