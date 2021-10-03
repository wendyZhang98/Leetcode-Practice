### Link：
# https://github.com/doocs/leetcode/blob/main/solution/0200-0299/0225.Implement%20Stack%20using%20Queues/README.md


### Description:
# 请你仅使用两个队列实现一个后入先出（LIFO）的栈
# 并支持普通队列的全部四种操作（push、top、pop 和 empty）


# 实现 MyStack 类：
# void push(int x) 将元素 x 压入栈顶。
# int pop() 移除并返回栈顶元素。
# int top() 返回栈顶元素。
# boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。


# 注意：
# 你只能使用队列的基本操作
# 也就是 push to back、peek/pop from front、size 和 is empty 这些操作
# 你所使用的语言也许不支持队列
# 你可以使用 list（列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。


# 输入：
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# 输出：
# [null, null, null, 2, 2, false]


# 解释：
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // 返回 2
# myStack.pop(); // 返回 2
# myStack.empty(); // 返回 False


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []


    def push(self, x):
        """
        Push element x onto stack.
        """
        self.q.append(x)
        n = len(self.q)
        for i in range(n-1):
            self.q.append(self.q.pop(0))
            # .pop(0) returns the 1st element of the list


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.pop(0)


    def top(self):
        """
        Get the top element.
        """
        return self.q[0]


    def empty(self):
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

