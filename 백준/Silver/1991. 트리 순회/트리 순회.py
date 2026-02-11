from sys import stdin

input = stdin.readline

node = int(input().rstrip())
tree = {}
for _ in range(node):
    parent, left, right = input().split()
    tree[parent] = (left,right)

def preoder(n):
    if n == '.':
        return
    print(n,end="")
    left, right = tree[n]
    preoder(left)
    preoder(right)
    
    
def inorder(n):
    if n == '.':
        return
    left, right = tree[n]
    inorder(left)
    print(n,end="")
    inorder(right)

def postorder(n):
    if n == '.':
        return
    left, right = tree[n]
    postorder(left)
    postorder(right)
    print(n,end="")

preoder('A')
print()
inorder('A')
print()
postorder('A')