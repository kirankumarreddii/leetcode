class TrieNode():
    def __init__(self):
        self.children={}
        self.last_word=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        node=self.root
        for s in word:
            if s not in node.children:
                node.children[s]=TrieNode()
            node=node.children[s]
        node.last_word=True

    def search(self, word: str) -> bool:
        def dfs(index,node):
            if len(word)==index:
                return node.last_word
            
            char=word[index]

            if char=='.':
                for char in node.children.values():
                    if dfs(index+1,char):
                        return True
                return False
            else:
                if char not in node.children:
                    return False

                return dfs(index+1,node.children[char])



        return dfs(0,self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)