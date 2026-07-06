class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        NZmul = 1
        zcount = 0
        for i in range(len(nums)):
            mul *= nums[i]
            if nums[i] == 0:
                zcount += 1
            if nums[i] != 0:
                NZmul *= nums[i]

        ans = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                ans[i] = int(mul * (nums[i] ** -1))
            else:
                if NZmul == 1 and zcount > 1:
                    NZmul = 0
                if zcount == 1:
                    ans[i] = int(NZmul)

        return ans