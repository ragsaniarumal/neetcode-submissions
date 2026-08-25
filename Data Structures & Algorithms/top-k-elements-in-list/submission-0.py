class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}

        for num in nums:
            if num not in mapp:
                mapp[num] = 1
            mapp[num] += 1
        
        l = sorted(mapp, key=mapp.get, reverse=True)

        return l[:k]