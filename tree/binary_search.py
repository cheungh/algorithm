# Node class that represents an individual node in a BST 
# with left and right branch or leaf
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
# binary insert func
def insert(root, node):
    # root ?
    if root is None:
        root = node
    # go left or right?
    if root.val > node.val:
        # go right if right node exist
        # else root.right = node
        if root.left is not None:
            insert(root.left, node)
        else:
            root.left = node
    else:
        if root.right is not None:
            insert(root.right, node)
        else:
            root.right = node

def binary_search(tree, SV):
    # let result be return value
    # 1. found tree.value = SV
    # 2. tree.value > SV:
    #   search left if tree->left
    #   else: "not found
    # 3. tree.value < SV:
    #   search right if tree->right
    #   else: "not found"
    # 4. not found
    result = -1
    if tree.val == SV:
        return 1
    elif tree.val > SV and tree.left is not None:
        result = binary_search(tree.left, SV)
    elif tree.val < SV and tree.right is not None:
        result = binary_search(tree.right, SV)

    return result


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)


a = [7,5,3,6,9,8,10,15,13,12,14,20,18,25]
bst = Node(11)
for i in a:
    insert(bst, Node(i))

finding_result = binary_search(bst, 14)
print("finding 14: result: %s" % finding_result)

inorder(bst)
preorder(bst)
postorder(bst)
