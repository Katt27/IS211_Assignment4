import time
import random

def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1

    end = time.time()
    return found, end-start

def ordered_sequential_search(a_list, item):
    a_list.sort()  # Ensure the list is sorted
    start = time.time()
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos += 1

    end = time.time()
    return found, end-start

def binary_search_iterative(a_list, item):
    a_list.sort()
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end = time.time()
    return found, end-start

def binary_search_recursive(a_list, item):
    a_list.sort()

    def binary_search(a_list, item, start, end):
        if start > end:
            return False

        midpoint = (start + end) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search(a_list, item, start, midpoint-1)
            else:
                return binary_search(a_list, item, midpoint+1, end)

    start = time.time()
    result = binary_search(a_list, item, 0, len(a_list) - 1)
    end = time.time()
    return result, end-start


def generate_random_list(size):
    return [random.randint(1, 10000) for _ in range(size)]


def benchmark_search_functions(sizes=[500, 1000, 5000]):
    for size in sizes:
        total_time = {'sequential_search': 0, 'ordered_sequential_search': 0,
                      'binary_search_iterative': 0, 'binary_search_recursive': 0}
        for _ in range(100):
            test_list = generate_random_list(size)
            _, time_taken = sequential_search(test_list, -1)  # Item not in list
            total_time['sequential_search'] += time_taken
            _, time_taken = ordered_sequential_search(test_list, -1)
            total_time['ordered_sequential_search'] += time_taken
            _, time_taken = binary_search_iterative(test_list, -1)
            total_time['binary_search_iterative'] += time_taken
            _, time_taken = binary_search_recursive(test_list, -1)
            total_time['binary_search_recursive'] += time_taken

        for key in total_time:
            print(f"{key} took {total_time[key]/100:.7f} seconds to run, on average, for list size {size}.")

# Main function to run the benchmarks
def main():
    benchmark_search_functions()

main()
