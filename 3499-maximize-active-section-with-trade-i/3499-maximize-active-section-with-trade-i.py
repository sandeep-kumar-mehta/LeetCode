from math import inf
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        cnt = s.count("1")

        i = 0
        n = len(s)
        bestGain = 0
        prev = -inf

        while i < n:
            start = i

            while i < n and s[i] == s[start]:
                i += 1
            if s[start] =="0":
                curr = i - start
                bestGain = max(bestGain, prev + curr)
                prev = curr

        return cnt + bestGain
        