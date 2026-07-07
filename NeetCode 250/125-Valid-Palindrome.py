class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = "[~!@#$%^&*()_+{}|:;<>,.?/'\"-\` ]"
        s.strip()
        new = ""
        for char in s:
            if char not in pattern:
                new += char
        new = new.lower()
        print(new)
        if new == new[::-1]:
            return True
        return False