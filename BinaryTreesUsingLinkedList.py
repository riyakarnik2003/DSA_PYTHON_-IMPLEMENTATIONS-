class BT:
    class treenode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

   
    def get_node(data):
        return BT.treenode(data)

  
    def insert_treenode(data, parent, child):
        if parent is not None:
            if child == 'l':
                parent.left = BT.treenode(data)
                if parent.left is not None:
                    return parent.left
            elif child == 'r':
                parent.right = BT.treenode(data)
                if parent.right is not None:
                    return parent.right
        return parent

   
    def inorder(root):
        if root is None:
            return
        BT.inorder(root.left)
        print(root.data, end=" ")
        BT.inorder(root.right)

if __name__ == "__main__":
        root = BT.get_node(10)
        BT.insert_treenode(5, root, 'l')
        BT.insert_treenode(12, root, 'r')
        BT.insert_treenode(25, root.left, 'l')
        BT.insert_treenode(67, root.right, 'l')
        BT.inorder(root)

