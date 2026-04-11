class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k):
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_freq[i][0])

        return result
        