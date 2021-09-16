class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))
        c = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    c = c + 1                    
        if c!=0:
            return True
        else:
            return False
