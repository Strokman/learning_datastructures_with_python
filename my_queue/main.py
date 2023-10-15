from my_queue import Queue

def main():
    q = Queue(11)
    print(q.dequeue())
    print(q)
    q.enqueue(1)
    print(q)
    b = Queue(1, 5, 6)
    print(b)
    b.enqueue(2)
    print(b)
if __name__ == '__main__':
    main()
