class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """

        digits = []
        lets = []

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                lets.append(log)

        lets.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return lets + digits