from collections import deque

#soltion1
#two queues
class MyStack:
    '''
    in - 存數據
    out - 僅在pop時用到
    '''
    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x:int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        #queue_in只留一個，再跟queue_out交換。
        for i in range(len(self.queue_in)-1):
            self.queue_out.append(self.queue_in.popleft())

        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        return self.queue_out.popleft()
    
    def top(self) -> int:
        if self.empty():
            return None
        
        for i in range(len(self.queue_in)-1):
            self.queue_out.append(self.queue_in.popleft())

        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        temp = self.queue_out.popleft()
        self.queue_in.append(temp)
        return temp

    def empty(self) -> bool:
        return len(self.queue_in) == 0
    
#solution2
#one queue
class MyStack:
    '''
    in - 存數據
    out - 僅在pop時用到
    '''
    def __init__(self):
        self.que = deque()

    def push(self, x:int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.que)-1):
            self.que.append(self.que.popleft())
        return self.que.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.que)-1):
            self.que.append(self.que.popleft())
        temp = self.que.popleft()
        self.que.append(temp)
        return temp


    def empty(self) -> bool:
        return not self.que
    
#solution3
#one queue
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x:int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop()
    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue)==0
