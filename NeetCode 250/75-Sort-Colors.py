class Solution:
    def sortColors(self, nums: List[int]) -> None:
        Zcount = 0
        Fcount = 0
        Scount = 0
        for i in range(len(nums)):
            if (nums[i] == 0): 
                Zcount += 1
            elif(nums[i] == 1):
                Fcount += 1
            else:
                Scount += 1
        nums.clear()
        nums.extend([0] * Zcount)
        nums.extend([1] * Fcount)
        nums.extend([2] * Scount)