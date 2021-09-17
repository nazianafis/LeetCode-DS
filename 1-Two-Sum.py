class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> bool:
    ls = len(nums)
    for i in range(ls):
        for j in range(i + 1, ls):
            if nums[i] + nums[j] == target:
                return [i, j]
              
# class Solution(object):
#   def twoSum(self, nums: List[int], target: int) -> bool:
#       for i in range (0,len(nums)):
#           if (target - nums[i]) in nums:
#               if nums.index(target-nums[i]) != i:
#                   return [i,nums.index(target-nums[i])] 
