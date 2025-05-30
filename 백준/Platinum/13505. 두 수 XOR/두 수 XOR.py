class TrieNode:
    def __init__(self):
        self.child = [None, None]

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root

        for i in reversed(range(31)):  
            bit = (num >> i) & 1

            if not node.child[bit]:
                node.child[bit] = TrieNode()

            node = node.child[bit]
    
    def max_xor(self, num):
        node = self.root
        xor_sum = 0

        for i in reversed(range(31)):
            bit = (num >> i) & 1
            toggled_bit = 1 - bit

            if node.child[toggled_bit]:
                xor_sum |= (1 << i)
                node = node.child[toggled_bit]

            else:
                node = node.child[bit]

        return xor_sum

def find_max_xor(arr):
    trie = Trie()
    max_xor = 0
    trie.insert(arr[0])

    for num in arr[1:]:
        max_xor = max(max_xor, trie.max_xor(num))
        trie.insert(num)

    return max_xor

N = int(input())
arr = list(map(int, input().split()))

print(find_max_xor(arr))