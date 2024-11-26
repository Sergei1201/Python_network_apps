from multiprocessing import Process, cpu_count
import time


def count(num):
    count = 0
    while count < num:
        count += 1


def main():

    print(cpu_count())
    # Implementing multiprocesses in python to boost the application performance
    a = Process(target=count, args=(25000000,))
    b = Process(target=count, args=(25000000,))
    c = Process(target=count, args=(25000000,))
    d = Process(target=count, args=(25000000,))

    # a.start()
    # b.start()
    # c.start()
    # d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print(f'The process took {time.perf_counter()} to complete')


if __name__ == '__main__':
    main()
