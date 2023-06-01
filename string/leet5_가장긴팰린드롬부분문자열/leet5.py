class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l + 1:r]

        # 예외처리 잊지말자
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result
                         , expand(i, i + 1)
                         , expand(i, i + 2)
                         , key=len)

        return result





