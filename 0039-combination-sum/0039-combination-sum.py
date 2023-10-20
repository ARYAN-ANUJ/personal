class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def dfs(can,sum1,arr):
            if sum1==0:
                return ans.append(arr)
            if sum1<=0:
                return
            for i in range(len(can)):
                dfs(can[i:],sum1-can[i],arr+[can[i]])
        dfs(candidates,target,[])
        return ans
