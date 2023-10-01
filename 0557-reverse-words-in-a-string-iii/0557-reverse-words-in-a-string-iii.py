class Solution:
    def reverseWords(self, s: str) -> str:
        lis=list(s.split(" "))
        for i in range(len(lis)):
            lis[i]=lis[i][::-1]
        return " ".join(lis)