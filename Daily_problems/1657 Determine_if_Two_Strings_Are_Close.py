class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return 0
        if set(word1)!=set(word2):
            return 0
        c1=Counter(Counter(word1).values())
        c2=Counter(Counter(word2).values())
        return c1==c2
        