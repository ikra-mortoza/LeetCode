class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = ""
        flag = True
        for ind,letter in enumerate(word1):
            ci = ind
            merged = merged + letter
            if flag and len(word2)> ind: 
                merged = merged + word2[ind] 
                if len(word2) == (ind+1):
                    flag = False
        if flag :
            merged = merged + word2[ci+1:]
        return merged

s = Solution()
print(s.mergeAlternately('abcd', 'pq'))
