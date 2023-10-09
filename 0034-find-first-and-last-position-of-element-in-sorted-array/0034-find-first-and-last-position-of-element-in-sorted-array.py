class Solution(object): 



    def searchRange(self, nums, target):
        
        result = [-1, -1] 
        index = -1 
        low, high = 0, len(nums) -1 
        
        while low <= high: 
            mid = low + (high - low)//2 
		
            if nums[mid] == target: 
                index = mid 
                high = mid - 1 
            elif nums[mid] > target:  
                high = mid - 1 
            else:  
                low = mid + 1 
        result[0] = index

        index = -1
        low, high = 0, len(nums) -1
        
        while low <= high:
            
            mid = low + (high - low)//2
            
            if nums[mid] == target:
                index = mid
                low = mid + 1 
            elif nums[mid] > target: 
                high = mid - 1
            else:
                 low = mid + 1

        result[1] =index 
        
        return result
		

