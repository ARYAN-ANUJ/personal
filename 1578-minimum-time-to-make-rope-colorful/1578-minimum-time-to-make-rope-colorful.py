class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        sum1=0
        j=0    
        l2=[]
        for i in range(len(colors)-1):
            if colors[i]!=colors[i+1]:
                l2.append(colors[j:i+1])
                j=i+1
        l2.append(colors[j:])
        
        j=k=0
        for i in l2:
            k+=len(i)
            sum1+=max(neededTime[j:k])
            j=k
        return sum(neededTime)-sum1
        