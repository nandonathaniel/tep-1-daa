import numpy as np
import os

sizes = [2**9, 2**13, 2**16]

statuses = ['sorted', 'random', 'reversed']

if not os.path.exists('arrays'):
    os.makedirs('arrays')

for size in sizes:
    for status in statuses:
        filename = f'arrays/array_{size}_{status}.txt'
        if status == 'sorted':
            array = np.arange(size)
        elif status == 'random':
            array = np.random.randint(0, size, size)
        elif status == 'reversed':
            array = np.arange(size, 0, -1)
        with open(filename, 'w') as file:
            for item in array:
                file.write(str(item) + '\n')

print("Arrays generated and saved in the 'arrays' directory.")