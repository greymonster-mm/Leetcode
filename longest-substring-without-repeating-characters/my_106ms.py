from collections import defaultdict
class Solution(object):
    result = ""
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        current = {}
        recurrent = {}
        tmp = 0
	lastdeli = 0
        for i,c in enumerate(s):
            if c in current:
                if (len(current) > tmp):
                    tmp = len(current)
                deli = current[c] + 1
                for j in range(lastdeli,deli):
                    current.pop(recurrent[j])
		lastdeli = deli

            current[c] = i
            recurrent[i] = c

	lcurrent = len(current)
        if (tmp < lcurrent):
            tmp = lcurrent
        self.ret = tmp
t = Solution()

t.lengthOfLongestSubstring("abcabcbb")
print "ret",t.ret
