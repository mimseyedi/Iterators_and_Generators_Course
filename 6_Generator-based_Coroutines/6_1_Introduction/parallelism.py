import time
from multiprocessing import Process


def a():
    time.sleep(1)
    print("Function 'A' executed!\n")


def b():
    time.sleep(1)
    print("Function 'B' executed!\n")


def main():
    p1 = Process(target=a)
    p2 = Process(target=b)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    p1.close()
    p2.close()


if __name__ == '__main__':
    main()