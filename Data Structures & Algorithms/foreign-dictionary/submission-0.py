from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)
        alphas = set()
        for i in range(1, len(words)):
            word1, word2 = words[i-1], words[i]
            alphas.update(word1)
            alphas.update(word2)
            len1, len2 = len(word1), len(word2)
            for j in range(min(len1, len2)):
                if word1[j] == word2[j]:
                    continue
                else:
                    adj[word1[j]].append(word2[j])
        
        visit = set()
        ans = []
        def dfs(node: str):
            if node in visit: return

            for dst in adj[node]:
                dfs(dst)

            visit.add(node)
            ans.append(node)

        for a in alphas: dfs(a)

        return "".join(ans[::-1])


            






            