#The idea of this solution is to check for words where there is only a one letter change untill the goal is reached
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        def similarity(str1,str2):
            i = len(str1)
            for j in range(len(str1)):
                if str1[j]==str2[j]:
                    i-=1
            return i
        wordList = set(wordList)
        queue = deque()
        queue.append([beginWord,0])
        visited.add(beginWord)
        while queue: 
            word, seq = queue.popleft()
            if word == endWord:
                    return seq+1
            for w in wordList:
                if similarity(word,w) == 1 and not(w in visited):
                    queue.append([w,seq+1])
                    visited.add(w)
            wordList = wordList.difference(visited)
        return 0
