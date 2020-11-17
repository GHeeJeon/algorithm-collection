import random
import time

def random_list(size):
    return [random.randint(1, 512) for i in range(size)]


def ordered_list(size):
    return list(range(1, size + 1))


def reverse_ordered_list(size):
    return list(range(size, 0, -1))


def elapsed_time(action):
    start_time = time.time()
    action()
    end_time = time.time()

    return (end_time - start_time) * 1000


if __name__ == "__main__":
    print(elapsed_time(lambda: print("hi! I'm very fast")))
