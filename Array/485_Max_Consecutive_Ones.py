'''
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4)
dfs，两种思路，一种是使用栈，另外一种递归，
依次将：
    查找到为1的点的上下左右四个值添加到栈中或者进行递归函数，判断后的值要置为0避免再次查找

'''
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums.sort()

        #return sum([nums[i] for i in range(len(nums)) if  not i % 2])
        return sum(sorted(nums)[::2])
        