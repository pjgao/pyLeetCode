'''

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

使用max的Lambda 表达式
因为多数元素出现次数大于n/2，故排序后位置在n/2处即是最多的元素
'''
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #return sorted({i:nums.count(i) for i in set(nums)}.items(),key=lambda x:x[1])[-1][0]
        #return(sorted(nums)[int(len(nums)/2)])
        return max(set(nums),key = lambda x:nums.count(x))#使用max的Lambda函数