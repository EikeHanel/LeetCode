class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(("".join(map(str, digits))))
        num_1 = number + 1
        ans = str(num_1)
        ans_lst = [int(num) for num in ans]
        return ans_lst