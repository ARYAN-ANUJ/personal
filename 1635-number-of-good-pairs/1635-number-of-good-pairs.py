from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c=defaultdict(int)
        s=0
        for i in nums:
            c[i]+=1
        for i in c.keys():
            s+=(c[i]*(c[i]+1))//2-c[i]
        return s