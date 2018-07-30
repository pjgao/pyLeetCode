'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

最开始的思路使用set，可能会使用外部空间
最终使用-号来在原位置做标记
'''
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #return list(set(range(1,len(nums)+1))-set(nums))
        #return [i for i in range(1,len(nums)+1) if i not in nums]复杂度太高
        for i in range(len(nums)):
            idx = abs(nums[i])-1
            nums[idx] = -abs(nums[idx])
        return [i+1 for i,j in enumerate(nums) if j > 0]
