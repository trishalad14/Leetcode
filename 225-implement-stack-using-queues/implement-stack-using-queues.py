from collections import deque
class MyStack(object):





    def __init__(self):
        self.q = deque()               # the front of q is the top of the stack

    

    # Insert an element into the stack
    def push(self, value):
        self.q.append(value)                       # 1) add at the rear
        for _ in range(len(self.q) - 1):           # 2) rotate all the OLD elements
            self.q.append(self.q.popleft())        #    from front to rear
      

    # Remove the top element
    def pop(self):
        if self.empty():
            
            return None
        value = self.q.popleft()                   # the front is the top
       
        return value

    # Display the top element
    def top(self):
        if self.empty():
            
            return None
        
        return self.q[0]
    # Check whether stack is empty
    def empty(self):
        return len(self.q) == 0

    
   

