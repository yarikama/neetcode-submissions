from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        length = 1
        q = deque([beginWord])
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return length
                
                for idx, char in enumerate(word):
                    for replace in range(ord('a'), ord('z')+1):
                        new_word = word[:idx] + chr(replace) + word[idx+1:]
                        if new_word in wordList:
                            q.append(new_word)
                            wordList.remove(new_word)

            length += 1

        return 0