class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        import collections
        ddict = collections.defaultdict(list)

        for str in strs:
            ddict["".join(sorted(str))].append(str)
        return sorted(list(ddict.values()))