class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for n in nums:
            hm[n] = hm.get(n,0) + 1
        kheap = []
        for num, freq in hm.items():
            heapq.heappush(kheap, (hm[num], num))
            if len(kheap) > k:
                heapq.heappop(kheap)
        res = []        
        for i in range(k):
            res.append(heapq.heappop(kheap)[1])
        return res    

