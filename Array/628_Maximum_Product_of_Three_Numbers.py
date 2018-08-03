'''


Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

思路：要利用排序后的性质
得到最大三乘积
1. 三个最大的正数相乘
2. 两个最小的负数相乘，再乘最大的正数
3. 全负，最大的三个负数

最大值为负：    [-4,-3,-2,-1]   全为负，最大的即是后三个积   
最大值为正：    
1.最小为正      [1,2,3,4,5]  后三个积
2.最小为负    [-3,0,1,2,3]  max(前两位*最后一位, 最后三位)
'''
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #return (set(range(len(nums)+1))-set(nums)).pop()
        return sum(range(len(nums)+1))-sum(nums)