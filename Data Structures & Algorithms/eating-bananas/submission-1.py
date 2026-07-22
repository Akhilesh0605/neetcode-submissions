class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ok (piles,k,h):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            return hours<=h
        l = 1
        r = max(piles)
        while l<=r:
            mid = (l+r)//2
            if ok(piles,mid,h):
                r = mid -1 
            else:
                l = mid + 1
        return l