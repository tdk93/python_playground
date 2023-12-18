from trie_module import *

class TestCase:
    def __init__(self,word,result):
        self.word = word 
        self.result = result 

def test_trie():
    trie = Trie()

    present_words = ["hello", "helloWorld", "red"]
    absent_words = ["h", "helloo", "yellow","redd"]

    for w in present_words:
        trie.add_word(w)


    cases = []
    for w in present_words:
        cases.append(TestCase(w,trie.search_word(w)))
    
    for w in absent_words:
        cases.append(TestCase(w,trie.search_word(w)))

    for case in cases:
        print(case.word)
        print(case.result)
        print("========")

def main():
    print('hello')
    test_trie()

if __name__=="__main__":
    main()


    

