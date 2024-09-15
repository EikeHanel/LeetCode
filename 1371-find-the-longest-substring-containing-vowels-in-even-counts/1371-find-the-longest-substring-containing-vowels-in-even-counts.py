class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Dictionary to set vowels as number(seen as bits)
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        # Used to store the current vowel as a bit
        current_state = 0  

        # Sets everything as equal                     
        state_to_index = {0: -1} 
        
        # Start length              
        max_len = 0                             
        
        # for loop - index, character
        for i, c in enumerate(s):
            # if character a vowel
            if c in vowel_to_bit:   
                # Convert to vowel to number
                bit = vowel_to_bit[c]
                # Takes the bit and makes a Left shift(<<) by 1 -> if bit = 0: 1<<0 = 00001 (number of zeros is dynamically set by python) 
                # XOR (^) Rule: Each bit is compared, and the result is 1 if the bits are different, and 0 if they are the same.
                current_state ^= (1 << bit)

            # checks if the current_state is already in state_to_index
            if current_state in state_to_index:
                # If this is true: 
                # Sets max_len to the either: 
                # max_len or 
                # (current index) i - state_to_index[current_state]
                max_len = max(max_len, i - state_to_index[current_state])
            else:
                # If false set new state_to_index
                state_to_index[current_state] = i

        return max_len
            