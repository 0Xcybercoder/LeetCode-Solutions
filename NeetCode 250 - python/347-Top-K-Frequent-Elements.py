class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                        nums.sort()
                        ans = []
                        cnt = 1
                        l = []
                        n = len(nums)
                        if n == 1:
                            p = (nums[0], cnt)
                            l.append(p)
                        for i in range(n - 1):

                            if nums[i] == nums[i + 1]:
                                cnt += 1
                            if nums[i] != nums[i + 1] or (nums[i] == nums[i + 1] and (i + 1 == n - 1)):
                                p = (nums[i], cnt)
                                l.append(p)
                                cnt = 1
                                if nums[i] != nums[i + 1] and (i + 1 == n - 1):
                                    p = (nums[i + 1], cnt)
                                    l.append(p)
                                
                            elif (n == 2 and nums[i] != nums[i + 1]):
                                p = (nums[i + 1], cnt)
                                l.append(p)
                        l = sorted(l, key=lambda x: x[1])
                        print(l)
                        if len(l) == 1:
                            m = l[0][0]
                            ans.append(m)
                            return ans

                        for i in range(len(l) - 1, -1, -1):
                            if k == 0:
                                break
                            m = l[i][0]
                            ans.append(m)
                            k -= 1
                        return ans