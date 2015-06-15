#!/usr/bin/env python
 
#EXAMPLE = [1,2,3]
EXAMPLE = [1,2,3,4,5,6,7,8,10,0]

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        nums = sorted(nums)
        ans = []
        ans.append(nums)
        if len(nums) > 1 :
            for x in nums:
                bak = nums[:]
                bak.remove(x)
                more = self.subsets(bak)
                for i in more:
                    if i not in ans:
                        ans.append(i)
        #ans = list(set(ans))
        return ans


i = Solution()
print i.subsets(EXAMPLE)
