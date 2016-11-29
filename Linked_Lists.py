class LinkedStack:
    class _node:
        _slots__ = '_element', ' _next'
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0
    def __str__(self):
        print str(self._node)

    def __len__(self):
        return self._size

    def is_empty(self):
         return self._size ==0

    def push(self, e):
        self._head = self._node(e, self._head)
        self._size+=1

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._head._element
    def pop(self):
        if self.is_empty():
            raise Exception('stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer




    def merge(self, head1, head2):
        #with help of internet#
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        s = t = self._node
        while not (head1 is None or head2 is None):
            if head1._size  < head2._size:
                c = head1
                head1 = head1._next
        else:
            c = head2
            head2 = head2._next
        t._next = c
        t = t._next
        t.next = head1 or head2
        return c._next

x = LinkedStack()
l = LinkedStack()
l.push([5,6,7])
x.push([6,2,1,8,4])
print x.merge(l,x)
print x