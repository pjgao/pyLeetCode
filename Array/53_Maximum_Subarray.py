'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
思路：
对于nums[i-1]，如果大于0的话，就把nums[i]加上nums[i-1]
'''
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums = [0] + nums
        #from itertools import accumulate        
        #return max(accumulate(nums))-min(accumulate(nums))
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i] += nums[i-1]
        return max(nums)
