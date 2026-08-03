class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter={}
        for num in nums:
            counter[num]=1+counter.get(num,0)
        buckets= [[] for _ in range(len(nums)+1)]

        for num,count in counter.items():
            buckets[count].append(num)
        
        result=[]

        for count in range(len(buckets)-1,0,-1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:

                    return result        
        