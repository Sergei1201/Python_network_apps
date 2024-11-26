import time
import threading


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(f'Logged it for {count} seconds')


x = threading.Thread(target=timer, daemon=True)
x.start()


answer = input('Do you wish to exit the program?')
