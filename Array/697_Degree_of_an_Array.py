'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6

思路：先找出现次数n最多的值,对于出现n次的值，分别计算最左边和最右边的该值的索引，拿len-去两个索引即是长度
'''
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """       
        dic = {i:nums.count(i) for i in set(nums)}
        degree = max(dic.values())    
        if degree== 1:
            return 1
        n = [i for i in dic if dic[i] == degree]
        minimum = len(nums)    
        for i in n:
            length = len(nums) - nums.index(i)-nums[::-1].index(i)
            minimum = min(minimum,length)
        return minimum