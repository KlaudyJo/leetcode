class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = dict()
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        sorted_items = sorted(seen.items(), key=lambda x: x[1], reverse=True)

        return [item[0] for item in sorted_items[:k]]
