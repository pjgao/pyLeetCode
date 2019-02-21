'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].

解读1：
地面是10，第一阶是15 第二阶是20。从第一阶15出发，上两个台阶就到了top。sum是15
解读2:
地面是1，从地面出发1，两个台阶到1，两个台阶到1，两个台阶到1，一个台阶到1，两个台阶到1，一个台阶到top。sum是6
思路：
要到top的话有两种情况：走一步到top和走两步到top
1. [10, 15, 20] top
   f(i) = f(i-2) + cost[i-2]  (f(top) = f(3))
2. [10, 10,  1] top
   f(i) = f(i-1) + cost[i-1]  (f(top) = f(3))
'''
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """        

        f = [0]*(len(cost)+1)
        for i in range(2,len(cost)+1):
            f[i] = min(f[i-1]+cost[i-1],f[i-2]+cost[i-2])
        return max(f[-1],f[-2])