class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        i = 0
        j = len(numbers) - 1

        while(i < j):
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                ans.append(i+1)
                ans.append(j+1)
                break
        
        return sorted(ans)