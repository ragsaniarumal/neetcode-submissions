class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapp = {}
        for num in nums:
            if num in mapp:
                return True
            mapp[num] = 1
        
        return False