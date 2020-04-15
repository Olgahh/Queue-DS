class Queue {
  constructor() {
    this.queue = [];
  }
  enqueue(item) {
    this.queue.push(item);
  }
  dequeue() {
    return this.queue.shift();
  }
  peek() {
    return this.queue[0];
  }
  size() {
    return this.queue.length;
  }
  isEmpty() {
    return this.queue.length === 0;
  }
  print() {
    console.log(this.queue.join(" , "));
  }
}

var q = new Queue();
console.log(q.isEmpty());
q.enqueue(10);
q.enqueue(20);
q.enqueue(30);
q.print();
console.log(q.peek());
console.log(q.dequeue());
q.print();
