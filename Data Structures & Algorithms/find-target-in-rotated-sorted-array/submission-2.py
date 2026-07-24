class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        low = self.binarySearch(nums, 0, pivot - 1, target)
        if low != -1:
            return low

        return self.binarySearch(nums, pivot, len(nums) - 1, target)

    def binarySearch(self, nums, left, right, target):
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1