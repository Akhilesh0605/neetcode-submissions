class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while low<high:
            mid=low+(high-low)//2
            timeTaken=self.maxTime(mid,piles)
            if timeTaken<=h:
                high=mid
            else :
                low=mid+1
        return low
    
    def maxTime(self,hours:int,piles:List[int])->int:
        time=0
        for pile in piles:
            time += math.ceil(pile/hours)
        return time