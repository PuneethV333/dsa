# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# from collections import Counter
def topKFrequent(nums: list[int], k: int) -> list[int]:
    freq = {}
    for i in nums:
        freq[i] = freq.get(i,0)+1
        
    return sorted(freq,key=freq.get,reverse=True)[:k]


print(topKFrequent([1,2],2))