class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sum_map = defaultdict(list)

        for n in nums:
            total = 0
            number = str(n)
            for c in number:
                total += int(c)
            sum_map[total].append(n)
        res = -1
        for numbers in sum_map.values():
            if len(numbers) > 1:
                sorted(numbers)
                res = max(res, numbers[-1] + numbers[-2])

        return res
