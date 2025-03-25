class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        booleanList = [(i + extraCandies >= max(candies)) for i in candies]
        return booleanList
