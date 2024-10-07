class Solution:
    def minLength(self, s: str) -> int:
        s_lst = list(s)
        def substring(lst):
            for n in range(len(lst)):
                if n < len(lst)-1 and (lst[n] == "A" and lst[n+1] == "B" or lst[n] == "C" and lst[n+1] == "D"):
                    lst =  lst[:n] + lst[n+2:]
                    print(lst)
                    return lst
            return False
        
        while True:
            result = substring(s_lst)
            if result: 
                s_lst = result
            else:
                return len(s_lst)


