
import time
import random


def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
    end = time.time()
    return end-start

def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2
    end = time.time()
    return end-start

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value

def python_sort(a_list):
    start = time.time()
    a_list.sort()
    end = time.time()
    return end-start


def generate_random_list(size):
    return [random.randint(1, 10000) for _ in range(size)]


def benchmark_sort_functions(sizes=[500, 1000, 5000]):
    for size in sizes:
        total_time = {'insertion_sort': 0, 'shell_sort': 0, 'python_sort': 0}
        for _ in range(100):
            test_list = generate_random_list(size)
            time_taken = insertion_sort(test_list.copy())
            total_time['insertion_sort'] += time_taken
            time_taken = shell_sort(test_list.copy())
            total_time['shell_sort'] += time_taken
            time_taken = python_sort(test_list.copy())
            total_time['python_sort'] += time_taken

        for key in total_time:
            print(f"{key} took {total_time[key]/100:.7f} seconds to run, on average, for list size {size}.")


def main():
    benchmark_sort_functions()


main()
