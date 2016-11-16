11. Container With Most Water
# Time: O(N)
# Space: O(1)

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0;
        i = 0
        j = len(height) - 1
        while (i < j):
            h = min(height[i], height[j]);
            water = max(water, (j - i) * h);
            while height[i] <= h and i < j: 
                i += 1
            while height[j] <= h and i < j:
                j -= 1
        return water;