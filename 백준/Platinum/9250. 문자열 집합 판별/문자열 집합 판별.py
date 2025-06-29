import sys
from collections import deque

input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.output = False

def build_trie(patterns):
    root = Node()

    for word in patterns:
        node = root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()

            node = node.children[ch]

        node.output = True

    return root

def build_failure_links(root):
    q = deque()
    root.fail = root

    for child in root.children.values():
        child.fail = root
        q.append(child)

    while q:
        current = q.popleft()

        for ch, child in current.children.items():
            fail_node = current.fail

            while fail_node != root and ch not in fail_node.children:
                fail_node = fail_node.fail

            child.fail = fail_node.children[ch] if ch in fail_node.children else root

            if child.fail.output:
                child.output = True

            q.append(child)

def search(text, root):
    node = root

    for ch in text:
        while node != root and ch not in node.children:
            node = node.fail

        if ch in node.children:
            node = node.children[ch]

        if node.output:
            return True

    return False

N = int(input())
S = [input().strip() for _ in range(N)]

Q = int(input())
queries = [input().strip() for _ in range(Q)]

root = build_trie(S)
build_failure_links(root)

for q in queries:
    print("YES" if search(q, root) else "NO")