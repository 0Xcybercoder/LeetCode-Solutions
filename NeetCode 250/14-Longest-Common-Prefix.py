class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ""
        x = 0
        i = 1
        if len(strs) > 1 and strs[0] != "":
            temp = strs[0][x]
            m = min(len(s) for s in strs)
            while x < m:
                if strs[i][x] == temp:
                    if i == len(strs) - 1:
                        out += temp
                        x += 1
                        if x > m - 1:
                            return out
                        temp = strs[0][x]
                        i = 1
                    else:
                        i += 1
                        continue
                else:
                    return out
        else:
            return strs[0]
        return out