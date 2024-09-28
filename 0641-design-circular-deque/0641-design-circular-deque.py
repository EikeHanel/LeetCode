class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = []
        self.size = k

    def insertFront(self, value: int) -> bool:
        if len(self.deque) < self.size:
            self.deque.insert(0, [value])
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.deque) < self.size:
            self.deque.append([value])
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.deque == []:
            return False
        else:
            self.deque.pop(0)
            return True

    def deleteLast(self) -> bool:
        if self.deque == []:
            return False
        else:
            print(self.deque)
            self.deque.pop()
            return True

    def getFront(self) -> int:
        if self.deque == []:
            return -1
        else: 
            return self.deque[0][0] 

    def getRear(self) -> int:
        print(self.deque)
        if self.deque == []:
            return -1
        else: 
            return self.deque[-1][0] 

    def isEmpty(self) -> bool:
        if self.deque == None:
            return True
        else: 
            return False

    def isFull(self) -> bool:
        if len(self.deque) < self.size:
            return False
        else: 
            return True


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()