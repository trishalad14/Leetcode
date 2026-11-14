class MyQueue(object):

    def __init__(self):
        self.s1 = []                   # for push
        self.s2 = []                   # for pop and peek

    def push(self, x):
        self.s1.append(x)

    def transfer(self):
        if not self.s2:                # only when s2 is empty
            while self.s1:             # move everything from s1
                self.s2.append(self.s1.pop())

    def pop(self):
        if self.empty():
            return None
        self.transfer()
        return self.s2.pop()

    def peek(self):
        if self.empty():
            return None
        self.transfer()
        return self.s2[-1]

    def empty(self):
        return not self.s1 and not self.s2