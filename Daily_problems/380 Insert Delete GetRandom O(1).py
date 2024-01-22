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


