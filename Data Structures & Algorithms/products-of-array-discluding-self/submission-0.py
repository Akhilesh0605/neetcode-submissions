class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_arr = [1] * len(nums)


        for i in range(1, len(nums)):
            pref_arr[i] = nums[i - 1] * pref_arr[i - 1]

        suff_arr = [1] * len(nums)


        for i in range(len(nums) - 2, -1, -1):
            suff_arr[i] = nums[i + 1] * suff_arr[i + 1]

        res_arr = [1] * len(nums)

        for i in range(len(nums)):
            res_arr[i] = pref_arr[i] * suff_arr[i]

        return res_arr