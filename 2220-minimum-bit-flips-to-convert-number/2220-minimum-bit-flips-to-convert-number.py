class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # # Initial Code without the hint:

        # start_bin = list(format(start, 'b'))
        # end_bin = list(format(goal, 'b'))
        # len_diff = len(start_bin) - len(end_bin)
        # # Compare bin-length and if different add zeros at the front until the length is equal
        # while len_diff != 0:
        #     if len_diff > 0:
        #         end_bin.insert(0, "0")
        #         len_diff -= 1
        #     elif len_diff < 0:
        #         start_bin.insert(0, "0")
        #         len_diff += 1
        # flip_count = 0
        # # Compare the bin-lists for each number 
        # for n in range(len(start_bin)):
        #     if start_bin[n] != end_bin[n]:
        #         flip_count += 1
        # return flip_count

        # # Code after reading the hint and looking up the XOR operator
        
        # XOR(^) operates on the binary of a number! 
        diff_bit = start ^ goal
        # Count the number of ones in the binary of diff_bit
        return bin(diff_bit).count('1')