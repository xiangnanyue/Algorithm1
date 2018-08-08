class WordDictionary:
    
    def __init__(self):
        self.root = _Node()
        
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def addWord(self, word):
        # write your code here
        node = self.root
        for i,w in enumerate(word):
            if node.links.get(w) is None:
                newNode = _Node(0)
                newNode.level = i
                node.links[w] = newNode
            node = node.links[w]
        node.val = 1

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        # write your code here
        node = self.root
        stack = [node]
        length = len(word)
        while len(stack) > 0:
            node = stack.pop()
            if node.level == length-1:
                if node.val==1:
                    return True
                else:
                    continue
            if node.level < length-1:
                w = word[node.level+1]
                if w == ".":
                    for k in node.links.keys():
                        stack.append(node.links[k])
                elif w >= "a" and w <= "z":
                    if node.links.get(w) is not None:
                        stack.append(node.links[w])

        return False
            
class _Node:
    def __init__(self, val=None):
        self.val = val
        self.level = -1
        self.links = {}
                    