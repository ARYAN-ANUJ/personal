class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        count=[]
        j=0
        for i in range(n):
            if j<len(target):
                if target[j]==i+1:
                    count.append("Push")
                    j+=1
                else:
                    count.append("Push")
                    count.append("Pop")
            else:
                return count
        return count