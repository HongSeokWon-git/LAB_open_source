class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.frequency = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word:
            return
        
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.frequency += 1

    def search(self, word):
        if not word:
            return False
        
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix):
        if not prefix:
            return False
            
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def autocomplete(self, prefix):
        if not prefix:
            return []
        
        def dfs(node, path):
            suggestions = []
            if node.is_end_of_word:
                suggestions.append((path, node.frequency)) # 빈도수를 함께 반환하도록 수정
            
            for char, child_node in node.children.items():
                suggestions.extend(dfs(child_node, path + char))
            
            return suggestions

        node = self.root
        for char in prefix:
            if char not in node.children:
                return []

            node = node.children[char]

        suggestions = dfs(node, prefix)
        suggestions.sort(key=lambda x: (-x[1], x[0])) #빈도와 단어를 함께 정렬
        return [suggestion[0] for suggestion in suggestions[:3]] # 단어만 반환

        #get_frequency 함수를 삭제해도 동일하게 동작함

# Example usage:
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("appetizer")
    trie.insert("app")
    trie.insert("banana")
    trie.insert("bat")
    trie.insert("ball")
    trie.insert("batman")

    print("Search 'app':", trie.search("app"))
    print("Starts with 'app':", trie.startsWith("app"))

    print("Autocomplete suggestions for 'app':", trie.autocomplete("app"))
