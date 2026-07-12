class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
                for num in numbers:
                    if target - num in numbers:
                        first = numbers.index(num) + 1
                        second = numbers.index(target - num) + 1
                        if first == second:
                            second += 1
                        return first, second