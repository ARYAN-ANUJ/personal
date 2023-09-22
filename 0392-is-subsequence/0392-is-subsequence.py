class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m=len(t)
        n=len(s)
        j=0
        i=0
        while(i<m and j<n):
            if s[j]==t[i]:
                j+=1
            i+=1
        
        
        return (j==n)