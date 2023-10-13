from stack import Stack


def main():
    st = Stack(1)
    print(st.pop())
    print(st)
    st.push(11)
    st.push(22222)
    print(len(st))
    print(st)
    b = st.pop()
    print(b.next)


if __name__ == '__main__':
    main()
