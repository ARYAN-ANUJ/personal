
class Solution:
    def minDeletions(self, s: str) -> int:
        dic = [0] * 26

        for i in s:
            dic[ord(i)-ord('a')]+=1
        dic.sort()
        count=0
        for i in range(24,-1,-1):
            if dic[i]==0:
                break
            if dic[i]>=dic[i+1]:
                prev=dic[i]
                dic[i]=max(0,dic[i+1]-1)
                # print(count)
                count+=prev-dic[i]
        return count