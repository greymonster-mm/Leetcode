"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
"""
class Solution(object):
    result = ""
    def lengthOfLongestSubstring(self, s):
        :type s: str
        :rtype: int
	current = {}
	recurrent = {}
	tmp = []
	i = 0;

	for c in s:
	    if c in current:
		if (len(current) > len(tmp)):
		    tmp = current.copy()
		deli = current[c]+1
		for j in range(deli):
		    if j not in recurrent:
			continue
		    delv = recurrent[j]
		    current.pop(delv)
		    recurrent.pop(j)
	
	    current[c] = i
	    recurrent[i] = c
	    i += 1
	if (len(tmp) < len(current)):
            tmp = current.copy()
	self.ret = tmp	
"""
class Solution(object):
    result = ""
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        current = {}
        recurrent = {}
        tmp = []
        i = 0;
	lastdeli = 0
        for c in s:
            if c in current:
                if (len(current) > tmp):
                    tmp = len(current)
                deli = current[c] + 1
                for j in range(lastdeli,deli):
                    current.pop(recurrent[j])
		lastdeli = deli

            current[c] = i
            recurrent[i] = c
            i += 1

	lcurrent = len(current)
        if (len(tmp) < lcurrent):
            tmp = lcurrent
        self.ret = tmp
t = Solution()

t.lengthOfLongestSubstring("abcabcbb")
print "ret",t.ret
