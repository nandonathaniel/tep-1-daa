import os
import time


def merge(A, B):
    i = 0
    j = 0
    result = []
    
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1

    while i < len(A):
        result.append(A[i])
        i += 1

    while j < len(B):
        result.append(B[j])
        j += 1

    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)

def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) or all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
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
    sorted_arr = merge_sort(arr)
    end_time = time.time()
    runtime = (end_time - start_time) * 1000
    print(f"Processing Two Merge Sort of {file_name} complete. Runtime: {runtime:.2f} milliseconds")
    if is_sorted(sorted_arr):
        print("aman")
    else:
        print("tidak aman")

if __name__ == "__main__":
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
