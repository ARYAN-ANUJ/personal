from collections import defaultdict 
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic=defaultdict(int)
        ans=list()
        for i in nums:
            dic[i]+=1
        for i in dic.keys():
            if dic[i]>(len(nums)//3):
                ans.append(i)
        return ans