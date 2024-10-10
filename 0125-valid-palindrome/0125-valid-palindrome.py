non_aphanumeric = (' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
 ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
 '\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', 
 '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', 
 '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', '\x7f')


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "" or s == " ":
            return True

        pal = "".join(s).translate(str.maketrans("", "", "".join(non_aphanumeric))).lower()

        if pal == pal[::-1]:
            return True
        else:
            return False