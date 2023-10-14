from my_queue import Queue

def main():
    q = Queue()
    print(q)
    # q.enqueue(11)
    print(q)
    aa = q.dequeue()
    print(q)
    print(aa.next)

if __name__ == '__main__':
    main()
