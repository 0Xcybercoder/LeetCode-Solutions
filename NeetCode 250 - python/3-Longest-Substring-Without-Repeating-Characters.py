class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ""
        mx = 0
        cur = 0
        st = 0
        check = False

        while cur < len(s):
            if s[cur] not in temp:
                temp += s[cur]
                cur += 1
                check = True
            if len(temp) > mx:
                mx = len(temp)
            elif check == False:
                cur = st + 1
                st = cur
                temp = ""
            check = False



        return mx