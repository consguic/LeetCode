class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0  # Boş liste için 0 döndür

        k = 0  # Tekrarsız elemanların indexi
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:  # Farklı bir eleman bulunursa
                k += 1
                nums[k] = nums[i] 
        return k + 1  # Benzersiz eleman sayısını döndür