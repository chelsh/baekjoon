import sys

N = int(sys.stdin.readline())

class Node:
	def __init__(self, key, parent, left, right):
		self.key = key
		self.parent = parent
		self.left = left
		self.right = right

tree = []

for _ in range(N):
	key, left, right = sys.stdin.readline().split()
	node = Node(key, '.', left, right)
	for i in range(len(tree)):
		if tree[i].key == left or tree[i].key == right:
			tree[i].parent = key
		if tree[i].left == key or tree[i].right == key:
			node.parent = tree[i].key
	tree.append(node)

for i in range(N):
	for j in range(N):
		if tree[j].key == tree[i].left:
			tree[i].left = tree[j]
			tree[j].parent = tree[i]
		elif tree[j].key == tree[i].right:
			tree[i].right = tree[j]
			tree[j].parent = tree[i]

root = None
for i in range(N):
	if tree[i].key == 'A':
		root = tree[i]
		break

preorder_list = []
inorder_list = []
postorder_list = []

def preorder(node):
	preorder_list.append(node.key)
	if node.left != '.':
		preorder(node.left)
	if node.right != '.':
		preorder(node.right)
preorder(root)

def inorder(node):
	if node.left != '.':
		inorder(node.left)
	inorder_list.append(node.key)
	if node.right != '.':
		inorder(node.right)
inorder(root)

def postorder(node):
	if node.left != '.':
		postorder(node.left)
	if node.right != '.':
		postorder(node.right)
	postorder_list.append(node.key)
postorder(root)

print(''.join(preorder_list))
print(''.join(inorder_list))
print(''.join(postorder_list))
