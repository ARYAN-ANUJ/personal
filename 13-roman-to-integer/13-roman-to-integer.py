class Solution:
    def romanToInt(self, s: str) -> int:
        valu={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=0
        s1=0
        s=s+" "
        while i<len(s)-1:
            if s[i]=='I':
                if s[i+1]=='X' or s[i+1]=='V':
                    s1+=valu[s[i+1]]-1
                    i+=1
                else:
                    s1+=1
             
            elif s[i]=='X':
                if s[i+1]=='L' or s[i+1]=='C':
                    s1+=valu[s[i+1]]-10
                    i+=1
                else:
                    s1+=10
                  
            elif s[i]=='C':
                if s[i+1]=='D' or s[i+1]=='M':
                    s1+=valu[s[i+1]]-100
                    i+=1
                else:
                    s1+=100
                   
            else: 
                s1+=valu[s[i]]
            i+=1
        return s1
    