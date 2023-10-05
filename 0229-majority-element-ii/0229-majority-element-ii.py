from collections import defaultdict 
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic=defaultdict(int)
        l=len(nums)//3
        ans=list()
        for i in nums:
            dic[i]+=1
        for k, v in dic.items():
            if v > l:
                ans.append(k)
        return ans