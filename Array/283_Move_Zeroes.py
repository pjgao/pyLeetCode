'''

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

开始的想法冒泡复杂度太高，改为了复杂度N的算法
改进：从最开始找，找到不是0的就放1，再找到不是0的放2....没放的全置0

'''
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
              
        '''版本一
        length_nums = len(nums)
        length_zero = 0
        for i in range(length_nums):
            if not nums[i]:
                length_zero += 1
        not_zero_index = 0
        for num in nums:
            if num:
                nums[not_zero_index] = num
                not_zero_index += 1
        for i in range(length_zero):
            nums[length_nums-length_zero+i] = 0
        '''
        #版本二
        length_nums = len(nums)
        not_zero_index = 0
        for num in nums:
            if num:
                nums[not_zero_index] = num
                not_zero_index += 1
        for i in range(not_zero_index,length_nums):
            nums[i] = 0