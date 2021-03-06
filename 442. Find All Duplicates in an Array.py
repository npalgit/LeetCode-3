# 442. Find All Duplicates in an Array
# Time: O(N)
# Space: O(N)

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set()
        res = []
        for num in nums:
            if num in s:
                res.append(num)
            else:
                s.add(num)
        
        return res


# Time: O(N)
# Space: O(1)

# take value as index and negate to indicate twice
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return res
