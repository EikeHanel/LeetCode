class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # # First attempt, is correct, but resulted in Memory Limit Exceeded
        # nums = []
        # ans = []
        # for q in queries:
        #     nums.append(arr[q[0]:q[1]+1])
            
        # for num in nums:
        #     length = len(num)
        #     if length == 1:
        #         ans. append(num[0])
        #     else:
        #         ans.append(reduce(lambda x, y: x ^ y, num))
        # return ans

        # # Second attempt. With lots of googling
        # By creating a prefix, with the length of len(arr) + 1 we can tabulate all XOR values for the list
        # e.g. prefix[4] contains the XOR of all elements from arr[0] to arr[3]
        prefix = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            prefix[i] = prefix[i-1] ^ arr[i-1]
        
        # Step 2: Process each query
        ans = []
        for q in queries:
            l, r = q
            # XOR of the sub-array arr[l:r+1] is prefix[r+1] ^ prefix[l]
            result = prefix[r+1] ^ prefix[l]
            ans.append(result)
        
        return ans