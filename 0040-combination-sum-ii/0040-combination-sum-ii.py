class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def dfs(can,sum1,arr):
            if sum1==0:
                return ans.append(arr)
            if sum1<=0:
                return
            for i in range(len(can)):
                if i>0 and can[i]==can[i-1]:
                    continue
                dfs(can[i+1:],sum1-can[i],arr+[can[i]])
        candidates.sort()
        dfs(candidates,target,[])
        return ans
