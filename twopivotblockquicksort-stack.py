import os
import threading
import time

import sys

def partition(left, right):
    p = arr[left]
    q = arr[right]
    i = left + 1
    j = left + 1
    k = left + 1
    num_p = 0
    num_q = 0
    while k < right:
        t = min(B, right-k)
        for c in range(t):
            block[num_q] = c
            num_q += (q >= arr[k+c])
        for c in range(num_q):
            arr[j+c], arr[k+block[c]] = arr[k+block[c]], arr[j+c]
        k += t
        for c in range(num_q):
            block[num_p] = c
            num_p += (p > arr[j+c])
        for c in range(num_p):
            arr[i], arr[j+block[c]] = arr[j+block[c]], arr[i]
            i += 1
        j += num_q
        num_p = 0
        num_q = 0
    arr[i-1], arr[left] = arr[left], arr[i-1]
    arr[j], arr[right] = arr[right], arr[j]
    return (i-1,j)


def TwoPivotQuicksort():
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]
    while stack:
        left, right = stack.pop()
        if left < right:
            if arr[left] > arr[right]:
                arr[left], arr[right] = arr[right], arr[left]
            i, j = partition(left, right)
            stack.append((left, i-1))
            stack.append((i + 1, j - 1))
            stack.append((j + 1, right))
    
    return arr


def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
from memory_profiler import memory_usage

def profile_memory(func):
    def wrapper(*args, **kwargs):
        def target():
            return func(*args, **kwargs)
        
        mem_usage, retval = memory_usage(target, interval=.1, timeout=1, retval=True, max_usage=True)
        print(f">{func.__name__}'s memory usage: {mem_usage} MiB.")
        return retval
    return wrapper

@profile_memory
def main():
    start_time = time.time()
    sorted_arr = TwoPivotQuicksort()
    end_time = time.time()
    runtime = (end_time - start_time) * 1000
    print(f"Processing Two Pivot Block Quicksort of {file_name} complete. Runtime: {runtime:.2f} milliseconds")
    if is_sorted(sorted_arr):
        print("aman")
    else:
        print("tidak aman")


if __name__ == "__main__":

    B = 1024
    block = []
    for i in range(B):
        block.append(-1)
    folder_path = "arrays"

    txt_files = [file for file in os.listdir(folder_path) if file.endswith(".txt")]

    for file_name in txt_files:
        file_path = os.path.join(folder_path, file_name)
        start_time = time.time()
        with open(file_path, 'r') as file:
            lines = file.readlines()
            arr = []
            for line in lines:
                arr.append(int(line.strip()))
        main()
    

    # sys.setrecursionlimit(100000)
    # threading.stack_size(2**27)
    # thread = threading.Thread(target=main)
    # thread.start()