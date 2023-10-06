class Solution:
    def integerBreak(self, n: int) -> int:
        
        if n<4:
            return n-1
        elif n==4:
            return 4
        else:
            r=n%3
            q=n//3
            if (r==1):
                return pow(3,q-1)*4
            else:
                return pow(3,q)*(max(r,1))
        