'''
头条面试
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
思路：
65342
165342

1. 倒序
653442
654432 找到原数和倒序第1个不同的，并继续在原数后面找最后一个不等于倒序不同位的

2. 从后向前扫，遇到比max_value 大的就记录这个最大数的值和位置，继续向前扫，遇到小于这个max_value时，就用当前位更新left，用最大位更新right， 因为越往左扫数位越高，交换后整个数字值越大
自右向左，找到当前最大值，若当前位1.大于最大值，更新最大值，2.若小于最大值，则将left标记为当前，并将right更新为当前的最大值

'''
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        num_list = list(str(num))
        max_index = len(num_list)-1
        left,right = 0,0
        for i in range(len(num_list)-1,-1,-1):            
            if num_list[i] > num_list[max_index]:
                max_index = i
            elif num_list[i] < num_list[max_index]:
                # 当出现小于的时候才更新最大值作为右侧交换点
                left,right =i,max_index
        num_list[left],num_list[right] = num_list[right],num_list[left]
        return int(''.join(num_list))