import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt =[(-freq,key) for key,freq in Counter(nums).items()]
        res = []

        heapq.heapify(cnt)
        while cnt and len(res)<k:
            res.append(heapq.heappop(cnt))

        return [key for (_,key) in res ]
