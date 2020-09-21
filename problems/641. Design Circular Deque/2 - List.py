class MyCircularDeque:
    def __init__(self, k: int):
        self.__capacity = k
        self.__size = 0
        self.__data = [-1] * k
        self.__front = -1
        self.__rear = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.__front = (self.__front + 1) % self.__capacity
        self.__data[self.__front] = value
        self.__size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.__rear = (self.__rear - 1) % self.__capacity
        self.__data[self.__rear] = value
        self.__size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.__data[self.__front] = -1
        self.__front = (self.__front - 1) % self.__capacity
        self.__size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.__data[self.__rear] = -1
        self.__rear = (self.__rear + 1) % self.__capacity
        self.__size -= 1
        return True

    def getFront(self) -> int:
        return self.__data[self.__front]

    def getRear(self) -> int:
        return self.__data[self.__rear]

    def isEmpty(self) -> bool:
        return self.__size == 0

    def isFull(self) -> bool:
        return self.__size == self.__capacity
