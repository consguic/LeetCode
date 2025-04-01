class Solution(object):
    def twoSum(self, nums, target):
        diff = {}
        for i in range(len(nums)):
            fark = target - nums[i] 
            if fark in diff:
                return (i,diff[fark])
            diff[nums[i]] = i

