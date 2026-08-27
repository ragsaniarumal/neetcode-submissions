class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]*len(height)
        suffix = [0]*len(height)
        curr_max = 0
        i = 0
        j = len(height) - 1
        water = 0

        for i in range(len(height)):
            curr_max = max(height[i], curr_max)
            prefix[i] = curr_max
        
        curr_max = 0

        for j in range(len(height) - 1, -1, -1):
            curr_max = max(height[j], curr_max)
            suffix[j] = curr_max
        
        for i in range(len(height)):
            water += min(prefix[i], suffix[i]) - height[i]
        
        return water


