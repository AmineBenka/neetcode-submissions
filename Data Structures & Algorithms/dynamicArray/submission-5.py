class DynamicArray:
    
    def __init__(self, capacity: int):
        self.L = []
        self.capacity = capacity


    def get(self, i: int) -> int:
        return self.L[i]

    def set(self, i: int, n: int) -> None:
        self.L[i] = n


    def pushback(self, n: int) -> None:
        if len(self.L) == self.capacity:
            self.resize()
        self.L.append(n)

    def popback(self) -> int:
        return self.L.pop()
 

    def resize(self) -> None:
        self.capacity+= self.capacity


    def getSize(self) -> int:
        return len(self.L)
        
    
    def getCapacity(self) -> int:
        return self.capacity
