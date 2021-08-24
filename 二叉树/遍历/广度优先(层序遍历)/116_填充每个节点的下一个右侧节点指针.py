# coding:utf-8

'''
date: 2021/08/24
content:
题目链接:https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/

给定一个"完美二叉树"，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有next 指针都被设置为 NULL。


进阶：
你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

示例：
输入：root = [1,2,3,4,5,6,7]
输出：[1,#,2,3,#,4,5,6,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。

提示：
树中节点的数量少于4096
-1000 <= node.val <= 1000
'''


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from collections import deque

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if root is None:
            return root

        q = deque([root])
        while q:
            q_size = len(q)
            former_node = None
            for i in range(q_size):
                node = q.popleft()

                if former_node is not None:
                    former_node.next = node
                former_node = node

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return root

