"""
The intuition behind this solutions is simply to think of the fastest and cleanest way to save previously seen data. 
Thus the thought was to use two sets one for words and one for prefixes. Each time a word is added, we would add all its possible prefixes
and therefore we only have O(1) time to find the word or the prefixe and if a new word has the same prefixes it would be already added 
and it won't be added again to the set due to item unicity.
If you liked the solution drop a follow on the github account, it would help alot <3
"""



class Trie:

    def __init__(self):
        self.words = set()
        self.prefixes = set()

    def insert(self, word: str) -> None:
        self.words.add(word)
        for j in range(len(word)):
            self.prefixes.add(word[:j+1])

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefixes


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)