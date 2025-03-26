class Solution(object):
    def majorityElement(self, nums):
        counts = dict(Counter(nums))
        max_key = max(counts, key=counts.get)  # En büyük value'ya sahip key
        return max_key
