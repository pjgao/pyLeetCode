'''

In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.

 

Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.

思路：长度小于3直接pass，
'''
class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        '''
        from collections import OrderedDict
        dic = OrderedDict()
        idx = 0
        dic[idx]=1
        for i in range(1,len(S)):
            if S[i] != S[i-1]:
                dic[i] = 1
                idx = i
            else:
                dic[idx] += 1
        return [[start,start+length-1] for start,length in dic.items() if length >=3]
        '''
        if len(S) < 3:
            return []
        cnt = 1
        res = []
        for i in range(1,len(S)):
            if S[i]!=S[i-1]:
                if cnt >= 3:
                    res.append([i-cnt,i-1])
                cnt =1
            else:
                cnt += 1
        if S[i]==S[i-1] and cnt >=3:
            res.append([i-cnt+1,i])
        return res