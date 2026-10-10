class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        min_word_cnt = min(len(word1), len(word2))

        for i in range(min_word_cnt):
            res.append(word1[i])
            res.append(word2[i])
        
        res += word1[min_word_cnt:] + word2[min_word_cnt:] 
        return "".join(res)
