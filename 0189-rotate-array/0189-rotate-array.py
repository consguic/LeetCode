class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        my_dict = {}
        for index,i in enumerate(nums):
            my_dict.update({index:i})
        count = 0
        k = k % len(nums)

        while count< len(nums) & len(nums) > 1:    
            if count < len(nums)-k:
                nums[count+k] = my_dict[count]
            else:
                nums[count + k - len(nums)] = my_dict[count] 
            count +=1 