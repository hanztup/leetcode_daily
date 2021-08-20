# coding:utf-8

'''
date: 2021/6/7
content:
请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通队列的全部四种操作（push、top、pop 和 empty）。

实现 MyStack 类：
void push(int x) 将元素 x 压入栈顶。
int pop() 移除并返回栈顶元素。
int top() 返回栈顶元素。
boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。


注意：
你只能使用队列的基本操作 —— 也就是push to back、peek/pop from front、size 和is empty这些操作。
你所使用的语言也许不支持队列。你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列, 只要是标准的队列操作即可。

示例：

输入：
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 2, 2, false]

解释：
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // 返回 2
myStack.pop(); // 返回 2
myStack.empty(); // 返回 False

提示：
1 <= x <= 9
最多调用100 次 push、pop、top 和 empty
每次调用 pop 和 top 都保证栈不为空

进阶：你能否实现每种操作的均摊时间复杂度为 O(1) 的栈？
换句话说，执行 n 个操作的总时间复杂度 O(n) ，尽管其中某个操作可能需要比其他操作更长的时间。
你可以使用两个以上的队列。
'''

class MyStack(object):

    '''
    解法一
    思路：要明确我有的是队列，那么操作细节要遵守队列的规矩，要实现的是栈，那么函数的返回要遵守栈的规矩。
    - init: 初始化两个队列，queue1作为底层的结构，queue2作为备选的时候使用，cur_length记录当前栈的长度，top_val记录栈顶元素
    - push: queue1的实现使用列表，遵循"插入在列表末尾O(1)，删除在列表头O(n)"；同时注意更新cur_length和top_val
    - pop: 将queue1中元素全部弹出并保存至queue2，同时保存最后一次弹出的元素为栈顶元素，以及top_val；将queue2中的元素再次全部弹出并保存至queue1
    - top: 直接返回top_val值
    - empty: 直接根据cur_length进行bool判断
    '''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        self.cur_length = 0
        self.top_val = None

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)
        self.top_val = x
        self.cur_length += 1
        return

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.cur_length == 0:
            return -1

        top_element = None
        for i in range(self.cur_length):
            if i != self.cur_length - 1:
                top_element = self.queue1.pop(0)
                self.queue2.append(top_element)
                self.top_val = top_element
            else:
                top_element = self.queue1.pop(0)
        self.cur_length -= 1

        for j in range(self.cur_length):
            self.queue1.append(self.queue2.pop(0))

        return top_element

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.cur_length == 0:
            return -1

        return self.top_val


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.cur_length == 0:
            return True

        return False



# # Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()