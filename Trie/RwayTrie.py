

class Trie:
        
    def __init__(self):
        # do intialization if necessary
        self.root = _Node()
        
    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        # write your code here
        node = self.root
        for w in word:
            if node.links.get(w) is None:
                node.links[w] = _Node(0)
            node = node.links[w]
        node.val = 1
        
    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        # write your code here
        node = self.root
        for w in word:
            if node.links.get(w) is None:
                return False
            else:
                node = node.links[w]
        return node.val == 1

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        node = self.root
        for w in prefix:
            if node.links.get(w) is None:
                return False
            else:
                node = node.links[w]
        return True


class _Node:
    def __init__(self, val=None):
        self.val = val
        self.links = {}