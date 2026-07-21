class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_ones = 0
        max_gain = 0

        prev_zero = float("-inf")

        i = 0
        n = len(s)

        while i < n:
            j = i

            while j < n and s[j] == s[i]:
                j += 1
            length = j - i

            if s[i] == '1':
                total_ones += length
            else:
                max_gain = max(max_gain, prev_zero + length)

                prev_zero = length

            i = j
        return total_ones + max_gain