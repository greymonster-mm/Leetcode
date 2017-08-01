class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for k,i in enumerate(nums):
            seek = target - i
            nums[k] = 'used'
            if (seek in nums) :
                return [k, nums.index(seek)]
