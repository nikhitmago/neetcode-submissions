class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        '''
        word: .ay
        word: day
        word: b..

        Trie:
        d b m
        a a a
        y y y
        '''

        def dfs(root, j) -> bool:
            cur, n = root, len(word)

            for i in range(j, n):
                if word[i] == '.':
                    for child in cur.children.values():
                        if dfs(child, i+1):
                            return True
                    return False
                else:
                    if word[i] not in cur.children:
                        return False
                    cur = cur.children[word[i]]
            
            return cur.endOfWord
        
        return dfs(self.root, 0)