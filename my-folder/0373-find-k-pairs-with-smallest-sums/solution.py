class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq
        res = []
        if not nums1 or not nums2 or not k:
            return res

        seen = set()
        heap = []

        heapq.heappush(heap, (nums1[0]+ nums2[0], 0, 0))
        seen.add((0, 0))

        while k and heap:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i]  , nums2[j]])

            next_i, next_j = i+1, j+1

            if next_i < len(nums1) and (next_i, j) not in seen:
                heapq.heappush(heap, (nums1[next_i]+ nums2[j], next_i, j))
                seen.add((next_i, j))

            if next_j < len(nums2) and (i, next_j) not in seen:
                heapq.heappush(heap, (nums1[i]+ nums2[next_j], i, next_j))
                seen.add((i, next_j))

            k -= 1
        
        return res




        
