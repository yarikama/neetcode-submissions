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
                if word1[j] != word2[j]:
                    adj[word1[j]].append(word2[j])
                    break

        if not adj:
            return ""
        
        print(adj)

        ans = []
        visit, path = set(), set()
        def dfs(node: str) -> bool:
            if node in visit: return False
            if node in path: return True
            path.add(node)
            for dst in adj[node]:
                if dfs(dst):
                    return True
            path.remove(node)
            visit.add(node)
            ans.append(node)

        for a in alphas: 
            if dfs(a):
                print("hello")
                return ""

        return "".join(ans[::-1])






            