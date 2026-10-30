class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for entity in filter(lambda x: x, path.split('/')):
            if entity == ".":
                continue
            
            if entity == "..":
                if res:
                    res.pop()
                continue

            res.append(entity)

        return '/' + "/".join(res)
