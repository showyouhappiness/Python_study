class TreeNode(object):
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None

    def getCommonAncestor(root, node1, node2):
        while root:
            print(root.item)
            if root.item > node1.item and root.item > node2.item:
                root = root.lchild
            elif root.item < node1.item and root.item < node2.item:
                root = root.rchild
            else:
                return root
        return None


# 创建一棵排序二叉树
root = TreeNode(6)  # 根节点
root.lchild = TreeNode(2)  # 左子树
root.rchild = TreeNode(8)  # 右子树
root.lchild.lchild = TreeNode(0)  # 左子树的左子树
root.lchild.rchild = TreeNode(4)  # 左子树的右子树
root.rchild.lchild = TreeNode(7)  # 右子树的左子树
root.rchild.rchild = TreeNode(9)  # 右子树的右子树
root.lchild.rchild.lchild = TreeNode(3)  # 左子树的右子树的左子树
root.lchild.rchild.rchild = TreeNode(5)  # 左子树的右子树的右子树

# 查找叶节点的最近公共祖先
leaf1 = root.lchild.lchild  # 叶节点 0
leaf2 = root.lchild.rchild.rchild  # 叶节点 5
ancestor = TreeNode.getCommonAncestor(root, leaf1, leaf2)  # 查找最近公共祖先
print("Lowest Common Ancestor:", ancestor.item)  # 打印最近公共祖先的值


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_lowest_common_ancestor(root, leaf1, leaf2):
    if root is None:
        return None

    # 如果根节点的值位于两个叶节点的值之间，根节点就是最近公共祖先
    if root.value > leaf1.value and root.value > leaf2.value:
        return find_lowest_common_ancestor(root.left, leaf1, leaf2)
    elif root.value < leaf1.value and root.value < leaf2.value:
        return find_lowest_common_ancestor(root.right, leaf1, leaf2)
    else:
        return root


# 创建一棵排序二叉树
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

# 查找叶节点的最近公共祖先
leaf1 = root.left.left  # 叶节点 0
leaf2 = root.left.right.right  # 叶节点 5
ancestor = find_lowest_common_ancestor(root, leaf1, leaf2)
print("Lowest Common Ancestor:", ancestor.value)
