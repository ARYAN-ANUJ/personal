class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l=[]
        l2=[]
        for i in s:
            if i=="#":
                if len(l)>0:
                    l.pop()
            else:
                l.append(i)
        for i in t:
            if i=="#":
                if len(l2)>0:
                    l2.pop()
            else:
                l2.append(i)
        if len(l)==len(l2):
            for i in range(len(l)):
                if l[i]==l2[i]:
                    continue
                else:
                    return False
        else:
            return False
        return True
