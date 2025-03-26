class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(0,len(nums2)):
            nums1[m] = nums2[i]
            m +=1
        nums1.sort()
        return nums1
        