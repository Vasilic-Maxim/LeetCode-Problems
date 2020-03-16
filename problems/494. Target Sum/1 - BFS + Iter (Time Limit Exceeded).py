'''
While we iterate throughout the 'nums' list the queue becomes huge,
O(2^N) where N is the length of the array, hence the solution
becomes slower and less effective.

N - length of the array
Time: O(2^N)
Space: O(N*2^N)
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = self.rear = None
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def enQueue(self, x):
        if self.isEmpty():
            self.front = self.rear = Node(x)
        else:
            self.rear.next = Node(x)
            self.rear = self.rear.next
        self.size += 1
    
    def deQueue(self):
        if self.isEmpty():
            return
        
        tmp = self.front
        
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        
        self.size -= 1
        
        return tmp.val
    
    def peek(self):
        if not self.isEmpty():
            return self.front
    
    def isEmpty(self):
        return not self.front

class Solution:
    def findTargetSumWays(self, nums: list, target: int) -> int:
        q = Queue()
        q.enQueue(0)
        for num in nums:
            for _ in range(len(q)):
                elm = q.deQueue()
                q.enQueue(elm - num)
                q.enQueue(elm + num)
        return sum([x for _ in range(len(q)) if (x := q.deQueue() == target)])

s = Solution()
print(s.findTargetSumWays([42,24,30,14,38,27,12,29,43,42,5,18,0,1,12,44,45,50,21,47], 38))