from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
            
        q = deque([beginWord])
        length = 1
        
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return length
                
                for idx, char in enumerate(word):
                    for replace in range(ord('a'), ord('z')+1):
                        new_word = word[:idx] + chr(replace) + word[idx+1:]
                        if new_word in wordList:
                            if new_word == endWord:
                                return length + 1
                            q.append(new_word)
                            wordList.remove(new_word)

            length += 1

        return 0