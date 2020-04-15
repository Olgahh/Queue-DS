class CircularQueue():
    def __init__(self,size):
        self.size=size
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1

    def enqueue(self,item):
        #is it is full
        if ((self.rear+1)%self.size == self.front):
            print("Q is full")
        # is it empty?
        elif(self.front == -1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=item
        else:
            self.rear = (self.rear+1)%self.size
            self.queue[self.rear]=item
    def dequeue(self):
        if(self.front == -1):
            print("Q is empty")
        elif (self.front ==self.rear):
            temp=self.queue[self.front]
            self.front= -1
            self.rear= -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front=(self.front+1) %self.size
            return temp

    def display(self):
        if(self.front == -1):
            print("Q is Empty")
        elif(self.rear >=self.front):
            print("Queue= ",end=" ")
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
            print ()

        else:
            print("Queue= ",end=" ")
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
            print ()
        if ((self.rear+1)%self.size==self.front):
            print("Q is Full")

q= CircularQueue(4)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.display()
print("Deleted value=",q.dequeue())
print("Deleted value=",q.dequeue())
q.display()
q.enqueue(1)
q.enqueue(2)
q.display()

