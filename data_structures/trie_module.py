class Node:
    def __init__(self):
        self.word_ends = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root_node = Node()


    def add_word(self,word):
        current_node = self.root_node

        for c in word:
            if c not in current_node.children.keys():
                current_node.children[c] = Node()
            current_node = current_node.children[c]

        current_node.word_ends = True



    def search_word(self,word): 
        current_node = self.root_node

        for c in word:
            if c not in current_node.children.keys():
                return False
            current_node = current_node.children[c]

        return current_node.word_ends 

