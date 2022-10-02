class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        l={}
        def count(d,t):
            c=0
            if (d,t) in l:
                return l[(d,t)]
            if t>k*(n-d):
                l[(d,t)]=0
                return 0
            if d==n:
                return 1 if t==0 else 0
            else :
                
                for i in range(1,k+1):
                    d+=1
                    if t-i>=0:
                        c+=count(d,t-i)
                    d-=1
            l[(d,t)]=c
            return c
        return count(0,target)%(10**9+7)
                    