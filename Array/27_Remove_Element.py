'''

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
思路：
对Nums原地修改，返回的是长度
记录更改的位置，遍历往那个位置上添加
搜索也要O(n)，尽量在自己的循环里完成

'''
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        '''my solution
        length = len(nums) - nums.count(val)
        if val not in nums:
            return len(nums)
        start = nums.index(val)
        equal = start
        for i in range(start,len(nums)):
            if nums[i] != val:
                nums[equal] = nums[i]
                equal += 1
        return length
        '''
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1    
        return k