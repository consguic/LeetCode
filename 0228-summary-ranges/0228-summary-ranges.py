class Solution(object):
    def summaryRanges(self, nums):
        liste = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i+1 < len(nums) and nums[i+1] == nums[i] + 1:
                i +=1
            if start != nums[i]:
                liste.append(f"{start}->{nums[i]}")
            else :
                liste.append(f"{start}")
            i +=1
        return liste


