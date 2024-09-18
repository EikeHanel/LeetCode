class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_str = [str(num) for num in nums]
        for k in range(len(num_str)):
            for j in range(k + 1, len(num_str)):
                if num_str[k] + num_str[j] < num_str[j] + num_str[k]:
                    num_str[k], num_str[j] = num_str[j], num_str[k]
        ans = ''.join(num_str)

        return '0' if ans[0] == '0' else ans  