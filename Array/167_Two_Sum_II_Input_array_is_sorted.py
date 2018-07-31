'''

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
思路：对于i,如果target-i在set中，则查找index，一定要去掉查找过的i
或者：每个i，将差值存到字典里，看后面的值是不是差值
或者：从两端逼近，l =0, r = len()-1 判断[l+r]与target
解题时很多trick是在处理 [0,1,0]，后来发现是有序的，故只会[0,0,1]，所以重复元素的Index在一起，只要判断ix1 == ix2将ix2加1即可
'''
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """       
        '''set
        setNum = set(numbers)
        for j in setNum:        
            if target-j in setNum:
                if j != target-j:
                    return sorted([numbers.index(j)+1,numbers.index(target-j)+1])
                else:
                    ix1 = numbers.index(j)
                    ix2 = (numbers[:ix1]+numbers[ix1+1:]).index(j)+1
                    return [ix1+1,ix2+1]
        '''
        '''两端逼近
        def twoSum(numbers, target):
            l,r = 0,len(numbers)-1
            s = numbers[l] + numbers[r]
            while(l < r):
                if s == target:
                    return [l+1,r+1]
                elif s < target:
                    l += 1
                else:
                    r -= 1
                s = numbers[l] + numbers[r]'''
        d = {}
        for i,j in enumerate(nums):
            if j in d:
                return [d[j]+1,i+1]
            d[target-j] = i