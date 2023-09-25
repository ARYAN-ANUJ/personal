from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic1=defaultdict(int)
        for i in t:
            dic1[i]+=1

        for i in s:
            dic1[i]-=1
        
        for i in dic1.keys():
            if dic1[i]>0:
                return i
        return ""