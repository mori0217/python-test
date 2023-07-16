
import os
import time
import concurrent.futures


LARGE_TEXT = 'large text' * 100000000


def io_bound(file_name: str):
    file_path = "section22/"+file_name
    with open(file_path, 'w+') as f:
        f.write(LARGE_TEXT)
        f.seek(0)
        f.read()
    os.remove(file_path)
    return 'io_bound is done!'


def cpu_bound():
    sum(i**2 for i in range(10**6))
    return 'cpu_bound is done!'


if __name__ == '__main__':
    start = time.time()
    print(io_bound('file1.txt'))
    print(io_bound('file2.txt'))
    end = time.time()
    print(f'io_bound time: {end - start}')

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        start = time.time()
        print(executor.submit(io_bound, 'file1.txt').result())
        print(executor.submit(io_bound, 'file2.txt').result())
        end = time.time()
        print(f'io_bound Thread time: {end - start}')

    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        start = time.time()
        print(executor.submit(io_bound, 'file1.txt').result())
        print(executor.submit(io_bound, 'file2.txt').result())
        end = time.time()
        print(f'io_bound Process time: {end - start}')

    start = time.time()
    print(cpu_bound())
    print(cpu_bound())
    end = time.time()
    print(f'cpu_bound time: {end - start}')

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        start = time.time()
        print(executor.submit(cpu_bound).result())
        print(executor.submit(cpu_bound).result())
        end = time.time()
        print(f'cpu_bound Thread time: {end - start}')

    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        start = time.time()
        print(executor.submit(cpu_bound).result())
        print(executor.submit(cpu_bound).result())
        end = time.time()
        print(f'cpu_bound Process time: {end - start}')
