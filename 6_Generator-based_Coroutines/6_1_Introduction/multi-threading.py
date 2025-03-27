import time
from threading import Thread


def a():
    time.sleep(1)
    print("Function 'A' executed!\n")


def b():
    time.sleep(1)
    print("Function 'B' executed!\n")


def main():
    t1 = Thread(target=a)
    t2 = Thread(target=b)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == '__main__':
    main()