class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        front, back = {beginWord}, {endWord}
        words.discard(beginWord)
        words.discard(endWord)
        length = 1

        while front and back:
            if len(front) > len(back):          # 永遠擴展較小的一側
                front, back = back, front

            nxt = set()
            for word in front:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        w = word[:i] + c + word[i+1:]
                        if w in back:           # 兩邊相遇
                            return length + 1
                        if w in words:
                            words.remove(w)
                            nxt.add(w)
            front = nxt
            length += 1

        return 0