'''

We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Input: 
bits = [1, 1, 1, 0]
Output: False

思路：如过是1的话就跳一下，看最后跳到了倒数第二个还是倒数第一个

'''
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits)-1:
            if bits[i]:
                i+=1    
            i+=1

        return i == len(bits)-1: