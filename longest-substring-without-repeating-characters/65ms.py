from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        current_len = 0
        max_len = 0
        start_index = 0
        d = defaultdict(int)
        for pos, ch in enumerate(s):
            if ch in d:
                if d[ch] >= start_index:
                    start_index = d[ch] + 1
                    current_len = pos - d[ch] # 'first' position of the duplicated char + 1 because of 0-indexing
                else: 
                    current_len += 1
                    if max_len<current_len:
                        max_len=current_len
            else:
                current_len += 1
                if max_len<current_len:
                    max_len = current_len
         
            d[ch]=pos
        return max_len
        
